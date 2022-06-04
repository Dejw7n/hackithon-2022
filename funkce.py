import analyza

def CompareStepsBySexGeneral(datas):
    k = analyza.GetData(datas, podle=["user"], metody=["sum"], co=["steps"]).merge(analyza.info, left_on="user", right_on="id")
    k["sum steps"] = k[("steps", "sum")]
    del k[("steps", "sum")]
    k = analyza.GetData(k, podle=["sex"], metody=["mean"], co=["sum steps"]).to_dict()[('sum steps', 'mean')]
    s = (k["male"]+k["female"])/100
    k = analyza.pd.DataFrame(columns=["sex", "mean daily steps", "ratio"], data=[["male", k["male"], f"{round(k['male']/s, 2)}%"], ["female", k["female"], f"{round(k['female']/s, 2)}%"]])
    return k

#Vrací průměrný počet kroků celé třídy za všechny dny
def GetAllAvgDayStepsForAllGeneral(datas):
    return analyza.GetData(analyza.GetMereny(datas), metody=["mean"], co=["STEPS"])*60*24

#Vrací počet kroků studenta za všechny dny
def GetSumDayStepsForUsersGeneral(datas):
    k = datas.copy(deep=True)
    k["TIMESTAMP"] = analyza.pd.to_datetime(k["TIMESTAMP"]*1000000000)
    k["DAY"] = k["TIMESTAMP"].dt.day
    k["WEEKDAY"] = k["TIMESTAMP"].dt.weekday
    k = k.groupby(by=["DEVICE_ID", "DAY"]).agg({"STEPS": "sum"})
    k["STEPS"] = k["STEPS"].map(lambda x: x*60*24)
    return k

#Vrací průmer kroků studenta za všechny dny
def GetAvgDayStepsForUsersGeneral(datas):
    k = datas.copy(deep=True)
    k["TIMESTAMP"] = analyza.pd.to_datetime(k["TIMESTAMP"]*1000000000)
    k = k.groupby("DEVICE_ID").agg({"STEPS": "mean"})
    k["STEPS"] = k["STEPS"].map(lambda x: x*60*24)
    return k

#Vrací průměr kroků třídy za všechny dny
def GetAvgDayStepsForAllGeneral(datas):
    k = datas.copy(deep=True)
    k["TIMESTAMP"] = analyza.pd.to_datetime(k["TIMESTAMP"]*1000000000)
    k["DAY"] = k["TIMESTAMP"].dt.day
    k = k.groupby("DAY").agg({"STEPS": "mean"})
    k["STEPS"] = k["STEPS"].map(lambda x: x*24*60)
    return k

GetAvgDayStepsForAll = GetAvgDayStepsForAllGeneral(analyza.data)
GetAvgDayStepsForUsers = GetAvgDayStepsForUsersGeneral(analyza.data)
GetSumDayStepsForUsers = GetSumDayStepsForUsersGeneral(analyza.data)
GetAllAvgDayStepsForAll = GetAllAvgDayStepsForAllGeneral(analyza.data)