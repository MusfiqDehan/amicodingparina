<div align="center">
    <h1>আমি কোডিং পারি না!</h1>
    A Python-Django Project with REST API, it is deployed on render and containerized using docker
    <br>
    <br>
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green">
    <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white">
    <img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white">
    <br>
    <br>
    <img src="static/homepage.png">
</div>

## Table of Contents

- [Necessary Links](#necessary-links)
- [Easy Login Info](#easy-login-info)
- [Technology Used](#technology-used)
- [Added Features](#added-features)
- [How to Run Locally](#how-to-run-locally) 
    - [From GitHub](#from-github)
    - [From Docker](#from-docker)
- [API Details](#api-details)

## Necessary Links

- **Live Link:** https://ami-coding-pari-na.onrender.com
- **API Endpoint:** https://ami-coding-pari-na.onrender.com/api/v1/items/
- **Docker Image Link:** https://hub.docker.com/r/musfiqdehan/amicodingparina-image

## Easy Login Info

To login as a user/admin, you can use the following credentials:

- Username: `admin`
- Password: `admin`

[⬆️**Go to Table of Contents**](#table-of-contents)

## Technology Used

- **Frontend:** HTML5, CSS3, Bootstrap5, JavaScript
- **Backend:** Python=3.10.6, Django=4.2.3
- **Database:** SQLite3
- **Deployment:** Render
- **API:** Django-Tastypie=0.14.5
- **Version Control:** Git, GitHub
- **Containerization:** Docker
- **Editor:** VS Code
- **Operating System:** WSL2 (Ubuntu 22.04 LTS)
- **Browser(Tested On):** Google Chrome, Microsoft Edge, Brave Browser

[⬆️**Go to Table of Contents**](#table-of-contents)


## Added Features

- **User Authentication:** Users can register and login to the website. 

- **Khoj the search Page:**

    - After login, users can access this page.
    - Khoj the search: In this segment(page), there are two input fields
    - **Input Values:** User can input comma separated integers
    - **Search Value:** User can input only one integer 
    - **Output:** Print True if the search value is in the input values. Otherwise print False

- **API Endpoints:**

    - In this section, there is only one API endpoint
    - Endpoint 1: Get All Input Values
    - User can also get filtered output using different parameters (start_datetime, end_datetime, user_id) 
    - For more info about API visit [API Details](#api-details)

- **Deployment:** The project is deployed deployed on render.

- **Containerization:** The project is containerized using docker.

- **Frontend Design:** Tried to make the frontend design as creative as possible.


[⬆️**Go to Table of Contents**](#table-of-contents)



## How to Run Locally

### From GitHub

- Install Python 3.10.6
- Install pip
```bash
sudo apt install python3-pip
```
- Install pipenv
```bash
pip3 install pipenv
```

- Clone the repository
```bash
git clone https://github.com/MusfiqDehan/amicodingparina.git
```
- Go to the project directory
```bash
cd amicodingparina
```

- Create a virtual environment
```bash
pipenv install
```
- Activate the virtual environment
```bash
pipenv shell
```
- Install the dependencies
```bash
pip3 install -r requirements.txt
```
- Run the server
```bash
python manage.py runserver 8080
```
- Open the browser and go to http://127.0.0.1:8080/
- To deactivate the virtual environment
```bash
deactivate
```

[⬆️**Go to Table of Contents**](#table-of-contents)

### From Docker

- Pull the docker image
```bash
docker pull musfiqdehan/amicodingparina:v0.1.0
``` 
- Run the docker container
```bash
docker run -p 8000:8000 musfiqdehan/amicodingparina:v0.1.0
```
- Open the browser and go to http://localhost:8000

- Remove the docker image
```bash
docker rmi musfiqdehan/amicodingparina:v0.1.0
```

[⬆️**Go to Table of Contents**](#table-of-contents)


## API Details

- **Endpoint:** https://ami-coding-pari-na.onrender.com/api/v1/items/
- **Method:** GET
- **URL Parameters:** 
    - `start_datetime=[datetime]`
    - `end_datetime=[datetime]`
    - `user_id=[integer]`
- **Example:** 

    - To include multiple parameters in the URL, you can use the ? character to start the query string and the & character to separate each key-value pair.

    - For example, if you want to get all input values from user with id 1 between July 1, 2023, and August 1, 2023, you would format your URL like this:

    - **Url with parameters:** https://ami-coding-pari-na.onrender.com/api/v1/items/?start_datetime=2023-07-01T00:00:00Z&end_datetime=2023-08-01T00:00:00Z&user_id=1

    - In this URL:

        - `start_datetime=2023-07-01T00:00:00Z`: sets the start of the datetime range.
        - `end_datetime=2023-08-01T00:00:00Z` sets the end of the datetime range.
        - `user_id=1` specifies the user.

    - The datetime format used in the URL is the **ISO 8601 Datetime Format:** `YYYY-MM-DDTHH:MM:SSZ`. This format is recognized by Django and many other web frameworks.
    
    - <details>
        <summary>YYYY-MM-DDTHH:MM:SSZ</summary>
        Each character in this string has a specific meaning:

        `YYYY`: Represents a four-digit year. For example, 2023.

        `MM`: Represents a two-digit month. For example, 07 for July.

        `DD`: Represents a two-digit day of the month. For example, 24 for the 24th day of the month.

        `T`: Is a delimiter that separates the date from the time.

        `HH`: Represents a two-digit hour in 24-hour format. For example, 13 for 1 PM.

        `MM`: Represents a two-digit minute. For example, 30 for half-past the hour.

        `SS`: Represents a two-digit second. For example, 45 for 45 seconds past the minute.

        `Z`: Indicates that the time is in Coordinated Universal Time (UTC). In other words, it is a 0 offset, equivalent to writing the time as "2012-02-09T12:22:09.144+0:00".

    </details>

[⬆️**Go to Table of Contents**](#table-of-contents)


