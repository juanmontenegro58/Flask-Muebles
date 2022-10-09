#!/bin/sh

if [ -f "mi_env/script/activate" ]
then
    echo virtual env already created
    source mi_env/script/activate
else
    virtualenv venv --python=python3.10.0
fi

source mi_env/script

# Just install dependencies by default to pick up any changes
pip3 install -r requirements.txt

#
# run the data server
#
export FLASK_APP=main.py
export FLASK_ENV=development
export FLASK_DEBUG=1

echo 'FLASK_APP: '$FLASK_APP


flask run

# Windows

cd /mi_env/script/activate

set FLASK_APP=main.py
set FLASK_DEBUG=1
set FLASK_ENV=development


flask run