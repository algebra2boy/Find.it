from flask import Flask, request, render_template
# from flask_mysqldb import MySQL
from flask_mysql_connector import MySQL
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DATABASE'] = 'items_collection'
app.config['MYSQL_PASSWORD'] = 'heffeOfOhill'

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
        "Date": x,
        "Framwork": "flask",
        "Folder": "backend"
    }


# Running app
if __name__ == '__main__':
    app.run(debug=True)
