# Food Order Management System (FOMS)
Allows the user to select and order the food item very simply and seemlessly
## Usage

Fork the project and follow the steps below

import to VS Code
setup the application by following the below instructions

```
python3

# create a virtual environment
python3 -m venv venv

# activate the virtual environment
. venv/bin/activate

# install the required packages inside venv
pip3 install -r requirements.txt

# if you need to upgrade pip for package compatibility please run the command below
# and install the require package again
pip3 install --upgrade pip

# create a .env file under INTVNT-NEW folder and add the below text and update with your db values

DB_USER=add your db username
DB_PASSWORD=add your password
DB_HOST=db server ip address
DB_NAME=food_order_system # no need to change the db name

# run the project with uvicorn autoreload to watch the file changes
uvicorn main:app --reload

# deactivate the virtual environment
deactivate
```
Access the swagger API docs
http://localhost:8000/docs
