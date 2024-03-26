from selenium import webdriver
from selenium.webdriver.common.by import By

# Создание объекта ChromeOptions для дополнительных настроек браузера
options_chrome = webdriver.ChromeOptions()

# Добавление аргумента '--headless' для запуска браузера в фоновом режиме
options_chrome.add_argument('--headless')
#  отключает использование графического процессора для рендеринга, что может быть полезным на машинах с проблемными или отсутствующими графическими драйверами
options_chrome.add_argument('--disable-gpu')
# если вам потребуется запустить браузер в режиме --headless и с расширениями(используются для модификации поведения браузера)
options_chrome.add_argument('--headless=chrome')
options_chrome.add_extension('coordinates.crx')
# Перенос профиля пользователя из основного браузера Chrome в браузер, управляемый через Selenium
options_chrome.add_argument('user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data')
# запрос через прокси
chrome_options.add_argument('--proxy-server=%s' % proxy)
# Запускает браузер без дополнительных мер безопасности
options.add_argument('--no-sandbox')  
# Запускает браузер в режиме инкогнито. В этом режиме не сохраняются куки и история просмотров
options.add_argument('--incognito')
# Устанавливает начальный размер окна браузера
options.add_argument('--window-size=width,height')
# Запускает браузер на весь экран
options.add_argument('--start-maximized')
# Отключает все установленные расширения
options.add_argument('--disable-extensions')
# Устанавливает директорию для хранения профиля пользователя
options.add_argument('Устанавливает директорию для хранения профиля пользователя')
# Убирает информационные строки в верхней части окна
options.add_argument('--disable-infobars')
# Игнорирует ошибки SSL-сертификатов. Полезно, если нужно обращаться к сайтам с недействительными сертификатами
options.add_argument('--ignore-certificate-errors')
# Устанавливает язык интерфейса браузера на русский
options.add_argument('--lang=ru')
# Отключает блокировку всплывающих окон. Может быть полезным при автоматизации некоторых сценариев
options.add_argument('--disable-popup-blocking')
# Позволяет загружать небезопасный контент на страницы, загруженные по HTTPS. Опасная опция, используйте с осторожностью
options.add_argument('--allow-running-insecure-content')
# Отключает уведомления браузера. Особенно полезно при автоматизированном тестировании
options.add_argument('--disable-notifications')
# Отключает меры безопасности веба. Не рекомендуется для обычного просмотра, но может быть полезно для тестирования
options.add_argument('--disable-web-security')
# Отключает обнаружение фишинга на клиентской стороне
options.add_argument('--disable-client-side-phishing-detection')
# Включает журналирование в файл
options.add_argument('--enable-logging')
# Устанавливает уровень журналирования (0-3)
options.add_argument('--log-level=0')
# Отключает кэш браузера. Полезно для тестирования изменений на веб-страницах в реальном времени
options.add_argument('--disable-cache')
# Подсказывает браузеру, что он управляется программой. Это может изменить поведение некоторых веб-сайтов
options.add_argument('--enable-automation')
# Отключает песочницу безопасности для браузера. Также не рекомендуется для обыденного использования
options.add_argument('--disable-setuid-sandbox')
# Отключает синхронизацию с аккаунтом Google
options.add_argument('--disable-sync')


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
    # Проходимся по списку найденных элементов и выводим их текст
    for i, p_element in enumerate(p_elements):
 
    # или

    # Ищем все div с классом 'text'
    divs = browser.find_elements(By.CLASS_NAME, 'text')
    # Проходимся по каждому div
    for i, div in enumerate(divs):
        # Получаем первый и третий теги <p> внутри каждого div
        first_p = div.find_element(By.XPATH, './p[1]')
        third_p = div.find_element(By.XPATH, './p[3]')
#-----------------------------------------------------------------------------     

# вернуться на предыдущую страницу
webdriver.back()
# перемещает вперёд по истории браузера
webdriver.forward()
# обновляет текущую страницу
webdriver.refresh()

# Сохраняет скриншот страницы в файл по указанному пути (возвращает True, False)
webdriver.get_screenshot_as_file("../file_name.jpg")
# Сохраняет скриншот в папке с проектом
webdriver.save_screenshot("file_name.jpg")
# Возвращает скриншот в виде двоичных данных
webdriver.get_screenshot_as_png()
# Возвращает скриншот в виде строки в кодировке Base64
webdriver.get_screenshot_as_base64()

# Открывает указанный URL в браузере
webdriver.get("http://example_url.ru")
# Закрывает все вкладки и окна, завершает процесс драйвера
webdriver.quit()
# Закрывает только текущую вкладку
webdriver.close()
 
# Устанавливает таймаут на загрузку страницы. Выбрасывает исключение, если время вышло
webdriver.set_page_load_timeout() 
 
# Возвращает первый найденный элемент по заданному локатору
webdriver.find_element(By.ID, 'example_id') 
# Возвращает список всех элементов, соответствующих локатору
webdriver.find_elements(By.ID, 'example_id') 
 
#  Возвращает словарь с текущей позицией окна браузера ({'x': 10, 'y': 50})
webdriver.get_window_position()
# Разворачивает окно на весь экран
webdriver.maximize_window() 

# Сворачивает окно.
webdriver.minimize_window() 

# Переводит окно в полноэкранный режим, как при нажатии F11
webdriver.fullscreen_window()  
# Возвращает размер окна в виде словаря ({'width': 945, 'height': 1020})
webdriver.get_window_size() 
# Устанавливает новый размер окна
webdriver.set_window_size(800,600) 
 
# Возвращает список всех cookies
webdriver.get_cookies() 
# Возвращает конкретную cookie по имени
webdriver.get_cookie(name_cookie) 

