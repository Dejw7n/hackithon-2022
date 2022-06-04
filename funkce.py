from copy import deepcopy
import analyza

##########NEDODĚLANÉ###########
def CompareStepsBySex():
    return analyza.GetData(analyza.data.merge(analyza.info, on=["ALIAS", "alias"]))

def GetCountInactive():
    return analyza.GetData(analyza.device.merge(analyza.info, how="outer", on=""), metody=["size"])["NAME"]["size"]

################################


def GetCountActive():
    return analyza.GetData(analyza.info, metody=["size"])["NAME"]["size"]

def GetAllAvgDayStepsForClass():
    return analyza.GetData(analyza.GetMereny(analyza.data), metody=["mean"], co=["STEPS"])*60*24

def GetSumDayStepsForStudents():
    k = analyza.data.copy(deep=True)
    k["TIMESTAMP"] = analyza.pd.to_datetime(k["TIMESTAMP"]*1000000000)
    k["DAY"] = k["TIMESTAMP"].dt.day
    k["WEEKDAY"] = k["TIMESTAMP"].dt.weekday
    k = k.groupby(by=["DEVICE_ID", "DAY"]).agg({"STEPS": "sum"})
    k["STEPS"] = k["STEPS"].map(lambda x: x*60*24)
    return k

def GetAvgDayStepsForStudents():
    k = analyza.data.copy(deep=True)
    k["TIMESTAMP"] = analyza.pd.to_datetime(k["TIMESTAMP"]*1000000000)
    k = k.groupby("DEVICE_ID").agg({"STEPS": "mean"})
    k["STEPS"] = k["STEPS"].map(lambda x: x*60*24)
    return k

def GetAvgDayStepsForClass():
    k = analyza.data.copy(deep=True)
    k["TIMESTAMP"] = analyza.pd.to_datetime(k["TIMESTAMP"]*1000000000)
    k["DAY"] = k["TIMESTAMP"].dt.day
    k = k.groupby("DAY").agg({"STEPS": "mean"})
    k["STEPS"] = k["STEPS"].map(lambda x: x*24*60)
    return k


print(GetAvgDayStepsForClass())