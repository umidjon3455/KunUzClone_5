# KunUzClone_5

Django yordamida yaratilgan yangiliklar sayti. Saytda yangiliklar kategoriyalar bo‘yicha ko‘rsatiladi va Django Admin orqali boshqariladi.

## Texnologiyalar

- Python 3.11
- Django 5.2 LTS
- SQLite
- Pillow
- python-dotenv
- HTML, CSS, Bootstrap va JavaScript

## Loyiha tuzilishi

```text
KunUzClone_5/
├── app/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── media/
├── static/
├── templates/
├── .env.example
├── .gitignore
├── manage.py
└── requirements.txt
```

## O‘rnatish (Windows / PowerShell)

Python 3.11 o‘rnatilgan bo‘lishi kerak.

1. Repozitoriyani yuklab oling:

```powershell
git clone https://github.com/umidjon3455/KunUzClone_5.git
cd KunUzClone_5
```

2. Virtual muhit yarating va faollashtiring:

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Kutubxonalarni o‘rnating:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Muhit faylini yarating:

```powershell
Copy-Item .env.example .env
```

5. Maxfiy kalit yarating:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Chiqqan qiymatni `.env` faylidagi `DJANGO_SECRET_KEY` qatoriga joylashtiring. Lokal ishga tushirish uchun `DJANGO_DEBUG=True` qoldirilishi mumkin. `.env` faylini hech qachon GitHub'ga yubormang.

6. Ma’lumotlar bazasini tayyorlang:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

7. Serverni ishga tushiring:

```powershell
python manage.py runserver
```

Sayt: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

## Tekshiruvlar

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

## Eslatma

- `.env`, virtual muhit, SQLite bazasi va Python cache fayllari Git'ga kiritilmaydi.
- Yangilik rasmlari `media/` ichida saqlanadi.
- Hostingga joylashda `DJANGO_DEBUG=False` va `DJANGO_ALLOWED_HOSTS` qiymatlarini hosting domeniga moslang.