# Добавляет новую cookie к вашему текущему сеансу----------------
webdriver.add_cookie(cookie_dict)

cookie_dict = {
    'name': 'any_name_cookie',    # Любое имя для cookie
    'value': 'any_value_cookie',  # Любое значение для cookie
    'expiry': 2_000_000_000,      # Время жизни cookie в секундах
    'path': '/',                  # Директория на сервере дял которой будут доступны cookie
    'domain': 'parsinger.ru',     # Информация о домене и поддомене для которых доступны cookie
    'secure': True,  # or False   # Сигнал браузера о том что передать cookie только по защищённому HTTPS
    'httpOnly': True,  # or False # Ограничивает достук к cookie по средствам API
    'sameSite': 'Strict',  # or lax or none # Ограничение на передачу cookie между сайтами
}
webdriver.add_cookie(cookie_dict)
pprint(webdriver.get_cookies())
#----------------------------------------------------------------
# Удаляет cookie по имени
webdriver.delete_cookie(name_cookie)
# удаляет все файлы cookie в рамках текущего сеанса
webdriver.delete_all_cookies() 
 
# Устанавливает неявное ожидание на поиск элементов или выполнение команд
webdriver.implicitly_wait(10)
webdriver.WebDriverWait(driver, timeout).until(condition)

# Симулирует клик по элементу
element.click() 
# Вводит текст в текстовое поле
element.send_keys("text")
# Очищает текстовое поле
element.clear()
# Проверяет, отображается ли элемент на странице
element.is_displayed() 
# Проверяет, доступен ли элемент для взаимодействия (например, не заблокирован)
element.is_enabled() 
# Проверяет, выбран ли элемент (актуально для радиокнопок и чекбоксов)
element.is_selected() 
# Возвращает значение указанного атрибута элемента
element.get_attribute("attribute") 
# Возвращает текст элемента
element.text 
# Отправляет форму, в которой находится элемент
element.submit() 

# Переключает фокус на указанный фрейм
webdriver.switch_to.frame("frame_name") 
# Возвращает фокус на основное содержимое страницы, выходя из фрейма
webdriver.switch_to.default_content() 

# Переключает фокус на всплывающее окно JavaScript
webdriver.switch_to.alert 

# Cookie-------------------------------------------------------
# Добавляет новую cookie к вашему текущему сеансу
webdriver.add_cookie(cookie_dict)

cookie_dict = {
    'name': 'any_name_cookie',    # Любое имя для cookie
    'value': 'any_value_cookie',  # Любое значение для cookie
    'expiry': 2_000_000_000,      # Время жизни cookie в секундах
    'path': '/',                  # Директория на сервере дял которой будут доступны cookie
    'domain': 'parsinger.ru',     # Информация о домене и поддомене для которых доступны cookie
    'secure': True,  # or False   # Сигнал браузера о том что передать cookie только по защищённому HTTPS
    'httpOnly': True,  # or False # Ограничивает достук к cookie по средствам API
    'sameSite': 'Strict',  # or lax or none # Ограничение на передачу cookie между сайтами
}
webdriver.add_cookie(cookie_dict)
pprint(webdriver.get_cookies())


# Удаляет cookie по имени
webdriver.delete_cookie(name_cookie)
# удаляет все файлы cookie в рамках текущего сеанса
webdriver.delete_all_cookies() 
# -------------------------------------------------------------

# JavaScript---------------------------------------------------
# Выполняет JavaScript код на текущей странице
webdriver.execute_script("script_code") 
# Асинхронно выполняет JavaScript код. Удобно для работы с AJAX и промисами
webdriver.execute_async_script("script_code" , *args )
# прокручивает родительский контейнер элемента таким образом, чтобы element, для которого вызывается scrollIntoView, был виден пользователю.
webdriver.execute_script("return arguments[0].scrollIntoView(true);", element) 
# создаст новую вкладку в браузере с именем "tab2"
webdriver.execute_script("window.open('http://parsinger.ru', 'tab2');")
# вернёт значение высоты элемента <body>
webdriver.execute_script("return document.body.scrollHeight") 
# вернёт значение ширины окна браузера
webdriver.execute_script("return window.innerWidth") 
# прокрутит документ на заданное число пикселей по осям X и Y
webdriver.execute_script("window.scrollBy(X, Y)")
# вызывает модальное окно Alert
webdriver.execute_script("alert('Ура Selenium')")
# возвращает title открытого документа
webdriver.execute_script("return document.title;")
# возвращает URL документа
webdriver.execute_script("return document.documentURI;") 
# возвращает состояние загрузки страницы; вернёт "complete", если страница загрузилась
webdriver.execute_script("return document.readyState;")
# возвращает список всех якорей на странице
webdriver.execute_script("return document.anchors;")
# этот код позволяет получить список всех тегов с якорями. Очень полезная инструкция, особенно если при скроллинге элемент для "зацепления" не найден
[x.tag_name for x in browser.execute_script("return document.anchors;")]
# возвращает строку, содержащую все cookies документа, разделённые точкой с запятой
webdriver.execute_script("return document.cookie;")
# возвращает домен текущего документа
webdriver.execute_script("return document.domain;") 
# возвращает список всех форм на странице
webdriver.execute_script("return document.forms;")
# прокручивает документ до указанных координат
webdriver.execute_script("window.scrollTo(x-coord, y-coord);")
# возвращает список всех элементов с классом 'container'
webdriver.execute_script("return document.getElementsByClassName('container');") 
# возвращает список всех элементов с тегом 'container'
webdriver.execute_script("return document.getElementsByTagName('container');")  
# возвращает элемент с указанным ID 'some-id'
webdriver.execute_script("return document.getElementById('some-id');") 
# -------------------------------------------------------------------
