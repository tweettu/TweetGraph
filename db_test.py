from pattern.db import Database, field, pk, STRING, BOOLEAN, DATE, NOW, date,\
    MYSQL


db = Database(
    name = 'hootguy_tweetgraph',
    host = '50.87.144.127',
    port = 3306,
    username = 'hootguy_root',
    password = 'Sk1tterp0p'
    #, type = MYSQL
)

print db.tables
print db.relations
print db.query

db.create('chows', fields=[
    pk()
    , field('manufacturer', STRING(80))
    , field('brand', STRING(80), index=True)
    , field('price', INTEGER)
])

# db.create('pets', fields=[
#           pk(),
#           field('name', STRING(80), index=True),
#           field('type', STRING(20)),
#           field('tail', BOOLEAN),
#           field('date_birth', DATE, default=None),
#           field('date_created', DATE, default=NOW)
# ])

db.pets.append(name=u'Schroedinger', type='cat', tail=True)
db.pets.append(name=u'Caleb', type=u'hound', tail=True)

for i in range(0, 20):
    print db.pets.rows()[i]