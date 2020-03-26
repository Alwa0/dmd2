import pymongo

client = pymongo.MongoClient("mongodb+srv://alina:Afanoz08@cluster0-blvuk.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('dvdrental')

film = db.film.find()
for f in film:
    n = 0
    inventory = db.inventory.find({'film_id': f['film_id']})
    for i in inventory:
        rental = db.rental.find({'inventory_id': i['inventory_id']})
        for r in rental:
            n = n + 1
    film_category = db.film_category.find({'film_id': f['film_id']})
    category = db.category.find({'category_id': film_category[0]['category_id']})
    print(f['title'] + " " + category[0]['name'] + " number of rents is "+"%s" % n)
