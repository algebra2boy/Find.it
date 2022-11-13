from flask import Flask, request
from flask_mysql_connector import MySQL
from decouple import config
import random

# Initializing flask app
app = Flask(__name__)

app.config['MYSQL_USER'] = config('USER')
app.config['MYSQL_DATABASE'] = config('DB')
app.config['MYSQL_PASSWORD'] = config('PASS')

mysql = MySQL(app)

# Login page
@app.post('/login')
def login():
  return validateLogin(request)


def validateLogin(request): 
  # SELECT * FROM items_collection.user where username = "adampTruck";
  loginFinder = "select * from items_collection.user where username = \"" + str(request.form['username']) + "\""; 
  print("the query is:" + loginFinder); 

  cur = mysql.new_cursor(dictionary=True)
  cur.execute(loginFinder)
  output = cur.fetchall()

  print(str(output))

  return str(output)


# New user account creation
@app.post('/signup')
def sign_up():
  return register_user(request)

def register_user(request):
  auth_code = random.randrange(0, 1000000)
  insert_query = \
  "INSERT INTO user (user_id, first_name, last_name, phone_number, auth_code, email, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
  cur = mysql.new_cursor(dictionary=True)
  cur.execute(insert_query, (str(15), str(request.form['first_name']), str(request.form['last_name']), str(request.form['phone_number']),\
    str(auth_code), str(request.form['email']), str(request.form['username']), str(request.form['password'])))
  output = cur.fetchall()
  mysql.connection.commit()
  return str(output)

@app.route('/find-lost-item')
def find_item():
  return 'find lost item'

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

# Running app
if __name__ == '__main__':
    app.run(debug=True)
