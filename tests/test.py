import animal
import enclosure
import staff
import pytest

from animal import Mammal
from staff import Veterinarian


@pytest.fixture
def create_Vet1():
    return Veterinarian("Dr John Doolittle", "11/11/2025", ["penguins", "seals", "dolphins", "meerkats", "chimpanzees"])

@pytest.fixture
def create_Vet2():
    return Veterinarian("Dr Sarah Smith", "05/12/2024", ["penguins", "seals", "dolphins", "meerkats", "chimpanzees"])

@pytest.fixture
def create_Animal1():
    return Mammal("Dave the Donkey","donkey", 5, ["vegetables", "grass"],"savannah")





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
    assert create_Animal1.name == "Dave the Donkey"
    assert "meat" not in create_Animal1.dietary_needs


