import animal
import enclosure
import staff
import pytest

from animal import Mammals, Birds, ALLOWABLE_FOODS, REGISTERED_ANIMALS
from staff import Veterinarian


@pytest.fixture
def create_Vet1():
    return Veterinarian("Dr John Doolittle", "11/11/2025", ["penguins", "seals", "dolphins", "meerkats", "chimpanzees"])

@pytest.fixture
def create_Vet2():
    return Veterinarian("Dr Sarah Smith", "05/12/2024", ["penguins", "seals", "dolphins", "meerkats", "chimpanzees"])

@pytest.fixture
def create_Animal1():
    return Mammals("Zane the Zebra","zebra", 5, ["vegetables", "grass"],"savannah")

@pytest.fixture
def create_Animal2():
    return Birds("Mark the Macaw","macaw", 7, ["fruit", "meat"])



def test_veterinarian1(create_Vet1):
    assert create_Vet1.responsibilities == ["health checks", "treat animals", "move animals", "assign enclosure"]

def test_veterinarian2(create_Vet2):
    assert "meerkats" in create_Vet2.animals_can_treat
    assert "sharks" not in create_Vet2.animals_can_treat
    assert create_Vet2.name == "Dr Sarah Smith"
    assert create_Vet2.date_employed == "05/12/2024"

def test_animal1(create_Animal1):
    assert create_Animal1.health == 100
    assert create_Animal1.age == 5
    assert create_Animal1.name == "Zane the Zebra"
    assert "meat" not in create_Animal1.dietary_needs
    assert create_Animal1.make_sound() == "Zane the Zebra whinnies !"

def test_animal2(create_Animal2):
    given_foods = create_Animal2.dietary_needs
    for food in given_foods:
        assert food in ALLOWABLE_FOODS
    assert create_Animal2.species in REGISTERED_ANIMALS



