# Vitrine web server
[![GitHub](https://img.shields.io/github/license/vitrine-app/vitrine.svg?style=flat-square)](/LICENSE.md)
![Python](https://img.shields.io/badge/python-3.6-blue.svg?style=flat-square)
![Golang](https://img.shields.io/badge/golang-1.10-lightblue.svg?style=flat-square)

## About
This is the web server used by the Vitrine client.
For the moment, it is mainly used to call the [games catcher](https://github.com/vitrine-app/games-catcher) to store games into our own database.

## Running
To get everything running, you need the same key as the [Vitrine client](https://github.com/vitrine-app/vitrine/blob/master/.github/CONTRIBUTING.md) to be stored as a `VITRINE_KEY` environment variable. Don't hesitate to [contact me](mailto:paul.roman@epitech.eu) to get a key.

The server is running in a Docker environment, all you need is [Docker](https://docs.docker.com/install) and [Docker Compose](https://docs.docker.com/compose/install).
We're using Docker Compose with 3 containers :
- `vitrine-server` for the web server written in Python and the dynamic library written in Go 
- `vitrine-db` for the MySQL database
- `vitrine-adminer` for monitoring the database through [Adminer](https://www.adminer.org)

Then just go to `localhost` to access to the web server and `localhost:8080` for the Adminer dashboard (the password for the database is the `VITRINE_KEY` env variable for the moment).
