import psycopg2

try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='35.239.229.146' password='health'")
except:
    print ("I am unable to connect to the database")

conn.autocommit = True
cur = conn.cursor()
