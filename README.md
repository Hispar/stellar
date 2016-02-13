## Dependencies
To run this project in a local environment, you will need Python 2.7 with django 1.9 and djangorestframework 3.3.2.
You can install the dependencies with pip using `pip install -r requirements-vendor.txt`

The database in the local environment is sqlite. A copy with data is already included.

## Run local environment
Execute `python manage.py runserver --settings=stellar.settings.local`.

In the `/admin` path with user `admin`and pass `a12345678` you can access to de administration of the app.

In the path `/api/v1/` you can see the api rest created.


## Run Google App Engine 

Install the [App Engine Python SDK](https://developers.google.com/appengine/downloads).
You'll need python 2.7 and [pip 7.0 or later](http://www.pip-installer.org/en/latest/installing.html) installed too.


Create a new CloudSQL instance.
    * From the Google Cloud Console, go to [Storage > CloudSQL> Create Instance](https://console.developers.google.com/project/_/sql/create)
    * Under [Access Control > IP Address](https://console.developers.google.com/project/_/sql/instances/polls/access-control/ip),  
    Request IPv4 Address. This address will be your HOST for remote access to the
      CloudSQL instance in stellar/settings/production.py, so replace `<your-database-host>` with this address.
    * Under [Databases](https://console.developers.google.com/project/_/sql/instances/polls/databases), 
    click New Database and create the name for your database in stellar/settings/production.py. Replace
      `<your-database-name>` with this value.
    * At this point, your deployed AppEngine application can access the database, after you replace `<your-project-id>` and
    `<your-database-name>` in mysite/settings.py. The following instructions are to connect to the same CloudSQL instance
    locally. Alternatively, you could install a local MySQL instance and use that in development.
    * Under [Access Control > Authorization](https://console.developers.google.com/project/_/sql/instances/polls/access-control/authorization) Under "Allowed Networks", click "Add item", and add Network 0.0.0.0/0. This opens up
          access to your CloudSQL instance from any network. Stricter firewall settings should be considered for production
          applications.
    * Under  [Access Control > Authorization](https://console.developers.google.com/project/_/sql/instances/polls/access-control/users), Click
          "Create user account". Create a username and password and edit stellar/production/settings.py DATABASES
          to reflect this. Replace `<your-database-user>` and `<your-database-password>` with these variables.
