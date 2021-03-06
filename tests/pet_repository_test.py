from faker import Faker
from src.infra.db.config import DBConnectionHandler
from src.infra.db.repo.pet_repository import PetRepository


fake = Faker()
pet_repository = PetRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_pet():
    db_connection_handler.create_db_and_tables()

    name = fake.name()
    species = "dog"
    user_id = 1

    pet = pet_repository.insert_pet(name, species, user_id)
    query_pet = pet_repository.get_pet_by_id(pet.id)

    assert pet.name == query_pet.name
    assert pet.specie == query_pet.specie
    assert pet.user_id == query_pet.user_id

    pet_repository.delete_pet_by_id(pet_id=pet.id)
