import apihelper
import pytest


def test_get_key_positive(testuser):
    result = apihelper.get_apikey(testuser["email"], testuser["password"])
    assert result.get("key") is not None

@pytest.mark.usefixtures("authenticate")
def test_get_pets():
    result = apihelper.get_pets()
    assert result.get('pets') is not None, result

@pytest.mark.usefixtures("authenticate")
def test_post_pets():
    name = "Helen"
    animal_type = "ladybug"
    age = 12
    path_for_picture = "D:\\OneDrive\\Current_job\\api_qa_git\\testdata\\qa_180x180.jpg"
    result = apihelper.post_pets(name, animal_type, age, path_for_picture)
    assert result.get('name') == name
    assert result.get('animal_type') == animal_type
    assert result.get('age') == str(age)
    assert "data:image/jpeg;base64" in result.get('pet_photo')