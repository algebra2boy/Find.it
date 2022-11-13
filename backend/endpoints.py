from flask import Flask, request, render_template
from flask_mysql_connector import MySQL
import datetime
import random

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)


mysql = MySQL(app)

# Login page
@app.post('/login')
def login():
  return validateLogin(request)


# returns true or false depending on if the 
def validateLogin(request): 
  # we SELECT * FROM items_collection.user where username = "adampTruck";
  loginFinder = "select * from items_collection.user where email = \"" + str(request.form['email']) + "\""; 
  print("the query is:" + loginFinder); 

  cur = mysql.new_cursor(dictionary=True)
  cur.execute(loginFinder)
  output = cur.fetchone()
  
  print(len(output['password']))
  print(len(request.form['password']))

  if (str(request.form['password']) == str(output['password'])):
     return {'tokenid': 100}

  return {'tokenid': -1}




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

@app.post('/find-lost-item')
def find_item():
    return found_lost_item(request)

# user found a lost item
def found_lost_item(request):
  cur = mysql.new_cursor(dictionary=True)
  q = "insert into item_identifier (item_description) values (%s)"
  val1 = [request.form['item_description']]
  cur.execute(q, val1)
  mysql.connection.commit()
  q = "select * from item_identifier order by item_id desc"
  cur.execute(q)
  res = cur.fetchone()
  throw = cur.fetchall()
  blurb = f"%{request.form['location_name']}%"
  cur.execute(f"select * from location_coords_translator where location_name like '{blurb}'")
  loc = cur.fetchone()
  xcoords = loc['location_xCoords']
  ycoords = loc['location_yCoords']
  q = "insert into lost_item (item_id, user_id, x_coords, y_coords, item_valid_until) values (%s, %s, %s, %s, %s)"
  val2 = (res['item_id'], request.form['user_id'], xcoords, ycoords, datetime.date.today())
  cur.execute(q, val2)
  mysql.connection.commit()
  return {
    "id": res["item_id"],
    "validity":val2[1],
    "uid":val2[1],
    "location":request.form['location_name'],
    "x_coords":val2[2],
    "y_coords":val2[3],
    "status": "Success"
  }



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
