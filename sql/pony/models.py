from pony.orm import Database, PrimaryKey, Required, Set

db = Database()
db.bind(provider='postgres', user='postgres', password='admin', host='127.0.0.1', database='group2005')


class Address(db.Entity):
    _table_ = 'addresses'
    address_id = PrimaryKey(int, auto=True)
    city = Required(str, 100)
    country = Required(str, 100)
    users = Set("User")


class User(db.Entity):
    _table_ = "users"
    id = PrimaryKey(int, auto=True)
    age = Required(int)
    name = Required(str, 100)
    address = Required(Address, column='address_id')

db.generate_mapping()

