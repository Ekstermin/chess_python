# REST Chess solver

Projekt polega na utworzeniu prostej aplikacji REST wspomagającej grę w szachy.

## Informacje wstępne

* Python 3.6 - 3.9
* Black (formatowanie)
* Flake8 (linter)
* Pytest (testy)
* Flask 1.0+
* SQLAlchemy (jeśli potrzeba) - nie użyte da się bez tego i unikniemy błędów serwera ponieważ nie będzie połączenia do bazy danych

## Wymagane moduły

Moduły potrzebne do uruchomienia aplikacji
```python
pip install pytest 
pip install flask
```

## Jak uruchomić aplikacje

Program napisany i testowany pod Windows 11.
Program w wersji deweloperskiej.

app.py i chess.py zastępujemy ścieżką do tych plików w sytuacji gdy uruchamiamy pythona z innej lokalizacji niż folder zawierający aplikację.
Uruchamiamy po przez komendę:

```python
python.exe app.py 
```
Uruchomienie testów po przez następujące polecenia

```python
python.exe -m pytest app.py -vvv
python.exe -m pytest chess.py -vvv
```
## Sposób używania api

Adres domowy root zawiera informacje jak używać api
http://127.0.0.1:5000/

List of examples website addresses:
After run app you can check avaibled moves for chessboard [a-h][1-8] position.
App only chek moves for white pawns.
Avaibled chess figure are:
1. king
2. queen
3. rooks
4. bishop
5. knights
6. pawns
To check avaible moves, you need put your figure and position to url like that:
http://127.0.0.1:5000/api/v1/{figure}/{field}

For example list avaiblet move for King from h2 field chek from url:
<a href="http://127.0.0.1:5000/api/v1/king/h2">http://127.0.0.1:5000/api/v1/king/h2


To check validate move from position to position, you need put your figure, curently position, destination position to url like that:
http://127.0.0.1:5000/api/v1/{figure}/{field}/{dest-field}

For example validate move to destination field use url like that:
<a href="http://127.0.0.1:5000/api/v1/king/h2/g3">http://127.0.0.1:5000/api/v1/king/h2/g3</a>