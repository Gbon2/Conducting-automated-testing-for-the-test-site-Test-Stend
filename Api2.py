import logging
import requests
import yaml

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Загрузка конфигурации
with open("config.yaml") as f:
    data = yaml.safe_load(f)

# Функция для выполнения теста API
def test_step1(login, testtext1):
    try:
        header = {"X-Auth-Token": login}
        res = requests.get(data["address"] + "api/posts", params={"owner": "notMe"}, headers=header)
        res.raise_for_status()  # Проверка на ошибки HTTP
        listres = [i["title"] for i in res.json()["data"]]
        assert testtext1 in listres
        logger.info("Тест успешно пройден: %s", testtext1)
    except requests.exceptions.RequestException as e:
        logger.error("Ошибка при выполнении запроса: %s", e)



if __name__ == "__main__":
    test_step1("example_login", "example_test_text")
