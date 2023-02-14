 # Projeto de Raspagem de Dados com Python
Este projeto tem como objetivo usar a linguagem Python para raspar dados e obter informações sobre domínios existentes no site registro.com.

## Começando
Estas instruções servirão para que você obtenha uma cópia deste projeto e a utilize em seu ambiente local.

### Pré-requisitos
Você precisará ter os seguintes componentes instalados:

- Python 3.7 ou posterior
- Bibliotecas python: selenium, xlrd, beautifil soup

### Instalando
Para instalar as dependências deste projeto, você pode executar o seguinte script no seu terminal:


pip install -r requirements.txt


### Executando
Para executar este projeto, basta rodar o arquivo *main.py, passando um arquivo *.xlsx** contendo os nomes dos domínios que você deseja verificar como parâmetro. Por exemplo:


python main.py domains.xlsx


## Construído com
- [Selenium](https://pypi.org/project/selenium/) - Biblioteca usada para automatizar o navegador
- [Xlrd](https://xlrd.readthedocs.io/en/latest/) - Biblioteca usada para ler/escrever arquivos Excel
- [Beautifil Soup] (https://beautiful-soup-4.readthedocs.io/en/latest/) - Biblioteca usada para extrair dados de arquivos HTML e XML

## Autores
- Ranner de Paula - [GitHub](https://github.com/rannerdepaula)
