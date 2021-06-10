import pandas as pd
import matplotlib.pyplot as plt


# lendo as tabelas
details = pd.read_csv("desafio_details.csv")
priceav = pd.read_csv("desafio_priceav.csv")

# unindo os 2 arquivos .csv pela chave estrangeira 'airbnb_listing_id'
data_base = pd.merge(priceav, details, how = 'left', on = 'airbnb_listing_id')
# deletando os dias em que nao estava ocupado
data_base = data_base.drop(data_base[data_base.occupied == 0].index)


# ordenando os bairros em ordem crescente de faturamneto medio
bairros_em_ordem_crescente_de_faturamento_medio=data_base.groupby(['suburb'], as_index=False).mean().groupby('suburb')['price_string'].mean().sort_values()
print(bairros_em_ordem_crescente_de_faturamento_medio)

bairros_em_ordem_crescente_de_faturamento_medio.to_csv("bairros_em_ordem_crescente_de_faturamento_medio.csv")


######################### gerando o grafico #####################

# estilo de grafico
plt.style.use("ggplot")

# passando os dados para gerar o grafico
plt.bar(bairros_em_ordem_crescente_de_faturamento_medio.index.to_list(),bairros_em_ordem_crescente_de_faturamento_medio.to_list(),color="green")

# legendas eixo X
plt.xticks(bairros_em_ordem_crescente_de_faturamento_medio.index.to_list(),fontsize=7)

# legendas eixo Y
plt.ylabel("Faturamento")

# legendas eixo x
plt.xlabel("Bairros")

# titulo do grafico
plt.title("Bairros em ordem crescente de faturamento medio")

# exibir grafico e salvar como imagem .png
fig = plt.gcf()
plt.show()
fig.savefig('bairros_em_ordem_crescente_de_faturamento_medio.png', format='png')