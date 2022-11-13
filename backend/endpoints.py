from datetime import datetime
from decimal import Decimal
import random
from flask import Flask, request, render_template
# from flask_mysqldb import MySQL
from flask_mysql_connector import MySQL
from decouple import config
import random

# Initializing flask app
app = Flask(__name__)

# app.config['MYSQL_USER'] = config('USER')
# app.config['MYSQL_DATABASE'] = config('DB')
# app.config['MYSQL_PASSWORD'] = config('PASS')

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DATABASE'] = 'items_collection'
app.config['MYSQL_PASSWORD'] = 'heffeOfOhill'

mysql = MySQL(app)

# Login page
@app.post('/login')
def login():
  return validateLogin(request)


# returns {authCode: -1} or {authCode: token} depending on if password is correct 
# state: DONE. Verify for bugs
def validateLogin(request): 
  # we SELECT * FROM items_collection.user where username = "adampTruck";

  loginFinder = "select * from items_collection.user where email = \"" + str(request.form['email']) + "\""; 
  print("the query is:" + loginFinder); 

  # execute the sql statement, and extract password
  cur = mysql.new_cursor(dictionary=True)
  cur.execute(loginFinder)
  output = cur.fetchone()

  if output is None: 
    return {'authCode': -1}

  print(type(request.form['password']))
  print(type(output['password']))
  #compare it to actual password. If same, generate authCode
  if ((request.form['password']) == (output['password'])):
     return generateAuthCode(output)

  #if not the same, return -1 
  return {'authCode': -1}

def generateAuthCode(output): 
  return {'authcode': output['auth_code']}




# psot that you need help finding a lost item
@app.post('/find-lost-item')
def find_item():

  # first verify necessary fields are there 

  # print(request.form.__contains__['email'])
  print(request.form['email'])
  print(request.form['email'])
  return "sheesh"

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


 # anan: post lost item -> goes to found lost item 
@app.post('/post-lost-item')
def post_item():
  # cur = mysql.new_cursor(dictionary=True)

  # # get the number to allocate 
  # print("hello")
  # findHighest = "select * from items_collection.item_identifier ORDER by item_id desc;"
  # cur.execute(findHighest)
  # nextIndex = len(cur.fetchall())+1 # important 
  
  # # find the coords of an item 
  # print(str(request.form['item_location']))
  # locQ = "select * from items_collection.location_coords_translator where location_name = \"" + str(request.form['item_location']) + "\""
  # cur.execute(locQ)
  # coordsData = cur.fetchone()
  # xCoord = coordsData['location_xCoords']
  # yCoord = coordsData['location_yCoords'] #important 

  # userId = request.form['user_id']

  # #date of an object
  # dateLost = datetime.strptime(request.form['item_date'], '%m-%d-%Y').date()

  # # post the found item 
  # q = "insert into items_collection.found_item (item_id, user_id, x_coord, y_coord, item_valid_until) values(%s, %s, %s, %s, %s)"
  # qEntries = (nextIndex, userId, xCoord, yCoord, dateLost)
  # cur.execute(q, qEntries)
  # mysql.connection.commit()

  # # create in generic using description and all that 
  # q2 = "insert into items_collection.item_identifier (item_id, item_description, item_name) values(%s, %s, %s)"
  # q2Entries = (nextIndex, request.form["item_description"], request.form["item_name"])
  # cur.execute(q2, q2Entries)
  # mysql.connection.commit()

  # #find all related lost items 
  # find_related_lost_items(nextIndex, userId)

  find_related_lost_items(11, 20)
  return {"hello":"eric"}

  #0.0005

# user found the item they lost
def twillio_notify_users(phone_number1, phone_number2, item_name):
  print("test")


#todo: get rleated lost items 
def find_related_lost_items(found_item_id, posterId): 
    cur = mysql.new_cursor(dictionary=True)
    qFindWords = "select * from items_collection.item_identifier where item_id = \"" + str(found_item_id) + "\" limit 1"
    h1 = cur.execute(qFindWords)
    userOne = cur.fetchone()
    useless = cur.fetchall()
    cur_found_item_words = str.split(userOne['item_name'])

    locQ = "select * from items_collection.location_coords_translator where location_name = \"" + str(request.form['item_location']) + "\""
    cur.execute(locQ)
    coordsData = cur.fetchone()
    useless = cur.fetchall()
    xCoord = coordsData['location_xCoords']
    yCoord = coordsData['location_yCoords'] #important 
    offset = Decimal("0.0005")
    print(str(xCoord+offset))

    qItemFind = "select * from items_collection.lost_item as l inner join items_collection.item_identifier as g on l.item_id = g.item_id and l.x_coords >= " + str(xCoord) + " and l.x_coords <= " + str(xCoord + offset) + " and l.y_coords >= " + str(yCoord) + "  and l.y_coords <= + " + str(yCoord+offset)
    cur.execute(qItemFind)
    # mysql.connection.commit()
    candidateItems = cur.fetchall()
    print(len(candidateItems))

    for candidate in candidateItems: 
      candidate_item_words = str.split(candidate['item_name'])
      print(str(candidate_item_words))
      if (any([item in candidate_item_words for item in cur_found_item_words ])): 
        item_name = userOne['item_name']

        
        p1 = cur.execute("select * from items_collection.user where user_id = \"" + str(posterId) + "\"")
        
        phone_number_1 = cur.fetchone()
        p1R = "123456789"
        if phone_number_1 is not None: 
          p1R = phone_number_1['phone_number']

        p2 = cur.execute("select * from items_collection.user where user_id = \"" + str(candidate['user_id']) + "\"")
        p2R = "123456789"
        phone_number_2 = cur.fetchone()
        if phone_number_2 is not None: 
          p2R = phone_number_2['phone_number']


        twillio_notify_users(p1R, p2R, item_name)
        print('notified one')

    



      

#todo: dashboard? 





@app.route('/delete-lost-item')
def delete_lost_item():
    return 'delete lost item'

# user round owner of lost item


@app.route('/delete-found-item')
def delete_found_item():
    return 'delete found item'

# user updates info of item they lost

#anan
@app.route('/update-lost-item')
def update_lost_item():
    return 'update item lost'

# user updates info of item they found

#anan
@app.route('/update-found-item')
def update_found_item():
    return 'update found item'

# Running app
if __name__ == '__main__':
    app.run(debug=False)
