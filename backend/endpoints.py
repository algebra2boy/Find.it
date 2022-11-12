from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import datetime
  
x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)

app.config['MYSWL_HOST'] = 'localhost'
app.config['MySQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

cursor = mysql.connection.cursor()

# Home page  
@app.route('/')
def home_page():
  return "hello"
  
# Login page
@app.route('/login', methods = ['GET', 'POST'])
def login():
  if request == 'GET':
    return "show login form"
  else:
    return "login the user"

# New user account creation
@app.route('/signup')
def sign_up():
  return 'signup'

# user lost item
@app.route('/find-lost-item')
def find_item():
  return 'find lost'

# user found a lost item
@app.route('/post-lost-item')
def post_item():
  return 'post lost'

# user found the item they lost
@app.route('/delete-lost-item')
def delete_lost_item():
  return 'delete lost item'

# user round owner of lost item
@app.route('/delete-found-item')
def delete_found_item():
  return 'delete found item'

# user updates info of item they lost
@app.route('/update-lost-item')
def update_lost_item():
  return 'update item lost'

# user updates info of item they found
@app.route('/update-found-item')
def update_found_item():
  return 'update found item'

# example for testing
@app.route('/data')
def get_time():
  # Return a json for front end to view
  return {
      "Date":x, 
      "Framwork":"flask",
      "Folder":"backend"
  }
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)