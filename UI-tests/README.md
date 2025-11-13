# Дипломный проект. Задание 3: Автотесты для UI

### Студент: Родевич Анна

### <h>Когорта: FS-28</h>
<hr>

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

## Реализованные сценарии

### Проверка основной функциональности
`test_navigate_to_constructor` - переход по клику на «Конструктор»
`test_navigate_to_orders_feed` - переход по клику на раздел «Лента заказов»
`test_open_ingredient_popup` - если кликнуть на ингредиент, появится всплывающее окно с деталями
`test_close_ingredient_popup` - всплывающее окно закрывается кликом по крестику
`test_ingredient_counter_increases` - при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается

### Раздел «Лента заказов»
`test_orders_counter_increases_after_creating_new_order` - при создании нового заказа счётчик «Выполнено за всё время»/«Выполнено за сегодня» увеличивается (параметризированный)
`test_order_number_appears_in_progress_section_after_creation` - после оформления заказа его номер появляется в разделе «В работе»

## Структура проекта

- `pages/` — пакет с Page Object для UI-тестов
- `tests/` — пакет с тестами
- `conftest.py` — файл с фикстурами для авторизации, создания пользователей 
- `generators.py` - файл с функциями генерации данных для тестов
- `helper.py` - файл с вспомогательными функциями 
- `requirements.txt` - файл с зависимостями проекта 
- `urls.py` - файл с ссылками: UI (ссылки на страницы веб-приложения), API (эндпоинты для работы с заказами, пользователями, ингредиентами)

### Технологии

+ Python 3.13.5

+ Pytest

+ Selenium

+ Faker (для генерации тестовых данных)

+ WebDriverWait + Expected Conditions

+ Random (для генерации тестовых данных)

+ Allure (отчёты о тестировании)


### Запуск тестов

1. Клонировать репозиторий:<br/>
    ```git clone git@github.com:hradzevich/Diplom_3.git  ```

2. Установить зависимости:<br/>
    ```pip install -r requirements.txt```

3. Запустить тесты с сохранением результатов для Allure:<br/>
    ```pytest --alluredir=allure-results```

4. Сгенерировать html-отчёт в папку allure_report:<br/>
    ```allure generate allure-results -o allure_report --clean```

5. Открыть готовый отчёт в браузере:<br/>
    ```allure open allure_report```


### Полезные команды 

Очистить результаты прошлых запусков:<br/>
    ```rm -rf allure-results allure_report```

Перегенерировать отчёт без запуска тестов (если тесты уже запускались и в папке allure_results есть данные):<br/>
    ```allure generate allure-results -o allure_report --clean```
    ```allure open allure_report```

Быстрый просмотр отчёта без сохранения (отчёт откроется во временном режиме, готовая папка не создаётся):<br/>
    ```allure serve allure-results```
