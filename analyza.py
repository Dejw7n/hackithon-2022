from ast import arg
from locale import normalize
from multiprocessing.dummy import Array
from statistics import mean
from tokenize import String
import pandas as pd
import sqlite3
import datetime
import flask

con = sqlite3.connect("data/Gadgetbridge.sqlite")
data = pd.read_sql_query("SELECT * FROM MI_BAND_ACTIVITY_SAMPLE", con)
info = pd.read_csv("data/info.csv")

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

def getClass():
    
    return

def GetData(datas, sloupce = data.columns.values, podle = None, metody = None, co = None):
    """
        datas = jaká data
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
    al = datas.count()
    n = datas[co].value_counts(normalize=True)
    return n

def GetMereny(datas):
    """Vrátí data mezi 1-254"""
    prom = "hr" if "hr" in datas.columns.values else "HEART_RATE"
    return datas.query(f"{prom} > 0 and {prom} < 255")

def Vypis(datas):
    print(datas.to_markdown())

def GetActivity(x):
    for activity in activity_dictionary:
        if x in activity_dictionary[activity]:
            return activity
    return "Unknown"

def PrelozActivity(datas):
    datas["ACTIVITY"] = datas["RAW_KIND"].map(GetActivity)
    return datas

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

def PrelozDatum(datas):
    datas["TIMESTAMP"] = datas["TIMESTAMP"].apply(lambda x: datetime.datetime.fromtimestamp(x))
    return datas

print(getUserByAlias("Band 01"))

# Get all data, kde neni tep 255, groupni by user a napis sum + mean hr
#result = GetData(GetMereny(GetData(data, sloupce=["user", "hr", "steps"])), podle=["user"], metody=[sum, mean], co=["hr", "steps"])

#print(PrelozActivity(data))

#print(Compare(data, "RAW_KIND"))

print(PrelozDatum(data))