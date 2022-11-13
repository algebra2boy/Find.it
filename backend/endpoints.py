import datetime

from flask import Flask, render_template, request
# from flask_mysqldb import MySQL
from flask_mysql_connector import MySQL

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)

app.config['MYSQL_USER'] = 'j1'
app.config['MYSQL_DATABASE'] = 'items_collection'
app.config['MYSQL_PASSWORD'] = 'sqlpass1!'

mysql = MySQL(app)

EXAMPLE_SQL = 'select * from user'

# using the new_cursor() method


@app.route('/new_cursor')
def new_cursor():
    cur = mysql.new_cursor(dictionary=True)
    cur.execute(EXAMPLE_SQL)
    output = cur.fetchall()
    return str(output)

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




# def login_test(request):
#     print(request.form['username'] + request.form['password'])
#     print(request)
#     return str(request.form['username'] + request.form['password'] + "wombat")

# # New user account creation



@app.route('/signup')
def sign_up():
    return 'signup'
  




@app.post('/find-lost-item')
def find_item():
  return post_item_db(request)
  
# user found a lost item
def post_item_db(request):
  # q = "select * from lost_item"
  cur = mysql.new_cursor(dictionary=True)
  # print(len(res))
  # if len(res) > 1:
  #   res = res[0]
  # else:
  #   pass
  # return {
  #   "id":res['item_id'],
  #   "picLink":res['item_picture_link'],
  #   "validity":res['item_valid_until'],
  #   "uid":res['user_id'],
  #   "x_loc":res['x_coords'],
  #   "y_loc":res['y_coords']
  # }
  q = "insert into lost_item (item_picture_link, item_valid_until, user_id, x_coords, y_coords) values(%s,%s,%s,%s,%s)"
  val = (request.form['item_picture_link'],request.form['item_valid_until'],request.form['user_id'],request.form['x_coords'],request.form['y_coords'])
  cur.execute(q, val)
  mysql.connection.commit()
  return {
    "link":val[0],
    "validity":val[1],
    "uid":val[2],
    "x_coords":val[3],
    "y_coords":val[4],
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

# example for testing


@app.route('/data')
def get_time():
    # Return a json for front end to view
    return {
        "Date": x,
        "Framwork": "flask",
        "Folder": "backend"
    }


# Running app
if __name__ == '__main__':
    app.run(debug=True)
