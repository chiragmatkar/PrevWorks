# PrevWorks

## Project Local Install

First make sure you have python3 installed and give further commands to install the application

Clone the project locally and run below commands to setup local python env , 
install required libraries and then run the flask app

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


## Prevworks UI Design

### Authentication Pages Employee Pages
#### Profile Page
- Includes information about the user and forms that allow the user to change information about the user such as address and password.

![Screenshot 2022-04-26 at 4 14 51 PM](https://user-images.githubusercontent.com/335651/165283453-b80008da-9fd0-4819-92f9-8761a95be34e.png)

#### Companies Page
-  Includes information about the companies that the employee is a part of and allows them to add and remove companies from their list.

![Screenshot 2022-04-26 at 4 14 51 PM](https://user-images.githubusercontent.com/335651/165284076-ecdd71d1-505b-4db2-8be8-6c7dad8cb30c.png)


