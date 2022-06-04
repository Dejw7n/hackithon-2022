import analyza

def CompareStepsBySex():
    return analyza.GetData(analyza.data.merge(analyza.info, on=["ALIAS", "alias"]))

def GetAvgDayStepsForClass():
    return analyza.GetData(analyza.GetMereny(analyza.data), metody=["mean"], co=["STEPS"])*60*24

print(GetAvgDayStepsForClass())