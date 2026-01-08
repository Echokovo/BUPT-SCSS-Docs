import tinydb

db = tinydb.TinyDB('test.json')
db.insert({"index": 2, "data": {"t": 1, "b": 2}})
db.insert({"index": 1, "data": {"t": 1, "b": 2}})
for x in db.all():
    print(x)