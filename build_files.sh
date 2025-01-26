#!/bin/bash
# Build script for Vercel
pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
python3 manage.py collectstatic --noinput
mkdir -p media
chmod -R 755 media
