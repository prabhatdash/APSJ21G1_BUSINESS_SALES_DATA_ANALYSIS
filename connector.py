import mysql.connector as mc
dbc = mc.connect(host="localhost",user="root",passwd="root",database="apsj21g1")
cursor=dbc.cursor()