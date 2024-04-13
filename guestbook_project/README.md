DESCRIERE

Guestbook este o aplicație web simplă care îți permite să creezi și să gestionezi un registru digital de oaspeți. 
Cu Guestbook, utilizatorii pot să adauge noi înregistrări pentru fiecare vizită, să vizualizeze înregistrările existente
și să interacționeze cu comunitatea prin lăsarea de mesaje și feedback.

Prin intermediul acestui instrument, organizatorii de evenimente sau proprietarii de site-uri web pot să ofere o 
experiență interactivă și personalizată oaspeților lor, să primească feedback în timp real și să păstreze un istoric al
interacțiunilor.

INSTRUCTIUNI DE INSTALARE

1. Clonează sau descarcă proiectul de pe repository-ul GitHub.

2. Asigură-te că ai Python și Django instalate pe sistemul tău. Dacă nu le ai deja, le poți instala folosind Python.
org și Django.

3. În folderul proiectului creează un virtual environment următoarele comenzi folosind 
   terminalul:

> python -m venv nume_mediu_virtual

4. Activează virtual environment creat cu comanda:

MacOS:

> source nume_mediu_virtual/bin/activate

Windows:

> nume_mediu_virtual\Scripts\activate

5. Instalează dependențele proiectului folosind comanda:

> pip install -r requirements.txt

6. Aplică migrările pentru a inițializa baza de date:

> python manage.py migrate

7. Creează un SuperUser pentru a avea acces la interfața de administrare și pentru a adăuga și gestiona intrările:

> python manage.py createsuperuser

odată rulată comanda de mai sus trebuie să urmezi pașii care apar în terminal.

> username - yourname
> 
> email - your@email.com
> 
> password - ******** (ATENTIE!!! caracterele scrise nu apar)

8. Rulează serverul de dezvoltare folosind:

> python manage.py runserver

9. Accesează aplicația într-un browser(Chrome, Safari, Opera) folosind adresa:

> http://localhost:8000

sau

> http://127.0.0.1:8000
