# Bank security console
This console shows:
* list of active passcard users
* list of users currently in the vault
* list of visits per specified user

## Installation
0. You need python interpreter installed on your PС. The project is tested on Python 3.10.
1. Clone the project to your PC, details [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
2. Install, run and activate your virtual environment, details [here](https://docs.python-guide.org/dev/virtualenvs/).
3. To install the dependencies, simply run ```pip install -r requirements.txt```.
4. Retrieve from the system administrator the environment variables:
* DB_HOST
* DB_USER
* DB_PASSWORD
* SECRET_KEY
5. In the root directory of the project create a file named '.env', put the environment variables in it.

## Usage
1. Run the server with `python manage.py runserver {address:port}`
2. Open the console at `{address:port}` in your browser

## Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.