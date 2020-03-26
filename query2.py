import csv
import pymongo

client = pymongo.MongoClient("mongodb+srv://alina:Afanoz08@cluster0-blvuk.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('dvdrental')

file = open('query2.csv', 'w')

fieldnames = ['actor_id']
actor = db.actor.find()
for i in range(200):
    a = actor[i]
    fieldnames.append(a['actor_id'])
writer = csv.writer(file)
writer.writerow(fieldnames)

actor = db.actor.find()
films = []
for i in range(200):
    a = actor[i]
    films.append([])
    film_actor = db.film_actor.find({'actor_id': a['actor_id']})
    for f in film_actor:
        films[i].append(f['film_id'])

output = []
for i in range(200):
    output.append([])
    for k in range(200-i):
        n = 0
        for j in films[i]:
            for f in films[i+k]:
                if j == f:
                    n = n + 1
        output[i].append(n)
    for z in range(i):
        output[i].insert(z, output[z][i+1])
    output[i].insert(0, actor[i]['actor_id'])
writer.writerows(output)

