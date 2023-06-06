import mysql.connector

database = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "Vaishali123!",
	auth_plugin='mysql_native_password'

	)

# prepare a cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")