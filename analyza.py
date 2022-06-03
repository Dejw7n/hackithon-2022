from ast import arg
from locale import normalize
from multiprocessing.dummy import Array
from statistics import mean
from tokenize import String
import pandas as pd
import sqlite3
import flask

con = sqlite3.connect("hackithon-2022\data\Gadgetbridge.sqlite")
data = pd.read_sql_query("SELECT * FROM MI_BAND_ACTIVITY_SAMPLE", con)

activity_dictionary = {
    1 : "Chodí",
    112 : "Spí",
    80 : "Žádné kroky",
    115 : "Nenosí",
    16 : "0h Timestamp",
    17 : "Rychle chodí",
    19 : "Bež do postele",
    123 : "Usl/a",
    122 : "sleep, raw_intensity =<20"
}
activity_dictionary_keys = activity_dictionary.keys()

def getUser(alias):
    
    
    return

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
    print(data.columns)
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

def Mereno(hr):
    return hr!=255

# Vrátí data bez hr=255
def GetMereny(datas):
    """Vrátí data bez "hr"=255"""
    return datas[Mereno(datas["hr"])]

def Vypis(datas):
    print(datas.to_markdown())

def PrelozActivity(datas):
    datas["ACTIVITY"] = datas["RAW_KIND"].map(lambda x: activity_dictionary[x] if x in activity_dictionary_keys else "unknown")
    return datas

# Get all data, kde neni tep 255, groupni by user a napis sum + mean hr
#result = GetData(GetMereny(GetData(data, sloupce=["user", "hr", "steps"])), podle=["user"], metody=[sum, mean], co=["hr", "steps"])

print(PrelozActivity(data))

print(Compare(data, "RAW_KIND"))