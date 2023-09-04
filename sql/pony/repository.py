from pony.orm import db_session, select
from models import User, Address


class UserRepo:
    def __init__(self):
        self.model = User


    @db_session
    def get_by_id(self, id):
        user = self.model.get(lambda u: u.id == id)
        return user


class AddressRepo:
    def __init__(self):
        self.model = Address


    @db_session
    def get_by_id(self, id):
        user = self.model.get(lambda u: u.address_id == id)
        return user


if __name__ == '__main__':
    repo = AddressRepo()
    user = repo.get_by_id(1)
    print(user)