import pymongo
import time
start_time = time.time()

client = pymongo.MongoClient("mongodb+srv://alina:Afanoz08@cluster0-blvuk.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('dvdrental')

degrees = {}
actors = db.actor.find()
bacon = actors[1]
for a in actors:
    degrees[a['actor_id']] = 7
degrees.update({bacon['actor_id']: 0})
print(degrees)
checked_films = []
checked_actors = []


def find_degree(actor, d):
    if d > 2:
        return
    if checked_actors.count(actor['actor_id']) == 0:
        checked_actors.append(actor['actor_id'])
        films = db.film_actor.find({'actor_id': actor['actor_id']})
        for f in films:
            if checked_films.count(f['film_id']) == 0:
                checked_films.append(f['film_id'])
                a1 = db.film_actor.find({'film_id': f['film_id']})
                for aa in a1:
                    if degrees.get(aa['actor_id']) > d:
                        degrees.update({aa['actor_id']: d})
                    find_degree(aa, d+1)


find_degree(bacon,  1)
print(degrees)
