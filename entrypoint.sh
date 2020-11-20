#!/bin/bash
ls /home/jobpost
pip3 install -r /home/jobpost/requirements.txt
python3 /home/jobpost/manage.py migrate
python3 /home/jobpost/manage.py runserver