#!/bin/bash
export DJANGO_SETTINGS_MODULE=settings
rm liquidityspot.db
./manage.py syncdb
