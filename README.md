# falcon-backend-template

This a project template for falcon project. I hope it can give people who wants to start a falcon based project a quick and standard start. Usually, you can just copy and paste this repo and rename it. It should have all basic things done for you. 

## Setup

First install Python 3 from [Homebrew](http://brew.sh/) and virtualenvwrapper:

    $ brew install python3
    $ pip3 install virtualenv virtualenvwrapper

After installing virtualenvwrapper please add the following line to your shell startup file (e.g. `~/.zshrc`):

    $ source /usr/local/bin/virtualenvwrapper.sh

Then reset your terminal. Clone this respository and create the virtual environment with the following commands:

    $ git clone https://github.com/wizeline/falcon-backend-template
    $ cd falcon-backend-template
    $ mkvirtualenv bot-cms-backend
    $ workon falcon-backend-template
    $ pip install -r requirements.txt


## How to run the app
run the command `gunicorn app:api`
server => is the file name. in this case there should be a file app.py under the directory for this command
api => is the variable/object name that we assign the falcon.API class for. In this case => api = falcon.API()


## Before deploy

  * Update the environment variable in app.py

  * Update the environment variable in migration/env if you need to update database
