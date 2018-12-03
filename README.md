# 8-Puzzle-Suchproblem


## Zustandsraum S
Eine mögliche Anordnung des 8-Puzzle wird als Knoten repräsentiert. Die Knoten-Definition ist in 'node.py' in der Klasse Node zu finden.
Ein Knoten besitzt folgende Eigenschaften/Variablen:
- data: Beinhaltet eine 2-dimensionale Liste, mit den zugehörigen Zahlen für jede Reihe des 3x3-Puzzles. Speichert die tatsächliche Anordnung des Puzzles.
- parent: Ist eine Referenz auf einen vorherigen Knoten, um bei den Lösungspfad in zwei Richtungen lesen/traversieren kann und weil man ja auch in der Realität einen Zug rückgängig machen kann.
- depth: speichert die Tiefe eines Knoten.
- children: Ist ein Dictionary und speichert die Folgeknoten, je nach der Bewegungsrichtung, des leeren Feldes. Sollte zB. Das leere Feld nach links bewegt worden sein, dann ist die neue Anordnung unter dem Schlüssel "links" zu finden. Dieser Schlüsselwert wird dann dem expandierten Knoten mitgegeben in der _move_ Variable.

Neben diesen können auch noch zwei Marker root und goal gesetzt werden. Diese erlauben es, die Knoten als Wurzel oder Ziel zu markieren. Sollten diese nicht gesetzt sein so sind beide 'False'.


## Initialzustand Si

Ein Knoten _root_, mit den Daten [ 
[2, 8, 3],
[1, 6, 4],
[7, 0, 5]
].

Ein Knoten _goal_, mit den Daten [
[1, 2, 3],
[8, 0, 4],
[7, 6, 5]
].


## Zielbeschreibung G
Es wird ein Pfad ausgegeben, welcher den Lösungsweg, vom Initialknoten bis hin zum Zielknoten, beinhaltet.


## Operatoren o

Daher, dass immer ein Feld leer bleibt, wird dieses als Referenfeld verwendet, um die direkten Nachbarfelder bewegen zu können. Als direkte Nachbarfelder zählen Felder die eine **Manhattan-Distanz von 1** zum leeren Feld besitzen und damit direkt an dem leeren Feld anliegen. Dazu zählen Felder die links, rechts, ober- oder unterhalb des leeren Feldes sind. Daraus ergeben sich auch die vier Möglichkeiten ein Feld verschieben zu können.

Beispiel:
Wenn wir den Initalzustand Si betrachten, so fällt auf, dass das Referenzfeld - welches mit "0" gekennzeichnet wird - drei direkte Nachbarsknoten besitzt, welche beim expandieren von Si entstehen.
Diese sind:
- [ [2, 8, 3], [1, 0, 4], [7, 6, 5] ] -> nach oben
- [ [2, 8, 3], [1, 6, 4], [0, 7, 5] ] -> nach links
- [ [2, 8, 3], [1, 6, 4], [7, 5, 0] ] -> nach rechts


## Pfadkostenfunktion g

Kosten pro Schritt: 1
Gesamtkosten: 6
Schritte: 6
Pfad:
1. [ [2, 8, 3], [1, 6, 4], [7, 0, 5] ]  == _root_
2. [ [2, 8, 3], [1, 0, 4], [7, 6, 5] ]
3. [ [2, 0, 3], [1, 8, 4], [7, 6, 5] ]
4. [ [0, 2, 3], [1, 8, 4], [7, 6, 5] ]
5. [ [1, 2, 3], [0, 8, 4], [7, 6, 5] ]
6. [ [1, 2, 3], [8, 0, 4], [7, 6, 5] ] == _goal_



---
## *by ### deschadx and hearegax; [git](https://github.com/Ageneh/ki)*