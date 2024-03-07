# fastapi_app


pip install virtualenv
virtualenv fastapi_venv
source fastapi_venv/Scripts/activate
pip install -r requirements.txt

uvicorn fastapi_app:app --reload --port=8001

On the browser:
http://127.0.0.1:8001/docs#/default/update_item_items__item_id__put

please scroll to GET /list_users
user_input : user1
password_input : password1

Json Output: {
  "message": "User is authenticated. Welcome user: user1"
  }
