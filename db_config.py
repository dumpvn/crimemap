# -*- coding: utf-8 -*-

import pymysql
import dbconfig

connection = pymysql.connect(host=dbconfig.db_host,
                             user=dbconfig.db_user,
                             passwd=dbconfig.db_password)

try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS `%s`"
        cursor.execute(sql, (dbconfig.db_name))

        sql = """   CREATE TABLE IF NOT EXISTS `%s`.`crimes` (
                    `id` int NOT NULL AUTO_INCREMENT,
                    `latitude` FLOAT(10,6),
                    `longitude` FLOAT(10,6),
                    `date` DATETIME,
                    `category` VARCHAR(50),
                    `description` VARCHAR(1000),
                    `updated_at` TIMESTAMP,
                    PRIMARY KEY (`id`)
        )"""
        
        cursor.execute(sql, (dbconfig.db_name));
        connection.commit()
finally:
    connection.close()
