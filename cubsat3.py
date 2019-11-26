import sqlite3
from sqlite3 import Error
import requests
 
html = 'https://www.celestrak.com/NORAD/elements/cubesat.txt'
name = input("Enter Name: ")
DATA = ["","","","","","","","","","","","","","","","","","",""]
TLESIZE = [[0,23],[26,30],31,[33,34],[35,37],[38,40],[42,43],[44,55],[57,66],[68,75],[78,84],[88,91],[101,108],[110,117],[119,125],[127,134],[136,143],[145,155],[156,160]]
#conn = None
#conn = None
def create_connection(db_file):


    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return conn
 
##def create_db(db):
##    
##    """ create a database connection to a SQLite database """
##    conn = None
##    try:
##        conn = sqlite3.connect(db)
##        print(sqlite3.version)
##    except Error as e:
##        print(e)
##    finally:
##        if conn:
##            conn.close()
 
    
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
 
def insert_data(conn,a):
    SN = a[0]
    SCN = a[1]
    C = a[2]
    ID1 = a[3]
    ID2 = a[4]
    E1 = a[5]
    E2 = a[6]
    MM1 = a[7]
    MM2 = a[8]
    RPS = a[9]
    ESN = a[10]
    I = a[11]
    RA = a[12]
    E = a[13]
    A = a[14]
    MA = a[15]
    MM = a[16]
    R = a[17]
    
    part = f"""INSERT INTO projects({SN},{SCN},{C},{ID1},{ID2},{E1},{E2},{MM1},{MM2},{RPS},{ESN},{I},{RA},{E},{A},{MA},{MM},{R}) VALUES(satellite_name,satellite_catalog_number,classification,International_Designator1,International_Designator2,Epoch1,Epoch2,Mean_motion1d,Mean_motion2d,RPS,Element_s3t_number,Inclination,R1ght_Ascension_0f_the_Ascending_Node,Eccentricity,Argument_0f_Perigee,Mean_Anomaly,Mean_Motion,Revolution_number_at_epoch);"""
    print(part)
    
    try:
        c = conn.cursor()
        c.execute(part)
    except Error as e:
        print(e)
 
def main():
    database = "r"+input("enter directory: ")
    #create_db(database)
    
    #r"C:\sqlite\db\pythonsqlite.db"
     
    table = """ CREATE TABLE IF NOT EXISTS projects (id integer PRIMARY KEY,
satellite_name text NOT NULL,
satellite_catalog_number integer,
classification text,
International_Designator1 integer,
International_Designator2 text,
Epoch1 integer,
Epoch2 decimal,
Mean_motion1d decimal,
Mean_motion2d decimal,
RPS decimal,
Element_s3t_number integer,
Inclination decimal,
R1ght_Ascension_0f_the_Ascending_Node decimal,
Eccentricity decimal,
Argument_0f_Perigee decimal,
Mean_Anomaly decimal,
Mean_Motion decimal,
Revolution_number_at_epoch integer
); """
 
    #create_db(conn)
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, table)
    else:
        print("Error! cannot create the database connection.")
 




 


    
def fetch(html,name):
    textTemp = ""
    temp = ""
    f= open("test.txt","w")
    response = requests.get(html)
    body2 = response.text
    f.write(body2)
    f.close() 
    f= open("test.txt","r")
    printed = False
    n = 0
    for line in f:
        if line.startswith(name):
            printed = True
        if printed and n<6:
            n = n + 1
            temp = line[:-1]
            textTemp = textTemp + temp
            print(line)
        elif n<6:
            printed = False
    f.close()
    a = 0
    
    for i in range(0,19):
        if (type(TLESIZE[i]) != int) :
            DATA[i] = textTemp[TLESIZE[i][0] : TLESIZE[i][1]+1]
        else:
            DATA[i] = textTemp[TLESIZE[i]]

main()
database = "r"+input("enter directory: ")
conn = create_connection(database)

fetch(html,name)
insert_data(conn,DATA)
