
import sys
import MySQLdb
import intercom
from intercom.client import Client

def connect_db(host,port,user,password,db):
    '''
    This function connects to database and checks in an error is generated.
    :param host: name of host
    :param port: port number
    :param user: user name of Database credentials
    :param password: password of Database credentials
    :param db: name of database
    :return: MySQLdb: MySQLdbobject of connection is successful
            False: if connection is not successful
    '''
    try:
        return MySQLdb.connect(host=host, port=port, user=user, passwd=password, db=db)
    except MySQLdb.Error:
        print("ERROR occured")
        return False

def getData(dbCon):
    '''
    This function performs select operation on database and returns values to main class
    :param dbCon: MySQLdb object
    :return: result: list of lists which stores output of select query
            false: if query operation fails return False
    '''
    sql = "SELECT * FROM user"
    try:
        cursor = dbCon.cursor()
        cursor.execute(sql)
        result = cursor.fetchall() #fetches all the data from database
        return result

    except MySQLdb.Error:
        print("ERROR occured")
        return False

def createUser(result):
    '''
    This function connects to intercom Client instance.
    Creates users.
    :param result: list of lists which stores output of select query

    '''
    intercom = Client(personal_access_token='my_personal_access_token')
    for row in result:
        id=row[0]
        name=row[1]
        email=row[2]
        intercom.users.create(user_id=id, email=email,name=name)


def main():
    '''
    This fucntion calls all the methods to connect to database, get data from database and creating the users.

    '''

    ip=input("Enter host IP")
    port=int(input("Enter port number"))
    user_name=input("Enter user name ")
    password=input("enter password")
    db=input("Enter database name")
    dbconn = connect_db(ip, port, user_name, password, db)
    if (dbconn):
        result=getData(dbconn)
    if (result):
        createUser(result)
    else:
        print("Error occured")
        sys.exit()

if __name__ == "_main_":
    main()





