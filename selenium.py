from selenium import webdriver
from selenium.webdriver.common.by import By

# Создание объекта ChromeOptions для дополнительных настроек браузера
options_chrome = webdriver.ChromeOptions()

# Добавление аргумента '--headless' для запуска браузера в фоновом режиме
options_chrome.add_argument('--headless')

# Инициализация драйвера Chrome с указанными опциями
# Использование менеджера контекста 'with' для автоматического закрытия браузера после выполнения кода
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/course/104774')
    browser.get(url)

    # Поиск элемента по уникальному идентификатору (id)
    element = browser.find_element(By.ID, "some_id")

    # Поиск элемента или элементов, используя селекторы CSS
    elements = browser.find_elements(By.CSS_SELECTOR, ".some_class")

    # Поиск элемента с помощью языка XPath
    element = browser.find_element(By.XPATH, "//div[@attribute='value']")

    # Поиск элемента по атрибуту name
    element = browser.find_element(By.NAME, "username")

    # Поиск элемента по названию HTML-тега
    images = browser.find_elements(By.TAG_NAME, "img")

    # Поиск элемента или элементов по классу
    buttons = browser.find_elements(By.CLASS_NAME, "btn")

    # Поиск элемента по точному тексту ссылки
    element = browser.find_element(By.LINK_TEXT, "Continue")

    # Поиск элемента по частичному тексту ссылки
    element = browser.find_element(By.PARTIAL_LINK_TEXT, "Cont")

    # найти один конкретный элемент на странице
    elements = browser.find_element(By.TAG_NAME, 'img')
    
    # получить список всех элементов
    elements = browser.find_elements(By.CLASS_NAME, 'some_class')

#-----------------------------------------------------------------------------
    # вернёт все найденные элементы <p>, расположенные на вторых позициях, во всех найденных <div class="text">
    p_elements = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")

    # или

    # 


driver.close() — закрывает текущее окно браузера, если во время работы вы открыли новое окно или вкладку.
driver.quit() — закрывает все окна, вкладки, процессы веб-драйвера, которые были запущены во время сессии.
