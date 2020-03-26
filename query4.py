import pymongo

client = pymongo.MongoClient("mongodb+srv://alina:Afanoz08@cluster0-blvuk.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('dvdrental')


customer = db.customer.find()
films = []
for ic in range(599):
    c = customer[ic]
    films.append([])
    rental = db.rental.find({'customer_id': c['customer_id']})
    for r in rental:
        inventory = db.inventory.find({'inventory_id': r['inventory_id']})
        for i in inventory:
            films[ic].append(i['film_id'])

output = []
for i in range(599):
    output.append([])
    for k in range(599-i):
        n = 0
        for j in films[i]:
            for f in films[i+k]:
                if j == f:
                    n = n + 1
        output[i].append(n)
    for z in range(i):
        output[i].insert(z, output[z][i])

for i in range(599):
    rec_film = None
    metric = 0
    maximum = 0
    for j in range(599):
        if i != j:
            if output[i][j] > maximum:
                maximum = output[i][j]
                rec_customer = customer[j]
                for film in films[j]:
                    if films[i].count(film) == 0:
                        rec_film = film
                        metric = maximum/len(films[i])
                        break
    print('for customer %s ' % customer[i]['customer_id'] + 'recommended film is ' + str(rec_film)
          + ' with recommendation metric ' + str(metric))
