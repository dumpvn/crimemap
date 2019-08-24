# crime map

## quick start

```bash
pipenv shell
python crimemap.py
```

## setup

```bash
sudo apt-get update
sudo apt-get install mysql-server

pipenv install flask
pipenv install pymysql

```

**apache command**

```bash
sudo a2dissite headlines.conf
sudo a2ensite crimemap.conf
sudo service apache2 reload

tail –f /var/log/apache2/error.log
```
