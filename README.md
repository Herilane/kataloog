# H1 Ärikataloog
# H2 Proovitöö.

# H3 Eeldused
Rakenduse paigaldamiseks vajalik tarkvara on Django.

Django==1.10

# H3 Installerimine

* virtualenv
Soovituslik komponent tarkvara installeerimiseks: 
$ [sudo] pip install virtualenv

* # H4 Lähtekoodi laadimine
Lae lähtekood oma töölauale:
$ cd /path/to/your/workspace
$ git clone git://github.com/Herilane/kataloog.git

Tekkinud kausta saab luua virtuaalkeskkonna käsuga:
virtualenv --python=python3.5 minu_keskkond

Django paigaldamiseks kasutada käsku:
pip install Django==1.10 

* # H4 Andmebaasi käivitamine
Andmebaasiks on selle töö raames ette nähtud Sqlite3. Andmebaasi kasutamiseks käivitada järgnevad käsud:
$ python manage.py migrate

* # H4 Andmebaasi testandmetega täitmine
Testandmed asuvad failis dummy.sql. Sisestada tuleb nad andmebaasi käsuga sqlite3 db.sqlite3 < dummy.sql.

* # H4 Veebirakenduse jooksutamine lokaalselt:
Veebirakendus käivitada käsuga:
$ python manage.py runserver

Aadressil http://localhost:8000 leiab toimiva rakenduse.
