# Diplom_1
Дипломный проект. Юнит-тесты

Stellar Burgers — это внеземной фастфуд, где можно создать свой бургер. 

Реализованные сценарии
В рамках выполнения работы нужно было покрыть юнит-тестами классы Bun, Burger, Ingredient и Database.

Структура проекта:
1. praсtiсum — пакет, содержащий оригинальный код программы;
2. tests — директория, в которой находяся тесты, разделенные по классам: test_bun.py, test_burger.py, test_database.py, test_ingredient.py;
3. Папка allure_results содержит JSON-файлы с результатами выполнения тестов;
4. Файл conftest содержит фикстуры, необходимые для запуска тестов;
5. Файл data содержит тестовые данные;
6. В файле requirements.txt перечислены все внешние зависимости исполняемых тестов для удобной установки одной командой;
7. Папка cov_html - отчет по результатам тестового покрытия

Установка зависимостей
$ pip install -r requirements.txt

Запуск автотестов и создание HTML-отчета о покрытии
$ pytest --cov --cov-report=html:cov_html

Allure-отчет о тестировании в формате веб-страницы
allure serve allure_results