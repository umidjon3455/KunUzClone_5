# Kun.uz Clone (Django)

**Kun.uz Clone** — Django yordamida yaratilgan yangiliklar sayti. Loyiha Kun.uz yangiliklar portalining dizayni va funksiyalaridan ilhomlangan.

## Imkoniyatlar

- Yangiliklar ro'yxati va batafsil sahifalari
- Rasmli yangiliklar
- Kategoriyalar bo'yicha saralash
- Ommabop yangiliklar va bosh sahifa slideri
- Django Admin orqali yangiliklarni boshqarish
- Responsive interfeys

## Texnologiyalar

- Python 3.11+
- Django 5.2
- SQLite
- Pillow
- python-dotenv
- HTML, CSS va Bootstrap

## O'rnatish

1. Repozitoriyani yuklab oling:

   ```bash
   git clone https://github.com/umidjon3455/KunUzClone_5.git
   cd KunUzClone_5
   ```

2. Virtual muhit yarating va faollashtiring:

   **Windows (PowerShell):**
   ```powershell
   py -3.11 -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   **Linux/macOS:**
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```

3. Kutubxonalarni o'rnating:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. `.env.example` faylidan nusxa olib, nusxasini `.env` deb nomlang. `DJANGO_SECRET_KEY` qiymatini yangi, maxfiy kalitga almashtiring. `DJANGO_DEBUG=True` faqat mahalliy ishlab chiqish uchun.

   **PowerShell:**
   ```powershell
   Copy-Item .env.example .env
   ```

5. Migratsiyalarni bajaring va serverni ishga tushiring:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

6. Saytni `http://127.0.0.1:8000/` manzilida oching.

## Admin panel

Administrator yaratish:

```bash
python manage.py createsuperuser
```

Admin panel: `http://127.0.0.1:8000/admin/`

## Xavfsizlik eslatmasi

- Haqiqiy `.env` faylini GitHub'ga yuklamang.
- Agar avvalgi `SECRET_KEY` ommaviy repozitoriyga yuborilgan bo'lsa, uni bekor qilib, yangisini yarating.
- Production muhitida `DJANGO_DEBUG=False` va `DJANGO_ALLOWED_HOSTS` qiymatlarini hosting domeningizga moslang.

## Muallif

**Umidjon Abdullayev** — [GitHub](https://github.com/umidjon3455)
