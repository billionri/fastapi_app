# User Login

### Pre-requisite 
Install python 3.10

Install pip

### Run the following commands
#### Install `virtualenv` library  for creating virtual environment
```bash
pip install virtualenv
```

#### Create virtual environment named `fastapi_venv`
```bash
virtualenv fastapi_venv
```

#### Activate `fastapi_venv`
```bash
source fastapi_venv/Scripts/activate
```
#### Install libraries from `requirement.txt` file
```bash
pip install -r requirements.txt
```

#### Start the fast api server on port 8001
uvicorn fastapi_app:app --reload --port=8001

#### Start web application on 8001
On the browser:
http://127.0.0.1:8001/docs#/default/update_item_items__item_id__put

#### Follow the following steps
please scroll to GET /list_users
user_input : user1
password_input : password1

Json Output: {
  "message": "User is authenticated. Welcome user: user1"
  }
