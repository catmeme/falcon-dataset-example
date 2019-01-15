# falcon-dataset-example

###### Setup a virtualenv:

```
python3 -m venv venv
source venv/bin/activate
```

###### Install dependencies:

`pip3 install -r requirements.in`

###### Create a database:

You should know how.

###### Run the application:

`DATABASE_URL='mysql+pymysql://root:local@localhost/mydatabase' gunicorn app:api -b '127.0.0.1:8080'`

###### Visit:

http://127.0.0.1:8080/users

###### Add/Update/Delete:

Use a REST client, such as POSTman to interact with the API.
