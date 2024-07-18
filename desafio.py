# formular perguntas --------------
# o valor é o mesmo em todas as regiôes?
# qual a classe social do publico de tal região?
# a oferta é a mesma da demanda?

from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt  
import statistics



url = 'https://bea3853.github.io/site_teste/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
dados = soup.find('table')

linhas = dados.find_all('tr')[1:]
nomes = []
compras = []
regiao = []

for linha in linhas:
    n = linha.find_all('td') 
    nomes.append(n[0].text)
    compras.append(int(n[1].text))
    regiao.append(n[2].text)


moda = statistics.mode(compras)
print('moda:' , moda)
mediana = statistics.median(compras)
print('mediana:' , mediana)
desvio = statistics.stdev(compras)
print('desvio:', desvio)
amplitude = statistics.pvariance(compras)
print('amplitude:', amplitude)


def barras():
    plt.bar(compras, regiao)
    plt.show()
barras()

def reto():
    plt.plot(compras, regiao)
    plt.show()
reto()