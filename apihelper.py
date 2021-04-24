import requests
import json
import base64


baseurl = "https://petfriends1.herokuapp.com"
apikey = ""
user = {
    "email": "test@1secmail.com",
    "password": "test"
    }


def get_apikey(email: str, password: str) -> json:
    """Get API key.
       Awaiting email: str and password: str - registered user data"""
    # добавляем заголовки
    headers = {
        "email": email,
        "password": password
    }
    # указываем, куда обращен запрос
    endpoint = "/api/key"
    # с помощью библиотеки requests передаем все параметры в гет-запросе
    # и запишем результат в переменную res
    res = requests.get(baseurl + endpoint, headers=headers)
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return result


def login(user: dict):
    result = get_apikey(user["email"], user["password"])
    if "key" in result:
        global apikey
        apikey = result.get("key")
    else:
        raise Exception("[key] not found, we have: \n" + str(result))


def get_pets(filter: str = "") -> json:
    """Returns all pets.
       With filter="my_pets" returns only pets for current user"""
    # добавляем заголовок - ключ апи
    headers = {
        "auth_key": apikey,
    }
    query = {
        "filter": filter
    }
    # указываем, куда обращен запрос
    endpoint = "/api/pets"
    # с помощью библиотеки requests передаем все параметры в гет-запросе
    # и запишем результат в переменную res
    res = requests.get(baseurl + endpoint, params=query, headers=headers)
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return result

def post_pets(name: str, animal_type: str, age: int, pet_photo: str):
    """Add new pet.
       pet_photo - path for jpeg picture.
       All fields is required"""
    # добавляем заголовок - ключ апи
    headers = {
        "auth_key": apikey,
    }
    # кодируем изображение в формат base64
    # 1. читаем изображение
    pic = open(pet_photo, "rb").read()
    # 2. кодируем изображение
    b64pic = base64.b64encode(pic).decode()
    # 3. добавляем служебную информацию
    pet_pic = 'data:image/jpeg;base64,' + b64pic
    # 4. результат в виде словаря запишем в переменную file
    file = {"pet_photo": pet_pic}
    # собираем остальные параметры в словарь
    formdata = {
        "name": name,
        "animal_type": animal_type,
        "age": age,
    }
    # указываем, куда обращен запрос
    endpoint = "/api/pets"
    # с помощью библиотеки requests передаем все параметры в пост-запросе
    # и запишем результат в переменную res
    res = requests.post(baseurl + endpoint, data=formdata, files=file, headers=headers)
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return result


if __name__ == '__main__':
    login(user)
    pets = post_pets("aaa", "kat", 12, "D:\\OneDrive\\Current_job\\api_qa_git\\testdata\\qa_180x180.jpg")
    print(pets)
