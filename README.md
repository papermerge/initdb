# InitDB

Small package that creates a user and database owned by that user.
Note that it works only with *postgres* database.
Optionally it can:

* wait for database connection to be ready

## Setup

    $ pip install initdb

## Usage

    import initdb as init

    if init.db_is_ready(): # blocks script execution until database is ready
        init.create_user()
        init.create_db()

InitDB reads its configuration from environment variables.

## Environment Variables

* INITIAL_DATABASE_USER - default value is `postgres`
* INITIAL_DATABASE_PASSWORD - default value is an empty string
* DATABASE_HOST - default value is `postgres`
* DATABASE_NAME - database to be created
* DATABASE_PASSWORD - set this password for the newly created user
* DATABASE_PORT - default value is 5432
* DATABASE_USER - database user to be created