
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files for WhiteNoise to serve
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate

# Automatically create the superuser (Custom command)
python manage.py setup_admin