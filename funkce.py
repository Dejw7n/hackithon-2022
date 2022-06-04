from copy import deepcopy
import analyza

def CompareStepsBySex():
    return analyza.GetData(analyza.data.merge(analyza.info, on=["ALIAS", "alias"]))

def GetCountActive():
    return analyza.GetData(analyza.device, metody=["size"])["NAME"]["size"]

def GetCountInctive():
    return analyza.GetData(analyza.device, metody=["size"])["NAME"]["size"]

def GetAvgDayStepsForClass():
    return analyza.GetData(analyza.GetMereny(analyza.data), metody=["mean"], co=["STEPS"])*60*24

def GetAvgDayStepsForStudents():
    k = analyza.data.copy(deep=True)
    k["TIMESTAMP"] = analyza.pd.to_datetime(k["TIMESTAMP"]*1000000000)
    k["DAY"] = k["TIMESTAMP"].dt.day
    k["WEEKDAY"] = k["TIMESTAMP"].dt.weekday
    k = k.groupby(by=["DEVICE_ID", "DAY"]).agg({"STEPS": "mean"})
    k["STEPS"] = k["STEPS"].map(lambda x: x*60*24)
    return k

def GetAvgDayStepsForStudent(alias):
    return analyza.GetData(analyza.GetMereny(analyza.data).merge(analyza.info, on=["id", "DEVICE_ID"]), metody=["mean"], co=["STEPS"])


print(GetAvgDayStepsForStudents())