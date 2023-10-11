# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python
"""
encourted below error
(venv) G:\Python\Django>python mydb.py
Error: Authentication plugin 'caching_sha2_password' is not supported
Traceback (most recent call last):
  File "G:\Python\Django\mydb.py", line 25, in <module>
    if dataBase.is_connected():
       ^^^^^^^^
NameError: name 'dataBase' is not defined

followed below steps to resolve:
1. mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY '1234';
Query OK, 0 rows affected (0.01 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.01 sec)

2. pip install mysql-connector-python-rf

"""

import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    auth_plugin='mysql_native_password'  # Specify the authentication plugin
)

# Check if the database connection is successful
if dataBase.is_connected():
    cursorObject = dataBase.cursor()
    cursorObject.execute("CREATE DATABASE spms_db")
    print("Database 'spms_db' created successfully!")

# Close the database connection
dataBase.close()
