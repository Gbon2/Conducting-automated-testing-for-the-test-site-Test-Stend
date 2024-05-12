import pytest
import logging
import yaml
import requests


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def login():
    try:
        res = requests.post(data["address"] + "gateway/login", data={"username": data["username"], "password": data["password"]})
        res.raise_for_status()  # Проверка на ошибки HTTP
        token = res.json()["token"]
        logger.info("Успешная авторизация")
        return token
    except requests.exceptions.RequestException as e:
        logger.error("Ошибка при авторизации: %s", e)



@pytest.fixture()
def testtext1():
    return "test"


def test_example(login, testtext1):
    try:
        header = {"X-Auth-Token": login}
        res = requests.get(data["address"] + "api/posts", params={"owner": "notMe"}, headers=header)
        res.raise_for_status()
        listres = [i["title"] for i in res.json()["data"]]
        assert testtext1 in listres
        logger.info("Тест успешно пройден: %s", testtext1)
    except requests.exceptions.RequestException as e:
        logger.error("Ошибка при выполнении запроса: %s", e)


if __name__ == "__main__":
    pytest.main([__file__])
