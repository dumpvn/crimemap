# -*- coding: utf-8 -*-
"""

References:
    - Connection object: https://pymysql.readthedocs.io/en/latest/modules/connections.html
"""
import sys
import pymysql
import dbconfig

connection = pymysql.connect(host=dbconfig.db_host,
                             user=dbconfig.db_user,
                             password=dbconfig.db_password,
                             database=dbconfig.db_name)

if not connection.open:
    print('Cannot connect to {host} using {user}'.format(host=dbconfig.db_host, user=dbconfig.db_user))
    sys.exit(-1)

try:
    # sql = "CREATE DATABASE IF NOT EXISTS %s"

    with connection.cursor() as cursor:
        # cursor.execute(sql, (dbconfig.db_name))

        sql = """   CREATE TABLE IF NOT EXISTS crimes (
                    id int NOT NULL AUTO_INCREMENT,
                    latitude FLOAT(10,6),
                    longitude FLOAT(10,6),
                    date DATETIME,
                    category VARCHAR(50),
                    description VARCHAR(1000),
                    updated_at TIMESTAMP,
                    PRIMARY KEY (id)
        )"""
        
        cursor.execute(sql);
        connection.commit()
finally:
    connection.close()
