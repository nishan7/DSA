#!/bin/bash
cd /home/nishan/project/DSA/
export FLASK_ENV=development
pkill -9 flask
pkill -9 python
python3 app.py