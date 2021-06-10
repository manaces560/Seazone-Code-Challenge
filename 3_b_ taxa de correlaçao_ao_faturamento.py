import pandas as pd
import matplotlib.pyplot as plt


# lendo as tabelas
details = pd.read_csv("desafio_details.csv")
priceav = pd.read_csv("desafio_priceav.csv")

# unindo os 2 arquivos .csv pela chave estrangeira 'airbnb_listing_id'
data_base = pd.merge(priceav, details, how = 'left', on = 'airbnb_listing_id')
# deletando os dias em que nao estava ocupado
data_base = data_base.drop(data_base[data_base.occupied == 0].index)

#calculando faturamento por listing
faturamento=data_base.groupby(['airbnb_listing_id'], as_index=False).sum().groupby('airbnb_listing_id')['price_string'].sum()

# unindo o faturamneto aos detalher de cada listing
data_base = pd.merge(faturamento, details, how = 'left', on = 'airbnb_listing_id')

# salvando listings com faturameto
data_base.to_csv("details_com_faturamento.csv")

#calcupalndo a correlaçao estre as colunas da tabela ao faturamneto
correlacao=data_base.corr().price_string

# salvando correlação dos elementos com o faturameto
data_base.to_csv("correlacao_com_faturamento.csv")

######################### gerando o grafico #####################

# estilo dos graficos
plt.style.use("ggplot")


# passando os dados para gerar o grafico
plt.barh(correlacao.index.to_list(),correlacao.to_list(),color="green")
# legendas eixo X
#plt.xticks(correlacao.index.to_list(),fontsize=7)
# legendas eixo Y
plt.ylabel("Indice de correlaçãoElementos do banco de dados")
# legendas eixo x
plt.xlabel("Indice de correlação")
# titulo do grafico
plt.title("Correlaçao dos elementos do banco de dados ao faturamento")
# exibir grafico e salvar como imagem .png
fig = plt.gcf()
plt.show()
fig.savefig('Correlacao_com_faturamento.png', bbox_extra_artists=(), bbox_inches='tight')