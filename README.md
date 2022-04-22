# PrevWorks

## Project Local Setup 

First make sure you have python3 installed and give further commands to install the application

Clone the project locally and and run below commands to setup local python env , install required libraries and then run the flask app

```
pip install virtualenv

virtualenv env

source env/bin/activate

cd PreWorks/backend

pip install -r flaskr/requirements.txt

export FLASK_APP=flaskr

flask run
```


## Database Local Setup 

setup mysql files and run those files to create tables in the database

```commandline

export ENVIRONMENT=LOCAL
export DATABASE_URL=postgres://postresql@localhost:5432/prevworks

```


## Postgresql Migration 
Project is currently being migrated to postgresql)

## Heroku Deployment

https://prevworks.herokuapp.com/
