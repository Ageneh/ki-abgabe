# **8-Puzzle-Suchproblem**


## Zustandstaum S


<br><br>

## Initialzustand SI

Ein Knoten, mit den Daten 
[2, 8, 3]
[1, 6, 4]
[7, 0, 5]. 
Repräsentiert die Anordnung der Felder Reihe für Reihe.
<br><br>

## Zielbeschreibung G

Ein Knoten, mit den Daten 
[1, 2, 3]
[8, 0, 4]
[7, 6, 5]. 
Repräsentiert die Anordnung der Felder Reihe für Reihe.
<br><br>

## Operatoren o

Daher, dass immer ein Feld leer bleibt, wird dieses als Referenfeld verwendet, um die direkten Nachbarfelder bewegen zu können. Als direkte Nachbarfelder zäheln Felder die eine **Manhattan-Distanz von 1** zum leeren Feld besitzen und damit direkt an dem leeren Feld anliegen. Dazu zählen Felder die links, rechts, ober oder unterhalb des leeren Feldes sind. Daraus ergeben sich auch die vier Möglichkeiten ein Feld verschieben zu können.

> **Beispiel:**<br>
> Wenn wir den Initalzustand SI betrachten, so fällt auf, dass das Referenzfeld - welches mit **`0`** gekennzeichnet wird - drei direkte Nachbarsknoten besitzt, welche beim expandieren von Si entstehen. Diese sind:
> * [2, 8, 3] 
>   [1, 0, 4] -> nach oben
>   [7, 6, 5] <br><br>
> * [2, 8, 3] 
>   [1, 6, 4] -> nach links
>   [0, 7, 5] <br><br>
> * [2, 8, 3] 
>   [1, 6, 4] -> nach rechts
>   [7, 5, 0] 

<br>

## Pfadkostenfunktion g

**Kosten pro Schritt:** 1  
**Gesamtkosten:** 6  
**Pfad / Schritte:**  

1. [ [2, 8, 3], [1, 6, 4], [7, 0, 5] ] 
2. [ [2, 8, 3], [1, 0, 4], [7, 6, 5] ]
3. [ [2, 0, 3], [1, 8, 4], [7, 6, 5] ]
4. [ [0, 2, 3], [1, 8, 4], [7, 6, 5] ]
5. [ [1, 2, 3], [0, 8, 4], [7, 6, 5] ]
6. [ [1, 2, 3], [8, 0, 4], [7, 6, 5] ]