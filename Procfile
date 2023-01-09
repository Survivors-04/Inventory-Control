web: python manage.py collectstatic --no-input \
    && python manage.py migrate \
    && gunicorn _inventory_control.wsgi --log-level debug