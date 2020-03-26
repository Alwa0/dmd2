import pymongo

client = pymongo.MongoClient("mongodb+srv://alina:Afanoz08@cluster0-blvuk.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('dvdrental')

max = db.rental.aggregate(
    [
        {
            "$group": {
                "_id": {

                },
                "MAX(rental_date)": {
                    "$max": "$rental_date"
                }
            }
        },
        {
            "$project": {
                "MAX(rental_date)": "$MAX(rental_date)",
                "_id": int(0)
            }
        }
    ]
)
current_year = list(max)[0]['MAX(rental_date)'][0:4]
print("Current year is: "+current_year)

customer = db.customer.find()
for c in customer:
    categories = []
    rental = db.rental.find({'customer_id': c['customer_id']})
    for r in rental:
        if r['rental_date'][0:4] == current_year:
            inventory = db.inventory.find({'inventory_id': r['inventory_id']})
            for i in inventory:
                film_category = db.film_category.find({'film_id': i['film_id']})
                for fc in film_category:
                    if len(categories) == 0:
                        categories.append(fc['category_id'])
                    else:
                        if categories[0] != fc['category_id']:
                            categories.append(fc['category_id'])
    if len(categories) > 1:
        print("%s " % c['customer_id'] + c['first_name'] + " " + c['last_name'])


