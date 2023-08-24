import psycopg2


class BaseRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            user='postgres',
            password='admin',
            host='127.0.0.1',
            port='5432',
            database='group2005'
        )
        self.connection.set_session(autocommit=True)
        self._cursor = self.connection.cursor()
        
    
class AddressRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def get_all(self):
        self._cursor.execute("SELECT * FROM addresses")
        return self._cursor.fetchall()

    def insert_into(self, city, country):
        self._cursor.execute(f"INSERT INTO addresses (city, country) VALUES ('{city}', '{country}');")
        # self.connection.commit()

    def delete(self, id):
        self._cursor.execute(f"DELETE FROM addresses WHERE address_id={id};")
        # self.connection.commit()

if __name__ == '__main__':
    repo = AddressRepository()
    # repo.insert_into("Lviv", "Ukraine")
    repo.delete(5)
    print(repo.get_all())
