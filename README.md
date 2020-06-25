# flask_rest_api_test
Flask test application with one endpoint (User)
## Install
```shell script
git clone https://github.com/culnaen/flask_rest_api_test.git
cd flask_rest_api_test
pip install -r requirements.txt
```

## Launching
```shell script
python -m app
```
> in the project directory

## Usage

* GET /users 

  Return the list of users

* GET /users/id

  Return user data by id
  
* POST /users

  Create user
  
  Example value:
  ```
  { 
      "name": "string"
  }
  ```
  
  Return data of created user

* DELETE /users/id
  
  Delete user by id
  
  Return "deleted" if user deleted or "user not found" if the user is not found
  
* PUT /users/id
  
  Change user by id
  
  Example value:
  ```
  {
      "name": "string"
  }
  ```
  
  Return modified data if user found or return 
  
