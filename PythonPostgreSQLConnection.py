# This library for Postgresql, most of python developers use this library
import psycopg2

# Connect to the database
#con = psycopg2.connect(host="localhost",#
#                       database="database_you_will_connect",
#                       user="postgres",
#                       password="your_password_please")
con = psycopg2.connect(host="localhost",database="dvdrental",user="postgres",password="mypassword:)")
# create cursor
# Cursor allows us to interact or communicate with database.
cur = con.cursor()
# There are two types of cursors: client-side cursor and server-side cursor.
# Client-site cursor allocates memory for which we are working on.

# execute query, bir query başlat
# If you want to make changes on tables that means you have to give a command onto cursor

# Insertion,
cur.execute("insert into city (city_id, city, country_id) values (%s, %s, %s)", (601, "Zonguldak", 97))

# Select the table
cur.execute("SELECT city_id, city FROM city")
# assign the query to row
rows = cur.fetchall()
for r in rows:
    print(f"id {r[0]} name {r[1]}")
# f in the print allows to fancy which means it activates fancy paranthesis
# We can see the records with this loops

# commit the changes on connection that you open
con.commit()
# close the cursor connection
cur.close()
# close the database connection
con.close()