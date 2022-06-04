from ast import arg
from calendar import weekday
from locale import normalize
from multiprocessing.dummy import Array
from statistics import mean
from tokenize import String
from xmlrpc.client import DateTime
import pandas as pd
import sqlite3
import datetime

con = sqlite3.connect("hackithon-2022/data/Gadgetbridge.sqlite")
data = pd.read_sql_query("SELECT * FROM MI_BAND_ACTIVITY_SAMPLE", con)
info = pd.read_csv("hackithon-2022/data/info.csv")
schedule = pd.read_csv("hackithon-2022/data/schedule.csv")

activity_dictionary = {
    "Running" : [98, 50, 66, 82],
    "Walking" : [1, 16, 17, 33, 49, 18, 34, 65],
    "Light_Sleep" : [112],
    "Heavy_Sleep" : [122],
    "Sit" : [80, 96, 99],
    "Standing" : [96],
    "SedentaryInLast5Minutes" : [90],
    "NotWorn" : [3],
    "NotWorn_Charging" : [6],
    "NotWorn_FaceUp" : [83],
    "NotWorn_FaceDown" : [115]
}
def GetData(datas, sloupce = data.columns.values, podle = None, metody = None, co = None):
    """
        datas = jaká datas
        sloupce = jaké sloupce má vybrat
        podle = podle čeho má seskupit

        metody = jaké metody má použít
        co = na jaké sloupce má použít "metody"
    """
    sl = data.loc[:, sloupce]
    if podle != None:
        sl = sl.groupby(by=podle)
    if metody != None:
        if co != None:
            d = {}
            for v in co:
                d[v] = metody
            sl = sl.agg(d)
        else:
            sl = sl.agg(metody)
    return sl

def Compare(datas, co):
    return datas[co].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'

def GetMereny(datas):
    """Vrátí data mezi hr = 1-254"""
    prom = "hr" if "hr" in datas.columns.values else "HEART_RATE"
    return datas.query(f"{prom} > 0 and {prom} < 255")

def GetMinutesByDeltaTime(start, end):
    return (end-start).days*24*60 if isinstance(start, DateTime) else (end-start)/60

def GetDifferenceSeconds(datas):
    new = datas.agg({"TIMESTAMP": [min, max]})["TIMESTAMP"]
    return 0.1*GetMinutesByDeltaTime(new["min"], new["max"])

def GetWorn(datas):
    minTime = GetDifferenceSeconds(datas)
    return GetMereny(datas).groupby("DEVICE_ID").filter(lambda x: len(x) > minTime)

def GetUserByAlias(alias):
    data = pd.read_sql_query(f"SELECT DEVICE.ALIAS, MI_BAND_ACTIVITY_SAMPLE.RAW_INTENSITY, MI_BAND_ACTIVITY_SAMPLE.STEPS, MI_BAND_ACTIVITY_SAMPLE.HEART_RATE FROM MI_BAND_ACTIVITY_SAMPLE JOIN DEVICE ON MI_BAND_ACTIVITY_SAMPLE.DEVICE_ID=DEVICE._id WHERE DEVICE.ALIAS='{alias}'", con)
    user_Info = info[info["alias"] == alias]
    df = GetMereny(data)
    user = {
        "info": user_Info,
        "stats": df
    }
    return user

def GetUserReport(alias):
    datas = pd.read_sql_query(f"SELECT * FROM MI_BAND_ACTIVITY_SAMPLE JOIN DEVICE ON MI_BAND_ACTIVITY_SAMPLE.DEVICE_ID=DEVICE._id JOIN BATTERY ON DEVICE._id=BATTERY.DEVICE_ID", con)
    GetData(datas, sloupce=[""])

def GetClassReport():
    return schedule

def GetActivity(x):
    for activity in activity_dictionary:
        if x in activity_dictionary[activity]:
            return activity
    return "Unknown"

def PrelozActivity(datas):
    datas["ACTIVITY"] = datas["RAW_KIND"].map(GetActivity)
    return datas

def PrelozDatum(datas):
    datas["TIMESTAMP"] = datas["TIMESTAMP"].apply(lambda x: datetime.datetime.fromtimestamp(x))
    datas["PASMO"] = datas["TIMESTAMP"].dt.tz_localize("UTC").dt.tz_convert("CET")
    return datas

def GetMethodBetweenDates(datas, start, end, method):
    new = PrelozDatum(datas)
    return getattr(new[(new["TIMESTAMP"] >= start) & (new["TIMESTAMP"] <= end)], method)()

def GetDataOnDays(datas, days, method):
    new = PrelozDatum(datas)
    new["TIMESTAMP"] = pd.to_datetime(new["TIMESTAMP"])
    new["DAY"] = new["TIMESTAMP"].dt.weekday
    return new[new["DAY"].isin(days)]

def GetSubjectsOnData():
    school_df = pd.read_csv('hackithon-2022/data/data_school.csv', parse_dates = ['datetime'])

    sched_df = pd.read_csv('hackithon-2022/data/schedule.csv')
    sched_df['zacatek'] = pd.to_datetime(sched_df['from'], format = '%H:%M')
    sched_df['konec'] = pd.to_datetime(sched_df['to'], format = '%H:%M')
    del sched_df['from'], sched_df['to']

    school_df['weekday'] = school_df['datetime'].dt.day_name()
    school_df['time'] = pd.to_datetime(pd.to_datetime(school_df['datetime']).dt.strftime("%H:%M"), format="%H:%M")

    df_merge = school_df.merge(sched_df, how = 'cross')
    df_merge = df_merge.query('time >= zacatek and time <= konec')

    df_all=df_merge.merge(school_df, how='outer')
    df_all.day[df_all.day.isnull()] = df_all.weekday[df_all.day.isnull()]
    return df_all

def Vypis(datas):
    print(datas.to_markdown())

print(GetMethodBetweenDates(data, datetime.datetime(2021, 1, 1, 1, 1, 1, 1), datetime.datetime(2022, 1, 1, 1, 1, 1, 1), "mean").to_dict())
