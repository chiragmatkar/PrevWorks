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

![Screenshot 2022-04-26 at 4 18 49 PM](https://user-images.githubusercontent.com/335651/165284165-4063d636-2dcf-4d35-a7b0-b1bac2c63bd1.png)

### Report Injury
-  Employees can submit a report of their injuries on the Report Injury page. 
-  The page provides a form to report covid-19 symptoms and a body diagram to select injured body parts. 
-  Employees can report the injured date and descriptions through the provided text box.
-  Covid-19 Symptoms Report

![Screenshot 2022-04-26 at 4 21 25 PM](https://user-images.githubusercontent.com/335651/165284493-e475191b-dc10-43cf-bcdf-869dca216976.png)




