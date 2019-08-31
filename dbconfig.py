import os

test = True

db_host = os.getenv('MYSQL_DB_HOST', 'localhost')
db_user = os.getenv('MYSQL_DB_USER', 'root')
db_password = os.getenv('MYSQL_DB_PASS', '123456')
db_name = os.getenv('MYSQL_DB_DB_NAME', 'crimemap')
