#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run the development server
python manage.py runserver
