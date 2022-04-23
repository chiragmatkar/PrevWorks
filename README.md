# PrevWorks

## Project Local Install

First make sure you have python3 installed and give further commands to install the application

Clone the project locally and and run below commands to setup local python env , install required libraries and then run the flask app

```
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```


## Database Local Setup 

setup postgresql db using create_table.sql and give below commands 

```commandline
export ENVIRONMENT=LOCAL
export DATABASE_URL=postgres://postresql@localhost:5432/prevworks
```
##  Local Project Run 

```
cd PrevWorks
export FLASK_APP=flaskr
flask run
```

## Heroku Deployment

https://prevworks.herokuapp.com/
