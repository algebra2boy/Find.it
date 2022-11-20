from datetime import datetime
from decimal import Decimal
from flask import Flask, request, jsonify
from flask_mysql_connector import MySQL
from decouple import config
import random

# from flask_mysqldb import MySQL
from twilio.rest import Client

# Initializing flask app
app = Flask(__name__)

app.config['MYSQL_USER'] = config('USER')
app.config['MYSQL_DATABASE'] = config('DB')
app.config['MYSQL_PASSWORD'] = config('PASS')

mysql = MySQL(app)


@app.get('/')
def home():
    return "Hello, world"

# Login page


@app.post('/login')
def login():
    # return {"authcode":"21"}
    return validateLogin(request)


# returns {authCode: -1} or {authCode: token} depending on if password is correct
# state: DONE. Verify for bugs
def validateLogin(request):

    loginFinderQuery = "select * from items_collection.user where email = \"" + \
        str(request.form['email']) + "\";"
    print("the query is: " + loginFinderQuery)

    # execute the sql statement, and extract password
    cur = mysql.new_cursor(dictionary=True)
    cur.execute(loginFinderQuery)
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
    twillio_notify_users("3854752176", "8579918356",
                         "Apple headphone", "Lederle Tower")
    return register_user(request)


def register_user(request):
    # generate a random authorization code from 0 to 1000000
    auth_code = random.randrange(0, 1000000)
    Insert_A_User_To_DB_Query = \
        "INSERT INTO user (first_name, last_name, phone_number, auth_code, email, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cur = mysql.new_cursor(dictionary=True)
    cur.execute(Insert_A_User_To_DB_Query, (str(request.form['first_name']), str(request.form['last_name']), str(request.form['phone_number']),
                                            str(auth_code), str(request.form['email']), str(request.form['username']), str(request.form['password'])))
    output = cur.fetchall()
    mysql.connection.commit()
    return str(output)


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
    q = "insert into lost_item (item_picture_link, item_valid_until, user_id, x_coords, y_coords) values(%s,%s,%s,%s,%s)" + ";"
    val = (request.form['item_picture_link'], request.form['item_valid_until'],
           request.form['user_id'], request.form['x_coords'], request.form['y_coords'])
    cur.execute(q, val)
    mysql.connection.commit()
    return {
        "link": val[0],
        "validity": val[1],
        "uid": val[2],
        "x_coords": val[3],
        "y_coords": val[4],
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
    return {"hello": "eric"}

# user found the item they lost


def twillio_notify_users(phone_number1, phone_number2, item_name):
    print("test")


# todo: get rleated lost items
def find_related_lost_items(found_item_id, posterId):

    # retrieve only one item from the item_identifier
    cur = mysql.new_cursor(dictionary=True)
    qFindWords = "select * from items_collection.item_identifier where item_id = \"" + \
        str(found_item_id) + "\" limit 1" + ";"
    h1 = cur.execute(qFindWords)
    userOne = cur.fetchone()
    cur_found_item_words = str.split(userOne['item_name'])

    # retrieve one location coordinator from the databae 
    locQ = "select * from items_collection.location_coords_translator where location_name = \"" + \
        str(request.form['item_location']) + "\""
    cur.execute(locQ)
    coordsData = cur.fetchone()


    xCoord = coordsData['location_xCoords']
    yCoord = coordsData['location_yCoords']  # important
    offset = Decimal("0.0005")

    print(str(xCoord+offset))

    qItemFind = "select * from items_collection.lost_item as l inner join items_collection.item_identifier as g on l.item_id = g.item_id and l.x_coords >= " + \
        str(xCoord) + " and l.x_coords <= " + str(xCoord + offset) + \
        " and l.y_coords >= " + \
        str(yCoord) + "  and l.y_coords <= + " + str(yCoord+offset) + " ;"
    cur.execute(qItemFind)
    # mysql.connection.commit()
    candidateItems = cur.fetchall()
    print(len(candidateItems))

    for candidate in candidateItems:
        candidate_item_words = str.split(candidate['item_name'])
        print(str(candidate_item_words))
        if (any([item in candidate_item_words for item in cur_found_item_words])):
            item_name = userOne['item_name']

            p1 = cur.execute(
                "select * from items_collection.user where user_id = \"" + str(posterId) + "\"")

            phone_number_1 = cur.fetchone()
            p1R = "123456789"
            if phone_number_1 is not None:
                p1R = phone_number_1['phone_number']

            p2 = cur.execute(
                "select * from items_collection.user where user_id = \"" + str(candidate['user_id']) + "\"")
            p2R = "123456789"
            phone_number_2 = cur.fetchone()
            if phone_number_2 is not None:
                p2R = phone_number_2['phone_number']

            twillio_notify_users(p1R, p2R, item_name)
            print('notified one')


# todo: dashboard?


@app.post('/delete-lost-item')
def delete_lost_item():
    return delete_lost_item_from_table(request)


def delete_lost_item_from_table(request):
    query = 'DELETE FROM lost_item WHERE item_id = ' + request.form['item_id'] + ";"
    cur = mysql.new_cursor(dictionary=True)
    cur.execute(query)
    output = cur.fetchall()
    mysql.connection.commit()
    return str(output)

# user round owner of lost item


@app.post('/delete-found-item')
def delete_found_item():
    return delete_found_item_from_table(request)


def delete_found_item_from_table(request):
    query = 'DELETE FROM found_item WHERE item_id = ' + request.form['item_id'] + ";"
    cur = mysql.new_cursor(dictionary=True)
    cur.execute(query)
    output = cur.fetchall()
    mysql.connection.commit()
    return str(output)


def twillio_notify_users(phone_number1, phone_number2, item_name):
    """
    phone number 1 is the person who lost the item
    phone number 2 is the person who found the item
    to notify the users if there is a match in the system for the post item and found item
    using twillio API to notify users
    """

    # message_to_lost_person = f"Hello, this is Find.it platform texting! Another user who potentially lost {item_name}!! Please reach out to this phone number, {phone_number1}, to see if there is a match!"
    message_to_found_person = f"Hello, this is Find.it platform texting! Another user who potentially found {item_name}!! Please reach out to this phone number, {phone_number2}, to see if there is a match!"
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
