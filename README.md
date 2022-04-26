# PrevWorks

## Project Local Install

First make sure you have python3 installed and give further commands to install the application

Clone the project locally and run below commands to setup local python env , install required libraries and then run the flask app

```
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```


## Database Local Setup 

- install postgresql
- create a database prevworks  
- run create_table.sql and create all required tables
- run below commands for configuring db env

```commandline
export ENVIRONMENT=LOCAL
export DATABASE_URL=postgresql://postgres@localhost:5432/prevworks
```
##  Local Project Run 

```
cd PrevWorks
export FLASK_APP=flaskr
flask run
```

## Heroku Deployment

https://prevworks.herokuapp.com/
