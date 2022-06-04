# HACKITHON 2022 - Analýza pohybové aktivity z chytrých náramků

**Nazev** je webová aplikace zabývající se zpracováním dat z náramků značky xiaomi band 4.
Data se po zpracování zobrazí ve webovém rozhraní.

## Použité technologie
 - ### FRONTEND
   - HTML/CSS
   - JS
 - ### BACKEND
   - Python
     - Pandas
  
## Dokumentace kódu
`GetData(datas = jaká datas, sloupce = jaké sloupce má vybrat, podle = podle čeho má seskupit, metody = jaké metody má použít, co = na jaké sloupce má použít "metody")`
 - Vrací vyfiltrované data z databáze

`Compare(datas = jaká datas, co = jaký sloupec)`
 - porovná data a vrátí poměr v %

`GetMereny(datas = jaká datas)`
 - Vrací data s hodnotou heart rate mezi 1-254

`GetMinutesByDeltaTime(start = cas začátku, end = čas konce)`
 - Vrací minuty mezi mezi rozdílem startu a endu

`GetDifferenceMinutes(datas = jaká datas)`
 - Vrací 10 % z rozdílu Max a Min hodnotou času

`GetWorn(datas)`
 - Vrací vyfiltrované data jen náramky které jsou nošené

`GetUserByAlias(alias)`
 - Vrací uživatele podle aliasu daného náramku
  
`GetUserReport(alias)`
 - Vrací statistiku uživatele podle aliasu daného náramku

`GetClassReport()`
 - Vrací data célé třídy

`GetActivity(x = activity)`
 - Vrací aktivitu (spánek, chůze, běh)

`PrelozActivity(datas = jaká datas)`
 - Vrací výsledek převodu kódového označení na string

`PrelozDatum(datas = jaká datas)`
 - Vrací výsledek převodu času na českou normu
  
`GetMethodBetweenDates(datas = jaká datas, start = začátek čas, end = konec čas, method = metoda)`
 - Provede vloženou metodu na všech záznamech začínajících s časem start a končícívh s časem end

