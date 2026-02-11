Campaign Tracker Backend

This is the backend service for the Campaign Tracker application built using Django REST Framework and PostgreSQL (Supabase).
It provides APIs for managing marketing campaigns, analytics reports, and currency conversion.

///// Live API

Base URL:

https://campaign-tracker-backend-production.up.railway.app


Example:

/api/campaigns/

//////Tech Stack

Python 3

Django & Django REST Framework

PostgreSQL (Supabase)

Railway (Deployment)

Gunicorn

CORS Headers

///// Features

Create / Update / Delete campaigns

Campaign listing API

Monthly trends report

Budget by platform report

Status summary

Currency conversion using third-party API

Production deployment on Railway

/////// Environment Variables

Create .env file locally:

DB_NAME=postgres
DB_USER=postgres.xxxxx
DB_PASSWORD=yourpassword
DB_HOST=aws-1-ap-south-1.pooler.supabase.com
DB_PORT=6543

SECRET_KEY=your-secret-key
DEBUG=True

///// Run Locally
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver


API runs at:

http://127.0.0.1:8000/api/

//////Deployment

Backend is deployed on Railway using:

Build Command:

pip install -r requirements.txt

Start Command:

gunicorn campaign_tracker.wsgi:application --bind 0.0.0.0:$PORT
