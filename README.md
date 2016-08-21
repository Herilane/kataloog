#h1 Ärikataloog
#h2 Proovitöö.

#h3 Eeldused
Rakenduse paigaldamiseks vajalik tarkvara on Django.

Django==1.10

#h3 Installerimine

1. virtualenv
Soovituslik komponent tarkvara installeerimiseks: 
$ [sudo] pip install virtualenv

2. Lähtekoodi laadimine
Lae lähtekood oma töölauale:
$ cd /path/to/your/workspace
$ git clone git://github.com/Herilane/kataloog.git

Tekkinud kausta saab luua virtuaalkeskkonna käsuga:
virtualenv --python=python3.5 minu_keskkond

Django paigaldamiseks kasutada käsku:
pip install Django==1.10 

3. Andmebaasi käivitamine
Andmebaasiks on selle töö raames ette nähtud Sqlite3. Andmebaasi kasutamiseks käivitada järgnevad käsud:
$ python manage.py migrate

4. Andmebaasi testandmetega täitmine
Testandmed asuvad failis dummy.sql. Sisestada tuleb nad andmebaasi käsuga sqlite3 db.sqlite3 < dummy.sql.

5. Veebirakenduse jooksutamine lokaalselt:
Veebirakendus käivitada käsuga:
$ python manage.py runserver

Aadressil http://localhost:8000 leiab toimiva rakenduse.
