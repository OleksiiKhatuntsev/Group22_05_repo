from sql.alchemy.models.models import AddressModel
from sql.alchemy.session import session


class AddressRepository:
    def __init__(self):
        self.__session = session
        self.__model = AddressModel

    def get_all(self):
        addresses = self.__session.query(self.__model).all()
        return addresses

    def get_by_id(self, address_id: int) -> AddressModel:
        address: AddressModel | None = self.__session.get(self.__model, {'address_id': address_id})
        return address

    def create_new(self, address_model: AddressModel) -> bool:
        try:
            self.__session.add(address_model)
            return True
        except:
            return False

    def delete(self, id: int) -> bool:
        try:
            address = self.get_by_id(id)
            self.__session.delete(address)
            return True
        except:
            return False


    def update(self, address_model: AddressModel):
        self.__session.query(self.__model).filter(AddressModel.address_id == address_model.address_id).update({AddressModel.city: address_model.city, AddressModel.country: address_model.country})


if __name__ == '__main__':
    repo = AddressRepository()
    lviv = AddressModel()
    ternopil = AddressModel()
    lviv.city = "Lviv"
    ternopil.city = "Vinnytsia"
    lviv.country = "Ukraine"
    ternopil.country = "Ukraine"
    ternopil.address_id = 7
    # repo.create_new(lviv)
    # repo.delete(6)
    repo.update(ternopil)
    print(repo.get_all())
    print(repo.get_by_id(2))