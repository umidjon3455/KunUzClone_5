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

4. Migratsiyalarni bajaring va serverni ishga tushiring:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Saytni `http://127.0.0.1:8000/` manzilida oching.

## Admin panel

Administrator yaratish:

```bash
python manage.py createsuperuser
```

Admin panel: `http://127.0.0.1:8000/admin/`

## Muallif

**Umidjon Abdullayev** — [GitHub](https://github.com/umidjon3455)
