# Deployment Guide — tva_church on Namecheap Shared Hosting (cPanel + Phusion Passenger)

This project is a Django 6.0 app (`gogap_web`) configured to run on Namecheap shared
hosting via **cPanel** and **Phusion Passenger** (`passenger_wsgi.py`).

## Prerequisites

- Namecheap shared hosting plan with cPanel (supports Python + Phusion Passenger).
- cPanel's **Setup Python App** / Passenger enabled and a Python version ≥ 3.10.
- Domain: `tva.ng` / `www.tva.ng` (adjust `.env` if different).

## 1. Configure your `.env` file (do this before uploading)

Copy your values into the real `.env` (already created for you; it is gitignored):

```ini
DEBUG=False
SECRET_KEY=<your-generated-secret-key>          # already set to a random key
ALLOWED_HOSTS=tva.ng,www.tva.ng
CSRF_TRUSTED_ORIGINS=https://tva.ng,https://www.tva.ng

# SSL — keep FALSE until your certificate is working, then flip to True
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False

# cPanel MySQL
DB_NAME=cpaneluser_tva_church
DB_USER=cpaneluser_tva_user
DB_PASSWORD=<your-db-password>
DB_HOST=localhost
DB_PORT=3306
```

**Important:** replace the `DB_*` values with the real database name/user/password you
create in step 2. The `SECRET_KEY` is already populated; regenerate it if you prefer:

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

## 2. Create the database in cPanel

1. cPanel → **MySQL® Databases**.
2. Create a database (e.g. `cpaneluser_tva_church`).
3. Create a MySQL user (e.g. `cpaneluser_tva_user`) with a strong password.
4. Add the user to the database with **ALL PRIVILEGES**.
5. Put those exact values in `.env`.

## 3. Prepare locally before upload

Run these in `tva_church/` (using your local venv):

```bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py setup_admin        # or: python manage.py createsuperuser
```

The `collectstatic` step outputs to `staticfiles/` which is served by WhiteNoise.
Upload `staticfiles/` and `media/` as-is (they must exist on the server).

## 4. Upload to cPanel

1. Upload the project so the root is at e.g. `~/tva.ng` (the folder where `manage.py`,
   `passenger_wsgi.py`, `.env` live).
2. **Do not upload**: `.venv/`, `db.sqlite3`, `.git/`, `__pycache__/`.
   Do **DO upload**: `.env`, `staticfiles/`, `media/`.

## 5. Configure the Python app (Passenger) in cPanel

1. cPanel → **Setup Python App** (or *Python App* / *Passenger*).
2. Create a new app:
   - **Application root:** the directory that contains `passenger_wsgi.py`
     (e.g. `/home/USER/tva.ng`).
   - **Application URL:** `tva.ng` (and add `www.tva.ng`).
   - **Application startup file:** `passenger_wsgi.py`.
   - **Application Entry point:** `application`.
   - Choose a Python version (≥ 3.10).
3. cPanel creates a virtual environment; install dependencies into it:
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```
4. Ensure `staticfiles/` and `media/` are writable / exist, and that the Passenger
   app directory is reachable at the site root.

> If you use the alternate file layout, update `passenger_wsgi.py`'s paths accordingly.
> The `.env` file must sit in the same directory as `passenger_wsgi.py` (the app root).

## 6. Point your domain

- In cPanel → **Domains**, ensure the document root points to the Passenger app
  (or the Passenger URL maps to `tva.ng`).
- Namecheap DNS: A/AAAA records for `tva.ng` and `www.tva.ng` must point to your
  hosting server.

## 7. After SSL is installed (very important)

Once the SSL certificate is active (Namecheap/cPanel → **SSL/TLS Status** shows a valid
cert and HTTPS loads), edit `.env` and flip these to `True`:

```ini
SECURE_SSL_REDIRECT=True       # force all traffic to HTTPS
SESSION_COOKIE_SECURE=True     # only send session cookie over HTTPS
CSRF_COOKIE_SECURE=True        # only send CSRF cookie over HTTPS
```

Then restart the Python app from cPanel. Everything above is already wired in
`settings.py` (via `SECURE_PROXY_SSL_HEADER` and env-driven switches), so no code
changes are needed.

## Troubleshooting

- **500 error / app not loading:** check the Passenger error log in cPanel; verify
  `.env` has the correct `ALLOWED_HOSTS` and DB credentials, and that the venv has all
  `requirements.txt` packages installed.
- **Static files missing:** confirm `python manage.py collectstatic --noinput` was run
  and `staticfiles/` exists in the app root (WhiteNoise serves it).
- **MySQL connection issues:** confirm the user was granted privileges on the database,
  `DB_HOST` is `localhost`, and port `3306`.
