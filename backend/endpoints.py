from flask import Flask, request
from flask_mysql_connector import MySQL
from decouple import config
import random
from twilio.rest import Client

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


# returns {authCode: -1} or {authCode: token} depending on if password is correct
# state: DONE. Verify for bugs
def validateLogin(request):
    # we SELECT * FROM items_collection.user where username = "adampTruck";

    loginFinder = "select * from items_collection.user where email = \"" + \
        str(request.form['email']) + "\""
    print("the query is:" + loginFinder)

    # execute the sql statement, and extract password
    cur = mysql.new_cursor(dictionary=True)
    cur.execute(loginFinder)
    output = cur.fetchone()

    if output is None:
        return {'authCode': -1}

    print(type(request.form['password']))
    print(type(output['password']))
    # compare it to actual password. If same, generate authCode
    if ((request.form['password']) == (output['password'])):
        return generateAuthCode(output)

    # if not the same, return -1
    return {'authCode': -1}


def generateAuthCode(output):
    return {'authcode': output['auth_code']}

# New user account creation


@app.post('/signup')
def sign_up():
  twillio_notify_users("3854752176","8579918356","Apple headphone", "Lederle Tower")
  return register_user(request)


def register_user(request):
    auth_code = random.randrange(0, 1000000)
    insert_query = \
        "INSERT INTO user (first_name, last_name, phone_number, auth_code, email, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cur = mysql.new_cursor(dictionary=True)
    cur.execute(insert_query, (str(request.form['first_name']), str(request.form['last_name']), str(request.form['phone_number']),
                               str(auth_code), str(request.form['email']), str(request.form['username']), str(request.form['password'])))
    output = cur.fetchall()
    mysql.connection.commit()
    return {"Status":"200"}


# psot that you need help finding a lost item
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
    "validity":val2[4],
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


@app.post('/delete-lost-item')
def delete_lost_item():
    return delete_lost_item_from_table(request)


def delete_lost_item_from_table(request):
    query = 'DELETE FROM lost_item WHERE item_id = ' + request.form['item_id']
    cur = mysql.new_cursor(dictionary=True)
    cur.execute(query)
    mysql.connection.commit()
    return {"Status":"200"}

# user round owner of lost item


@app.post('/delete-found-item')
def delete_found_item():
    return delete_found_item_from_table(request)


def delete_found_item_from_table(request):
    query = 'DELETE FROM found_item WHERE item_id = ' + request.form['item_id']
    cur = mysql.new_cursor(dictionary=True)
    cur.execute(query)
    output = cur.fetchall()
    mysql.connection.commit()
    return {"Status":"200"}

@app.post('/dashboard')
def dashboard():
  return get_items(request)

def get_items(request):
  query = 'SELECT lost_item.* from lost_item INNER JOIN user ON user.user_id = lost_item.user_id WHERE user.user_id = '+request.form['user_id']+' ORDER BY item_valid_until DESC LIMIT 3'
  cur = mysql.new_cursor(dictionary=True)
  cur.execute(query)
  output = cur.fetchall()
  mysql.connection.commit()
  return output

def twillio_notify_users(phone_number1, phone_number2, item_name, location):
  """
  phone number 1 is the person who lost the item
  phone number 2 is the person who found the item
  to notify the users if there is a match in the system for the post item and found item
  using twillio API to notify users
  """

  # message_to_lost_person = f"Hello, this is Find.it platform texting! Another user who potentially lost {item_name} at {location}!! Please reach out to this phone number, {phone_number1}, to see if there is a match!"
  message_to_found_person = f"Hello, this is Find.it platform texting! Another user who potentially found {item_name} at {location}!! Please reach out to this phone number, {phone_number2}, to see if there is a match!"
  account_sid = config("account_sid")
  auth_token = config("auth_token")
  client = Client(account_sid, auth_token)

  message = client.messages.create(
  body=message_to_found_person,
  from_=f'+1{phone_number1}',
  to=f'+1{phone_number2}'
  )

  
# Running app
if __name__ == '__main__':
    app.run(debug=True)
