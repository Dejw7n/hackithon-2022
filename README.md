# HACKITHON 2022 - Analýza pohybové aktivity z chytrých náramků

**FitStats** je webová aplikace zabývající se zpracováním dat z náramků značky Xiaomi Mi Band 4.
Data se po zpracování zobrazí ve webovém rozhraní.

## Použité technologie
 - ### FRONTEND
   - HTML/CSS
   - JavaScript
   - Plotly
   - TailWind

 - ### BACKEND
   - Python
     - Flask
     - Pandas
     - Sqlite3
  
## Dokumentace kódu

### analyza.py

`Vypis(datas = jaká datas)`
 - Vypíše data

`GetData(datas = jaká datas, sloupce = jaké sloupce má vybrat, podle = podle čeho má seskupit, metody = jaké metody má použít, co = na jaké sloupce má použít "metody")`
 - Vrací vyfiltrované data z databáze

`Compare(datas = jaká datas, co = jaký sloupec)`
 - Porovná data a vrátí poměr v %

`GetMereny(datas = jaká datas)`
 - Vrací data s hodnotou heart rate mezi 1-254

`GetMinutesByDeltaTime(start = čas začátku, end = čas konce)`
 - Vrací minuty mezi rozdílem startu a endu

`GetDifferenceMinutes(datas = jaká datas)`
 - Vrací 10 % z rozdílu Max a Min hodnotou času

`GetWorn(datas = jaká datas)`
 - Vrací vyfiltrované data jen náramky které jsou nošené

`GetUserByAlias(alias)`
 - Vrací uživatele podle aliasu daného náramku
  
`GetUserReport(alias)`
 - Vrací statistiku uživatele podle aliasu daného náramku

`GetClassReport()`
 - Vrací data célé třídy

`GetActivity(x = aktivita)`
 - Vrací aktivitu (spánek, chůze, běh)

`PrelozActivity(datas = jaká datas)`
 - Vrací výsledek převodu kódového označení na string

`PrelozDatum(datas = jaká datas)`
 - Vrací výsledek převodu času na českou normu
  
`GetMethodBetweenDates(datas = jaká datas, start = začátek čas, end = konec čas, method = metoda)`
 - Provede vloženou metodu na všech záznamech začínajících s časem start a končícívh s časem end

`GetDataOnDays(datas = jaká datas, days = index dnu)`
 - Vrací vyfiltrované data podle indexu dnu

### funkce.py

`GetCountActive()`
 - Vrací náramky u kterých jsou data dostupná

<<<<<<< HEAD
`GetAllAvgDayStepsForAll()`
 - Vrací průměrný počet kroků celé třídy za všechny dny

`GetSumDayStepsForUsers()`
 - Vrací počet kroků studenta za všechny dny

`GetAvgDayStepsForUsers()`
 - Vrací průmer kroků studenta za všechny dny

`GetAvgDayStepsForAllGeneral(datas)`
 - Vrací průměr kroků třídy za všechny dny
=======
`GetAllAvgDayStepsForClass()`
- 
>>>>>>> 2739f83c0f8006ae6903893c8190d50f94e837af
