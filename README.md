# InitDB

Small package that creates a user and database owned by that user.
Note that it works only with *postgres* database.
Optionally it can:

* wait for database connection to be ready

## Setup

    $ poetry add initdb

## Usage

Use it from command line:

    $ python -m initdb

In order to print its config:

    $ python -m initdb print

Use it from other scripts:

    import initdb as init

    if init.db_is_ready(): # blocks script execution until database is ready
        init.create_user()
        init.create_db()

`db_is_ready` function will try to connect to database and using
`INITIAL_DATABASE_USER`, `PAPERMERGE_DATABASE_HOST`, and `PAPERMERGE_DATABASE_PORT`. If there is an
error during the connection e.g. database is not availble, it will block
(infinit loop with one second delay between cycles) the script until connection
succeeds. When connection successed it will create a user, a database owned by
that user and will exit.

## Environment Variables

InitDB reads its configuration from following environment variables.

* INITIAL_DATABASE_USER - default value is `postgres`
* INITIAL_DATABASE_PASSWORD - default value is an empty string
* PAPERMERGE_DATABASE_HOST - default value is `postgres`
* PAPERMERGE_DATABASE_NAME - database to be created
* PAPERMERGE_DATABASE_PASSWORD - set this password for the newly created user
* PAPERMERGE_DATABASE_PORT - default value is 5432
* PAPERMERGE_DATABASE_USER - database user to be created
