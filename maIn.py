import json
import psycopg2
import functools
import operator
import pymongo

db_name = "dvdrental"
conn = psycopg2.connect(f"dbname={db_name} user=postgres password=alina", host="localhost", port=5433)
cursor = conn.cursor()

f = open('mongo.txt', 'w')
tables = ['actor', 'address', 'category', 'city', 'country', 'customer', 'film', 'film_actor', 'film_category',
          'inventory', 'language', 'payment', 'rental', 'staff', 'store']
for ta in tables:
    f.write("collection = db.get_collection('%s')\n" % ta)
    f.write("collection.insert_many([")
    sql1 = ('select * from %s) t' % ta)
    cursor.execute('SELECT row_to_json(t) FROM(' + sql1)
    n = 1
    for row in cursor:
        if n > 1:
            f.write(', ')
        j = json.dumps(functools.reduce(operator.add, row))
        f.write(j)
        n = n + 1
    f.write('])\n')
f.close()

client = pymongo.MongoClient("mongodb+srv://alina:Afanoz08@cluster0-blvuk.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('dvdrental')

f = open('mongo.txt', 'r')

null = None
false = False
true = True

while true:
    line = f.readline()
    if line != 'null':
        exec(line)
    else:
        break
    if not line:
        break
