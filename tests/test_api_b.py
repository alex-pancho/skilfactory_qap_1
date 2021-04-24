import tools
from requests import get, post
import pytest
import json


def test_get_key_positive(testuser):
    headers = {
        "email": testuser["email"],
        "password": testuser["password"]
    }
    result = tools.point(get, "/api/key", headers=headers)
    result_json = result.json()
    assert result_json.get("key") is not None


@pytest.mark.usefixtures("signin")
def test_get_pets():
    result = tools.point(get, "/api/pets")
    result_json = result.json()
    assert result_json.get('pets') is not None, result

@pytest.mark.usefixtures("signin")
def test_post_pets():
    name = "Helen"
    animal_type = "ladybug"
    age = 12
    path_for_picture = "D:\\OneDrive\\Current_job\\api_qa_git\\testdata\\qa_180x180.jpg"
    data = {
        "name": name,
        "animal_type": animal_type,
        "age": age,
    }
    result = tools.point(post, "/api/pets", data=data, pet_photo=path_for_picture)
    result = result.json()
    assert result.get('name') == name, result
    assert result.get('animal_type') == animal_type
    assert result.get('age') == str(age)
    assert "data:image/jpeg;base64" in result.get('pet_photo')
