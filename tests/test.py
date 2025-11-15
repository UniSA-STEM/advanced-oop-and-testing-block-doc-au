import animal
import enclosure
import staff
import pytest

from animal import Mammals, Birds, ALLOWABLE_FOODS, REGISTERED_ANIMALS
from staff import Veterinarian
from enclosure import Enclosure


@pytest.fixture
def create_vet1():
    return Veterinarian("Dr John Doolittle", "11/11/2025", ["penguins", "seals", "dolphins", "meerkats", "chimpanzees"])

@pytest.fixture
def create_vet2():
    return Veterinarian("Dr Sarah Smith", "05/12/2024", ["penguins", "seals", "dolphins", "meerkats", "chimpanzees"])

@pytest.fixture
def create_animal1():
    return Mammals("Zane the Zebra","zebra", 5, ["vegetables", "grass"],"savannah")

@pytest.fixture
def create_animal2():
    return Birds("Mark the Macaw","macaw", 7, ["fruit", "vegetables"])

@pytest.fixture
def create_enclosure1():
    return Enclosure("A wet and dry space", 35, "amphibious")


def test_veterinarian1(create_vet1):
    assert create_vet1.responsibilities == ["health checks", "treat animals", "move animals", "assign enclosure"]

def test_veterinarian2(create_vet2):
    assert "meerkats" in create_vet2.animals_can_treat
    assert "sharks" not in create_vet2.animals_can_treat
    assert create_vet2.name == "Dr Sarah Smith"
    assert create_vet2.date_employed == "05/12/2024"

def test_animal1(create_animal1):
    assert create_animal1.health == 100
    assert create_animal1.age == 5
    assert create_animal1.name == "Zane the Zebra"
    assert "meat" not in create_animal1.dietary_needs
    assert create_animal1.make_sound() == "Zane the Zebra whinnies !"

def test_animal2(create_animal2):
    given_foods = create_animal2.dietary_needs
    for food in given_foods:
        assert food in ALLOWABLE_FOODS
    assert create_animal2.species in REGISTERED_ANIMALS
    assert create_animal2.make_sound() == "Mark the Macaw goes 'cheep cheep' !"

def test_enclosure_1(create_enclosure1):
    assert create_enclosure1.animal_count == 0
    assert create_enclosure1.name == "A wet and dry space"


