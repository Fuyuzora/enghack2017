#!/bin/bash
export PYTHONPATH=`pwd`
echo $PYTHONPATH
export FLASK_APP=negativity_index/app.py
flask run

