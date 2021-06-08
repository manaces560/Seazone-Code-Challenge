import pandas as pd
import matplotlib.pyplot as plt


# lendo a tabela
details = pd.read_csv("desafio_details.csv")

# ordenando os bairros em ordem crescente de listings
bairros_em_ordem_crescente_de_listings= details.groupby("suburb").size().sort_values()
print(bairros_em_ordem_crescente_de_listings)

# salvando em um .csv
bairros_em_ordem_crescente_de_listings.to_csv("bairros_em_ordem_crescente_de_listings.csv")


######################### gerando o grafico #####################

# estilo de grafico
plt.style.use("ggplot")

# passando os dados para gerar o grafico
plt.bar(bairros_em_ordem_crescente_de_listings.index.to_list(),bairros_em_ordem_crescente_de_listings.to_list(),color="green")

# legendas eixo X
plt.xticks(bairros_em_ordem_crescente_de_listings.index.to_list(),fontsize=7)

# legendas eixo Y
plt.ylabel("Listings")

# legendas eixo x
plt.xlabel("Bairros")

# titulo do grafico
plt.title("Bairros em ordem crescente de listings")

# exibir grafico e salvar como imagem .png
fig = plt.gcf()
plt.show()
fig.savefig('bairros_em_ordem_crescente_de_listings.png', format='png')