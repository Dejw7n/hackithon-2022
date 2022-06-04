import analyza

pd = analyza.pd

def CompareStepsBySexGeneral(datas):
    k = analyza.GetData(datas, podle=["user"], metody=["sum"], co=["steps"]).merge(analyza.info, left_on="user", right_on="id")
    k["sum steps"] = k[("steps", "sum")]
    del k[("steps", "sum")]
    k = analyza.GetData(k, podle=["sex"], metody=["mean"], co=["sum steps"]).to_dict()[('sum steps', 'mean')]
    s = (k["male"]+k["female"])/100
    k = pd.DataFrame(columns=["sex", "mean daily steps", "ratio"], data=[["male", k["male"], f"{round(k['male']/s, 2)}%"], ["female", k["female"], f"{round(k['female']/s, 2)}%"]])
    return k

#Vrací průměrný počet kroků celé třídy za všechny dny
def GetAllAvgDayStepsForAllGeneral(datas):
    return analyza.GetData(analyza.GetMereny(datas), metody=["mean"], co=["STEPS"])*60*24

#Vrací počet kroků studenta za všechny dny
def GetSumDayStepsForUsersGeneral(datas):
    k = datas.copy(deep=True)
    k["TIMESTAMP"] = pd.to_datetime(k["TIMESTAMP"]*1000000000)
    k["DAY"] = k["TIMESTAMP"].dt.day
    k["WEEKDAY"] = k["TIMESTAMP"].dt.weekday
    k = k.groupby(by=["DEVICE_ID", "DAY"]).agg({"STEPS": "sum"})
    k["STEPS"] = k["STEPS"].map(lambda x: x*60*24)
    return k

#Vrací průmer kroků studenta za všechny dny
def GetAvgDayStepsForUsersGeneral(datas):
    k = datas.copy(deep=True)
    k["TIMESTAMP"] = pd.to_datetime(k["TIMESTAMP"]*1000000000)
    k = k.groupby("DEVICE_ID").agg({"STEPS": "mean"})
    k["STEPS"] = k["STEPS"].map(lambda x: x*60*24)
    return k

#Vrací průměr kroků třídy za všechny dny
def GetAvgDayStepsForAllGeneral(datas):
    k = datas.copy(deep=True)
    k["TIMESTAMP"] = pd.to_datetime(k["TIMESTAMP"]*1000000000)
    k["DAY"] = k["TIMESTAMP"].dt.day
    k = k.groupby("DAY").agg({"STEPS": "mean"})
    k["STEPS"] = k["STEPS"].map(lambda x: x*24*60)
    return k


def FormatSchedule():
    days = {} 
    day = None
    subject = None
    for (key, value) in analyza.schedule.groupby("day"):
        value = analyza.GetData(value, sloupce=["subject", "from", "to", "school"])
        day = []
        for _, row in value.iterrows():
            subject = []
            for _, v in row.items():
                subject.append(v)
            day.append(subject)
        days[key] = day
    return days

import analyza

def CompareStepsBySexGeneral(datas):
    k = analyza.GetData(datas, podle=["user"], metody=["sum"], co=["steps"]).merge(analyza.info, left_on="user", right_on="id")
    k["sum steps"] = k[("steps", "sum")]
    del k[("steps", "sum")]
    k = analyza.GetData(k, podle=["sex"], metody=["mean"], co=["sum steps"]).to_dict()[('sum steps', 'mean')]
    s = (k["male"]+k["female"])/100
    k = pd.DataFrame(columns=["sex", "mean daily steps", "ratio"], data=[["male", k["male"], f"{round(k['male']/s, 2)}%"], ["female", k["female"], f"{round(k['female']/s, 2)}%"]])
    return k

#Vrací průměrný počet kroků celé třídy za všechny dny
def GetAllAvgDayStepsForAllGeneral(datas):
    return analyza.GetData(analyza.GetMereny(datas), metody=["mean"], co=["STEPS"])*60*24

#Vrací počet kroků studenta za všechny dny
def GetSumDayStepsForUsersGeneral(datas):
    k = datas.copy(deep=True)
    k["TIMESTAMP"] = pd.to_datetime(k["TIMESTAMP"]*1000000000)
    k["DAY"] = k["TIMESTAMP"].dt.day
    k["WEEKDAY"] = k["TIMESTAMP"].dt.weekday
    k = k.groupby(by=["DEVICE_ID", "DAY"]).agg({"STEPS": "sum"})
    k["STEPS"] = k["STEPS"].map(lambda x: x*60*24)
    return k

#Vrací průmer kroků studenta za všechny dny
def GetAvgDayStepsForUsersGeneral(datas):
    k = datas.copy(deep=True)
    k["TIMESTAMP"] = pd.to_datetime(k["TIMESTAMP"]*1000000000)
    k = k.groupby("DEVICE_ID").agg({"STEPS": "mean"})
    k["STEPS"] = k["STEPS"].map(lambda x: x*60*24)
    return k

#Vrací průměr kroků třídy za všechny dny
def GetAvgDayStepsForAllGeneral(datas):
    k = datas.copy(deep=True)
    k["TIMESTAMP"] = pd.to_datetime(k["TIMESTAMP"]*1000000000)
    k["DAY"] = k["TIMESTAMP"].dt.day
    k = k.groupby("DAY").agg({"STEPS": "mean"})
    k["STEPS"] = k["STEPS"].map(lambda x: x*24*60)
    return k


def FormatSchedule():
    days = {} 
    day = None
    subject = None
    for (key, value) in analyza.schedule.groupby("day"):
        value = analyza.GetData(value, sloupce=["subject", "from", "to", "school"])
        day = []
        for _, row in value.iterrows():
            subject = []
            for _, v in row.items():
                subject.append(v)
            day.append(subject)
        days[key] = day
    return days

def GetSubjectsOnData():
    school_df = pd.read_csv('data/data_school.csv', parse_dates = ['datetime'])

    sched_df = pd.read_csv('data/schedule.csv')
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

def GetAvgHeartRateBySubject():
    return GetSubjectsOnData()

def GetColorByHeartRate(hr):
    return '%02x%02x%02x' % (-51/4*hr+2805/2, 52/4*hr-2295/2, 0) 

GetAvgDayStepsForAll = GetAvgDayStepsForAllGeneral(analyza.data)
GetAvgDayStepsForUsers = GetAvgDayStepsForUsersGeneral(analyza.data)
GetSumDayStepsForUsers = GetSumDayStepsForUsersGeneral(analyza.data)
GetAllAvgDayStepsForAll = GetAllAvgDayStepsForAllGeneral(analyza.data)

GetAvgDayStepsForAll = GetAvgDayStepsForAllGeneral(analyza.data)
GetAvgDayStepsForUsers = GetAvgDayStepsForUsersGeneral(analyza.data)
GetSumDayStepsForUsers = GetSumDayStepsForUsersGeneral(analyza.data)
GetAllAvgDayStepsForAll = GetAllAvgDayStepsForAllGeneral(analyza.data)

print(analyza.GetData(analyza.GetMereny(GetAvgHeartRateBySubject()), podle=["subject"], metody=["mean"], co=["hr"]))