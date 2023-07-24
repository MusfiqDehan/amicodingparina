<div align="center">
    <h1>আমি কোডিং পারি না!</h1>
    A Python-Django Project
    <br>
    <br>
    <img src="static/homepage.png">
</div>

## Table of Contents

- [Necessary Links](#necessary-links)
- [Technology Used](#technology-used)
- [How to Run](#how-to-run) 
    - [Locally](#locally)
    - [Using Docker](#using-docker)
- [API Details](#api-details)

## Necessary Links

- **Live Link:** https://ami-coding-pari-na.onrender.com
- **API Endpoint:** https://ami-coding-pari-na.onrender.com/api/v1/items/

## Technology Used

- **Frontend:** HTML5, CSS3, Bootstrap5, JavaScript
- **Backend:** Python=3.10.6, Django=4.2.3
- **Database:** SQLite3
- **Deployment:** Render
- **API:** Django-Tastypie=0.14.5
- **Version Control:** Git
- **Editor:** VS Code
- **Operating System:** WSL2 (Ubuntu 22.04 LTS)
- **Browser:** Google Chrome, Microsoft Edge

## How to Run

### Locally

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
exit
```

### Using Docker

- Clone the repository
```bash
git clone https://github.com/MusfiqDehan/amicodingparina.git
```
- Go to the project directory
```bash
cd amicodingparina
```

- Build the docker image
```bash
docker build -t ami-coding-pari-na .
```
- Run the docker container
```bash
docker run -p 8000:8000 ami-coding-pari-na
```
- Open the browser and go to http://localhost:8000

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



