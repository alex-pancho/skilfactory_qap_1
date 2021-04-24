from requests import get, post
import json
import base64


baseurl = "https://petfriends1.herokuapp.com"
apikey = ""
user = {
    "email": "test@1secmail.com",
    "password": "test"
    }


def point(method, pointname, params={}, data={}, headers={}, pet_photo=None, auth=True):
    if apikey != "" and auth:
        headers.update({"auth_key": apikey})

    if pet_photo is not None:
        # 1. читаем изображение
        pic = open(pet_photo, "rb").read()
        # 2. кодируем изображение
        b64pic = base64.b64encode(pic).decode()
        # 3. добавляем служебную информацию
        pet_pic = 'data:image/jpeg;base64,' + b64pic
        # 4. результат в виде словаря запишем в переменную file
        file = {"pet_photo": pet_pic}
        res = method(baseurl + pointname, params=params, files=file, data=data, headers=headers)
    else:
        res = method(baseurl + pointname, params=params, data=data, headers=headers)
    return res


def get_apikey(email: str, password: str) -> json:
    """Get API key.
       Awaiting email: str and password: str - registered user data"""
    # добавляем заголовки
    headers = {
        "email": email,
        "password": password
    }
    # с помощью  передаем все параметры в гет-запросе
    # и запишем результат в переменную res
    res = point(get, "/api/key", headers=headers)
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
