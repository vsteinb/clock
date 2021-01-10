# Am Terminal gibt es zunächst folgende Befehle. Diese Befehle sind kein „Spielzug“. #

|Befehl | Auswirkung |
|--|--|
|/init   | Startet das Gerät (Ohne /init gibt es die Antwort ```System not ready.```) |
|/s = 10 | Prüft, ob es sich um ein Phänomen mit Stufe 10 handelt. >, <, >=, <= gehen auch. |
|/type <...> | Prüft, um welches Phänomen es sich handelt. (RR für Raumriss, ZR für Zeitriss, ZA für Zeitanomalie) |
|/response <...> |      Prüft, ob ein bestimmtes Phänomen noch auf die Zeitmaschine reagiert. |
|/splits <...> |   Prüft, ob das Phänomen bereits alt genug ist, dass es sich vergrößert und vermehrt hat. |
|/splitn <...> |   Prüft, wie oft sich das Phänomen bereits vermehrt hat. |
|/restart|	Neustart der Patie. Geht nur 3x|
|/help   |  Zeigt alle möglichen Hilfebefehehle an (also /help1, /help2) |
|/help1  |   Zeigt die Startbefehle (alle Befehle, die mit / starten) |
|/help2  |   Zeigt alle Befehle zum beheben von Problemen an (alle Befehle, die mit // starten) |
|//analyze||
|//crystallize||
|//delete||
|//drag||
|//drop||
|//forward||
|//inject||
|//naturalize||
|//normalize||
|//return||
|//bdv||
|//mdbv||
|//mdv||

# Zeitrisse lösen #

- Linearriss: //return  →  //crystallize  →  //normalize

- Liniendeletion: //analyze  →  //drag  →  //drop  →  //naturalize

- Splinter: Warten bis Umwandlung erfolgt ist. Befehl //skip lässt Zeit verstreichen und hat keine Auswirkungen.

- Duplikator: //crystallize → //normalize → //return

- Looper: //analyze → //drag → //delete → //naturalize

- Timelagger: //analyze → //drag → //drop → normalize

- Timedelayer: //forward → //inject → //normalize

- Runner: //crystallize → //return → //normalize


# Gatter #

 - Mirror: Dieses Modul reflektiert jeden Befehl. Danach ist der Spiegel allerdings durchbrochen. Der Spiegel besitzt somit nur einen Input und einen Output. Ein Mirror macht am System beträchtliche Mengen an Schaden, was zur Folge hat, dass dieser Befehl für einige Zeit nicht mehr funktioniert (in der Hauptuhr für drei Züge).

 - Inverter: Der Inverter reagiert nur selektiv auf gewisse Befehle. Wird er von dieses passiert, wandelt er manche Befehle um.

	| input       | output       |
	|-------------|--------------|
	|//drag       |//drop        |
	|//drop       |//drag        |
	|//inject     |//crystallize |
	|//crystallize|//inject      |
	|//forward    |//return      |
	|//return		  |//forward     |

 - Aktivator/Desaktivator: Sie befinden sich auf einer Leitung und können aktiviert werden. Dann können alle Befehle passieren. Werden sie deaktiviert, so kann kein Befehl mehr passieren.

 - Switch: Sie besitzen zwei Outputs, von denen einer aktiv ist und einer inaktiv. Welche aktiv und welche inaktiv ist, kann entschieden werden.

 - Konverter: Konverter können gemein sein, da sie Zeitrisse unbehebbar machen können. Dies ist etwas, dass auch nur von einer Liniendeletion hervorgerufen werden kann. Ein Konverter reagiert nur auf einen bestimmten Befehl, den es in einen anderen umwandelt. Sie können entweder monodirektional sein, was besonders gravierend ist. Das heißt, sie wandeln zum Beispiel ein //drag in //return um, aber nicht umgekehrt. Bidirektionale Konverter funktionieren demnach in beide Richtungen.

 - Barriere: Eine Barriere fängt eine Anzahl Befehle in Höhe der Stufe ab, die ein Zeitriss für diese Barriere aufgewendet hat. Nach der Anzahl ist die Barriere zerstört.


# Ereignisse #
Es gibt einige Ereignisse, die während des Behebens auftreten können. Hier deshalb eine Liste davon.

## Outputs ##
Manche Zeitrisse reagieren auf die Befehle, was die Zeituhr registriert. Im Terminal werden diese Reaktionen übersetzt und tauchen deshalb dann direkt darin auf. Da alle Phänomene, die aktuell behoben werden durchgezählt werden, taucht dann im Terminal nach folgendem Schema auf:
#12: \<Output\>

Die Outputs der Zeitrisse generell sollten der Reihe nach in 0,3s bis 0,5s Intervallen erfolgen.

### Linearriss ###
Dieser muss als erstes entfernt werden. Er erhält netterweise automatisch immer die erste(n) Nummer(n). Linearrisse reagieren auf alle Befehle gleich, da ihre Manaquelle gigantisch ist.

 - Folgender Output taucht bei ihnen immer auf, solange sie nicht behoben sind:
```#1: Growth accelerated. Manainput stabilized. Increasing size for further division.```
 - Wenn sie behoben sind, kommt:
```#1: Growth has been corrupted. Stabilization failed.```

Linearrisse können wachsen und sich teilen. Ihre Stufe erhöht sich alle drei Befehle um 1. Jedes Mal, wenn sich die Stufe erhöht gibt es eine 25% Chance, dass der Linearriss zu einem Splinter wird. Nach jedem weiteren Befehl gibt es dann eine 10% Chance, dass der Splinter in die nächste Phase übergeht. **Splinter** werden immer gelb markiert. Entsteht die nächste Form spricht man von einem Supersplinter. Diese sind rot markiert und pulsieren. Metasplinter sind bedrohlich und haben eine 33% Chance sich zu mit jedem weiteren Befehl zu teilen.
Es entstehen nach dem Teilen immer wieder der ursprüngliche Linearriss und weitere Zeitrisse (aber keine weiteren Linearrisse und auch keine Liniendeletion).
Die Anzahl ist dabei zufällig. Mindestens ein zusätzlicher Zeitriss entsteht. Bis zu fünf weitere Zeitrisse können aber entstehen.
Die Wahrscheinlichkeit für einen weitere Zeitriss ist 45%
Für zwei 25%
Für drei 15%
Für vier 10%
Für fünf 5%
Sind Linearrisse erst zu einem Splinter geworden, sind sie unaufhaltsam. Darum sollten Linearrisse immer oberste Priorität haben.

### Liniendeletionen ###
sind ähnlich problematisch. Liniendeletionen werden immer schwarz markiert, wodurch sie kenntlich gemacht werden. Liniendeletionen können aber das Raum-Zeit-Gefüge unterwandern und korrumpieren. Dies hat zur Folge, dass sie auch andere Zeitrisse beeinflussen. Sie können andere Zeitrisse tarnen und decken. Dadurch wird die Hauptuhr getäuscht. Nach jedem Befehl besteht eine 5% Chance, dass eine Liniendeletion einen beliebigen Zeitriss (nicht Liniendeletionen oder Linearrisse deckt, indem diese ebenfalls schwarz angezeigt werden). Sie kann mit diesem Zeitrisse auch die Position wechseln. Dies ist dabei zufällig. Wurde diese Entscheidung für den gewählen Zeitriss gewählt, besteht die Möglichkeit nicht mehr.
Alle potenziellen Kandidaten für den Linearriss werden dann mit der nächsten freien Nummer und einem Fragezeichen gelistet. Also zum Beispiel mit #2? oder #4?, wenn es nur einen bzw. drei Linearrisse gibt. Die Outputs der Liniendeletionen und getarnten Zeitrisse werden dadurch unter der gleichen Bezeichnung aufgeführt.
Liniendeletionen antworten allerdings recht charakteristisch. Nach einem Befehl antworten sie typischerweise mit einem aus:

```python
['Target not found.', 'No event existing.', 'There is nothing.', 'We are wasting energy.',
'No.', 'Time is a state of mind.', 'Reach out.', 'Unidentified object found.', 'Restarting...',
'Programm not ready.', 'Initializing...', 'Please restart.', 'Converting splinter.', 'What am I?']
```
Dabei ist irrelevant, ob der Befehl richtig war oder nicht.

### Splinter ###
Wenn Splinter einen Befehl abbekommen, so werden sie immer mit einer nicht zu entziffernden Antwort kommen. Diese sind randomized in Länge (3 bis 50 Zeichen) und Text.

### Duplikator ###
Outputs vom Duplikator werden immer doppelt kommen. Es muss nicht immer der Gleiche doppelt erscheinen. Outputs des

 - Duplikators bei einem **falschen Treffer** sind zum Beispiel:
```python
['Mana has been detected', 'More mana is needed', 'Gathering more mana']
```

 - Bei einem **Treffer**:
```python
['Input has been blocked', 'Currently no power input', 'A critical error occured']
```

 - Bei **Zerstörung**:
 ```python
['Maintaining manaflow failed', 'Stabilization failed', 'Dew point too high']
```

### Looper ###
Ein Looper kann bei Outputs sehr lästig werden. Looper **wiederholen alle ihre bisher gegebenen Outputs und hängen den neuen an**.

- Bei **falschem Treffer**:
```python
['Mana in a spiral', 'Circulating more energy', 'Power ramped up']
```

 - Bei **Treffer**:
 ```python
['Dizzyness', 'Eastward it goes', 'Getting down']
```

 - Bei **Zerstörung**:
 ```python
['Mana falling down', 'Leaving the circle', 'Outer space']
```

### Timelagger ###
Timelagger sind etwas fies, da sie die **letzte Antwort des letztantwortenden Zeitrisses einfach kopieren**. Ihre Antwort kommt allerdings immer etwa drei Sekunden später, als die vom letzten Zeitriss.

 - Bei **Zerstörung** kommt keine Antwort.
 - Bei einem **Treffer** wird noch ein weiterer Output angehängt:
 ```python
 ['it says', 'I guess', 'maybe', 'it should not be', 'I assume']
 ```

### Timedelayer ###
Timedelayer sind relativ unkompliziert und antworten nur sehr kurz. Ihre **Antwort wird allerdings immer um eine Runde verzögert**. Das heißt, anfangs antworten sie einmal nicht und danach hängen sie immer einen Befehl hinterher.

 - Bei einem **falschen Treffer**:
```python
['No', 'Wrong', 'Incorrect', 'Yesno', 'Do not', 'Is not']
```

 - Bei einem **Treffer**:
 ```python
['Yes', 'Right', 'Hurt', 'Wow', 'Betrayal', 'Unfair']
```

 - Bei **Zerstörung**:
 ```python
['Murderer', 'Killer', 'No time for that', 'Out of existence']
```

### Runner ###
Runner haben die Eigenschaft generell etwas schwer verständlich zu sein. Ihre Outputs sind nicht so aufschlussreich, da sie sich mit anderen Outputs decken. Nur manche sind spezifisch für Runner. Der Runner ist jedoch **immer der erste Output**, der ankommt.

 - Bei **falschem Treffer**:
```python
['Yes', 'More power', 'POW', 'Module established', 'More mana is needed']
```

 - Bei **Treffer**:
 ```python
['Mana has been blocked', 'A critical error occured', 'Target not found', 'Run']
```

 - Bei **Zerstörung**:
 ```python
['Stormy', 'Awaiting input', 'Stopped running', 'I stopped working']
```


## Zeitanomalien ##

Von diesen gibt es fünf Stück. Zeitanomalien benötigen viel Feingefühl, wenn sie zusammen mit Zeitrissen auftreten. Das Gute: Zeitanomalien steigen bei einem fehlerhaften Befehl nicht um eine Stufe, wenn nicht anders beschrieben.

Zeitanomalien stellen andere Gatter zur Verfügung. Diese Gatter sind generell möglich:

### Spezifische Gatter ###

 - Manadegenerator:
Läuft durch dieses Gatter ein //inject durch, so wird es ausgelöscht. Das Gatter löscht sich dabei allerdings auch aus. Alle anderen Befehle passieren normal.

 - Manabombe:
Wird dieses Gatter passiert, so wird es zerstört, es gibt eine starke Explosion und ein beliebiger Zeitriss wird zu einem Splinter. Es wird also wohl oder übel ein weiterer Linearriss entstehen. Die Manabombe zerstört allerdings die zugehörige Zeitanomalie.

- Support-Gatter:
siehe Eraser

- Teleportgatter:
siehe Traceback


### Consumer ###
Consumer werden mit dem Befehl ```//inject``` zu Fall gebracht. Dabei sinkt ihre Stufe jedes Mal um 1. Consumer sollten zügig zu Fall gebracht werden. Sie haben nach jedem Zug eine 33% Chance, dass ihre Stufe um 1 steigt. Erreichen sie Stufe 5, so fallen Sie in sich zusammen, aber erschaffen dabei einen Linearriss.

### Eraser ###
Eraser sind stärker als Consumer. Sie benötigen den Befehl ```//crystallize```. Mit jedem Mal wird ihre Stufe dabei um 1 gesenkt.
Eraser können ein Support-Gatter erschaffen. Wird dieses von einem //inject oder //drop  durchlaufen, so wird der Befehl abgefangen und ein Consumer der Stufe 1 wird geschaffen. Die Support-Gatter können allerdings durch den Befehl //drag entfernt werden.

### Blurr ###
Ein Blurr ist eine Anomalie, die sehr störend sein kann und bei langem Bestehen zur Selbsterhaltung neigt.
Ein Blurr hat pro Stufe nach jedem Zug eine 1% Chance, dass er irgendein anderes Phänomen (also ZR, RR oder ZA) mit einem Manasturm tarnt. Das heißt, dass das entsprechende Phänomen noch da ist, aber man im Interface wird das Ziel von einer Art Wolke umgeben („geblurrt“). Dies kann auch mit Gattern passieren.
Ein Blurr verliert sein Stärke durch ```//drag```. Dieser Befehl senkt die Stufe des Blurrs um je 1.
Jedes Mal, wenn der Befehl //inject //drop oder //crystallize allerdings zu ihnen gelangt, steigt ihre Stufe um 1.

### Short ###
Sie sind immer fest mit einem anderen beliebigen Zeitriss verbunden. Sobald entweder der Short oder der zugehörige Zeitriss entfernt wird, ist auch der andere weg.
Beide arbeiten dabei füreinander. Der Short kann durch den Befehl ```//naturalize``` behoben werden. Jeder Treffer reduziert die Stufe des Shorts um 1. Der Zeitriss nimmt dabei diesen Befehl nie als fehlerhaft war. Seine Stufe steigt also nicht, auch wenn der Befehlt in der Situation ankommt und falsch wäre.
Der Short hat die Fähigkeit, dass er zu 5% eine Stufe eines beliebigen anderen Phänomens klaut und dafür eine Stufe stärker wird. Erreicht ein Short Stufe 10, so erschafft er einen Splinter und eine Raumfissur, verschwindet dafür aber selbst.

### Traceback ###
Diese Zeitanomalie ist äußerst gefährlich und tritt **immer zusammen mit einem Wurmloch** auf. Tracebacks können ein Teleportgatter erschaffen. Wird dieses von einem Befehl passiert, wird es zum korrespondieren Gatter befördert und läuft dort weiter. Nach der Benutzung verschwindet das Gatter und wird neu platziert. Pro Stufe kann der Traceback eines dieser Teleportgatter platzieren. Es kann dafür gar keine anderen Gatter erschaffen. Mit ```//crystallize``` kann der Traceback sofort ausgeschaltet werden. Jedoch muss auch das Wurmloch diesen Befehl im gleichen Zug erhalten. Nur wenn das der Fall ist löschen sich beide aus. Sonst bleiben sie beide bestehen.

## Raumrisse ##

Wo gerade schon die ersten Raumrisse thematisiert wurden, ist hier die Anleitung, wie man diese behebt.

Raumrisse müssen mit bestimmten Werkzeugen behoben werden. Raumrisse erschaffen andere Arten von Gattern.


### spezifische Gatter ###

- Sensor-Gatter:
siehe Raumfisssur

 - Tracing-Gatter:
 siehe Wurmloch


### Raumfissur ###
Sie sind alleinstehende Phänomene und müssen mit dem Befehl ```//mdv``` entfernt werden. Damit wird ein monodirektionales Manaventil geschaffen, welches die Raumfissur direkt entfernt.
Raumfissuren können jedoch Sensor-Gatter erschaffen. Diese absorbieren jeden Befehl und ihre Stufe steigt um 1. Die Gatter können nur mit dem Befehl //delete gelöscht werden. Der Befehl //delete kommt aber in dem Zug nicht durch.

### Wurmloch ###
Dieser Raumriss tritt immer zusammen mit einem Traceback auf und muss deshalb mit ```//crystallize``` behoben werden (s. Traceback). Sie können nur maximal Stufe 3 sein, wobei man bei Wurmlöchern eher Kategorie sagt. Der Befehl ```//bdv``` (bidirektionales Manaventil) kann verwendet werden, um zumindest die Kategorie des Wurmlochs um 1 zu senken. Unter 1 kann sie allerdings nicht sinken.

 - Kat. 1 Wurmloch zu 20% kann nach einem Zug ein Gatter mit einem anderen tauschen. Außerdem können sie zu 20% ebenfalls einfach die Position eines Gatters ändern.
 - Kat.2 hat ebenfalls die Möglichkeit zu 5% pro Zug ein Tracing-Gatter zu erschaffen. Diese zählen, wie viele Befehle bereits durch sie gelaufen sind. Alle fünf Befehle erschaffen diese Gatter ein Kapselphänomen.
  - Kat.3 Wurmlöcher sind dramatische Gebilde, die die oben genannten Fähigkeiten und Eigenschaften auch haben, jedoch zusätzlich bei Anwesenheit von Tracing-Gattern pro Gatter eine 1% Chance haben ein Kapselphänomen (wenn anwesend) in ein Raumloch zu verwandeln.

### Raumloch ###
Ein Raumloch ist das dramatischste Phänomen von allen. Hier existiert der Raum nicht mehr. Das Raumloch legt sich auf oder zwischen Gatter und kann nicht behoben werden. Es ist unpassierbar und bleibt permanent an seiner Position.

### Kapselphänomen ###
Diese Raumrisse sind Quarantäne-Objekte, die von der Raumuhr isoliert wurden, um größere Schäden zu verhindern. Sie besitzen eine **Immunität gegen alle Befehle**.
**Alle 5 Züge** wird ihre **Immunität** allerdings **verschwinden** und dann kann man Kapselphänomene  mit dem Befehl ```//bdv``` beheben. Es besteht eine 50% Chance, dass dies funktioniert. Wenn nicht, erschafft das Kapselphänomen ein Raumloch. Deshalb ist manchmal ganz sinnvoll Kapselphänomene ganz in Ruhe zu lassen.
Kapselphänomene haben **bis zu fünf Stufen**. Die Stufe entscheidet, wie groß ihre Toleranz gegenüber //bdv ist.

|Stufe | //bdv klappt zu... |
|------|-----|
| 1    | 50% |
| 2    | 40% |
| 3		 | 30% |
| 4 	 | 20% |
| 5		 | 10% |

### Bizarrgebiet ###
Bizarrgebiet sind besonders kurios, da sie Materie verschwinden und auftauchen lassen können. Sie können mit dem Befehl ```//mdbv``` (monodirektionales Breitbandventil) oder ```//mdv``` (2x nötig) behoben werden. Sie besitzen keine Stufen. Bizarrgebiete haben die Fähigkeit, dass sie nach jedem Zug entweder einen Befehl der Raum-Zeit-Uhr blockieren können (für einen Zug zufällig) oder alternativ ein Gatter für einen Zug verschwinden lassen oder hinzufügen können (auch nur für einen Zug).

# Generelles zum Verlauf #

Gewonnen ist die Partie, wenn alle Phänomene behoben sind. Außnahmen sind Raumlöcher und Kapselphänomene.

Es gibt einen Counter, der mitzählt, wie viele Züge stattgefunden haben. Züge sind dabei nur die Befehle zum Beheben von ZR, ZA oder RR.
Mit ```/restart``` kann die Partie wiederholt werden. Dies ist nur zwei Mal möglich. Danach sind Hopfen und Malz verloren.
Der Stand der Partie kann „gespeichert“ werden.
Es gibt eine maximale Anzahl an Zügen.
