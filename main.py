# type: ignore
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import xlrd


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'driver' / 'chromedriver'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser

arq = open('domainsResult.txt', 'w')
dominios = []
#lendo do excel
workbook = xlrd.open_workbook('dominio.xls')
sheet = workbook.sheet_by_index(0)

for linha in range(0,10):
    dominios.append(sheet.cell_value(linha,0))


if __name__ == '__main__':
    TIME_TO_WAIT = 5
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://registro.br/')

   
    for dominio in dominios:
        search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'is-avail')
        )
        )
        search_input.clear()
        search_input.send_keys(dominio)
        search_input.send_keys(Keys.RETURN)
        sleep(TIME_TO_WAIT)
        results = browser.find_elements(By.TAG_NAME, 'strong')
        texto = "Domínio %s %s\n" % (dominio, results[4].text)
        arq.write(texto)

    arq.close()
    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)
