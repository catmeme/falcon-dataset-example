# falcon-dataset-example

###### Setup a virtualenv:

```
virtualenv -p /usr/bin/python3.4 venv
ln -s venv/bin/activate
source activate
```

###### Install dependencies:

`pip install -r requirements.txt`

###### Create a database:

You should know how.

###### Run the application:

`DATABASE_URL='mysql+pymysql://root:local@localhost/mydatabase' gunicorn app:api -b '127.0.0.1:8080'`

###### Visit:

http://127.0.0.1:8080/users

###### Add/Update/Delete:

Use a REST client, such as POSTman to interact with the API.
