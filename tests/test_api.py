# импортируем библиотеку requests
import requests


def test_get_key():
    # задаем базовый урл
    baseurl = "https://petfriends1.herokuapp.com"
    # указываем заголовки, которые должны быть в запросе
    headers = {
        "email": "test@1secmail.com",
        "password": "test"
        }
    # указываем, куда обращен запрос
    endpoint = "/api/key"
    # с помощью библиотеки requests передаем все параметры и запишем результат в переменную res
    res = requests.get(baseurl+endpoint, headers=headers)
    # получаем тело ответа
    # сначала пробуем получить данные в формате json
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        # если данные в json не преобразовались, возвращаем как текст
        result = res.text
    print(result.get("key"))
    assert res.status_code == 200
    assert result.get("key") is not None


# вызываем функцию
test_get_key()