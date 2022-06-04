from copy import deepcopy
import analyza

##########NEDODĚLANÉ###########
def CompareStepsBySex():
    return analyza.GetData(analyza.data.merge(analyza.info, on=["ALIAS", "alias"]))

def GetCountInactive():
    return analyza.GetData(analyza.device.merge(analyza.info, how="outer", on=""), metody=["size"])["NAME"]["size"]

################################

#Vrací náramky, u kterých jsou data dostupná
def GetCountActiveGeneral():
    return analyza.GetData(analyza.info, metody=["size"])["id"]["size"]
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
GetCountActive = GetCountActiveGeneral()



print(GetCountActive)
