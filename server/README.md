# Server

## Prerequisites

* [Python 3.x](https://www.python.org/)

## Getting started

Initialize a local Python venv and populate it with the required third party dependencies that are defined in `requirements.txt`:

```Shell
python3 -m venv ./venv
source venv/bin/activate
pip3 install -r requirements.txt
deactivate
```

## Running the server

```Shell
source venv/bin/activate
python -m flask run
```
