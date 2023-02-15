 # Projeto de Raspagem de Dados com Python
Este projeto tem como objetivo usar a linguagem Python para raspar dados e obter informações sobre domínios existentes no site registro.br

## Começando
Estas instruções servirão para que você obtenha uma cópia deste projeto e a utilize em seu ambiente local.

### Pré-requisitos
Você precisará ter os seguintes componentes instalados:

- Python 3.7 ou posterior
- Bibliotecas python: selenium, xlrd.

### Instalando
Para instalar as dependências deste projeto, você pode executar o seguinte script no seu terminal:


python3 -m pip install -r dev-requirements.txt


### Executando
Para executar este projeto, basta rodar o arquivo *main.py, passando um arquivo *.xlsx** contendo os nomes dos domínios que você deseja verificar como parâmetro. Por exemplo:


python main.py domains.xlsx


## Construído com
- [Selenium](https://www.selenium.dev) - Biblioteca usada para automatizar o navegador
- [Xlrd](http://www.python-excel.org/) - Biblioteca usada para ler/escrever arquivos Excel

## Autores
- Ranner de Paula - [GitHub](https://github.com/Ranner106)
