import pandas as pd
import matplotlib.pyplot as plt


# lendo as tabelas
details = pd.read_csv("desafio_details.csv")
priceav = pd.read_csv("desafio_priceav.csv")

# unindo os 2 arquivos .csv pela chave estrangeira 'airbnb_listing_id'
data_base = pd.merge(priceav, details, how = 'left', on = 'airbnb_listing_id')


# analise simples da relaçao dos detalhes dos listings com o faturamento
ordem_crescente_de_faturamento_por_number_of_bedrooms=data_base.groupby(['number_of_bedrooms'], as_index=False).sum().groupby('number_of_bedrooms')['price_string'].sum().sort_values()
ordem_crescente_de_faturamento_por_star_rating=data_base.groupby(['star_rating'], as_index=False).sum().groupby('star_rating')['price_string'].sum().sort_values()
ordem_crescente_de_faturamento_por_is_superhost=data_base.groupby(['is_superhost'], as_index=False).sum().groupby('is_superhost')['price_string'].sum().sort_values()
ordem_crescente_de_faturamento_por_number_of_reviews=data_base.groupby(['number_of_reviews'], as_index=False).sum().groupby('number_of_reviews')['price_string'].sum().sort_values()
ordem_crescente_de_faturamento_por_number_of_bathrooms=data_base.groupby(['number_of_bathrooms'], as_index=False).sum().groupby('number_of_bathrooms')['price_string'].sum().sort_values()


#salvando os dados em .csv
ordem_crescente_de_faturamento_por_number_of_bedrooms.to_csv("ordem_crescente_de_faturamento_por_number_of_bedrooms.csv")
ordem_crescente_de_faturamento_por_star_rating.to_csv("ordem_crescente_de_faturamento_por_star_rating.csv")
ordem_crescente_de_faturamento_por_is_superhost.to_csv("ordem_crescente_de_faturamento_por_is_superhost.csv")
ordem_crescente_de_faturamento_por_number_of_reviews.to_csv("ordem_crescente_de_faturamento_por_number_of_reviews.csv")
ordem_crescente_de_faturamento_por_number_of_bathrooms.to_csv("ordem_crescente_de_faturamento_por_number_of_bathrooms.csv")


######################### gerando os graficos #####################

# estilo dos graficos
plt.style.use("ggplot")


# passando os dados para gerar o grafico
plt.bar(ordem_crescente_de_faturamento_por_number_of_bedrooms.index.to_list(),ordem_crescente_de_faturamento_por_number_of_bedrooms.to_list(),color="green")
# legendas eixo X
plt.xticks(ordem_crescente_de_faturamento_por_number_of_bedrooms.index.to_list(),fontsize=7)
# legendas eixo Y
plt.ylabel("Faturamento")
# legendas eixo x
plt.xlabel("Quartos")
# titulo do grafico
plt.title("Ordem crescente de faturamento por quantidade de quartos")
# exibir grafico e salvar como imagem .png
fig = plt.gcf()
#plt.show()
fig.savefig('ordem_crescente_de_faturamento_por_number_of_bedrooms.png', format='png')


# passando os dados para gerar o grafico
plt.bar(ordem_crescente_de_faturamento_por_star_rating.index.to_list(),ordem_crescente_de_faturamento_por_star_rating.to_list(),color="green")
# legendas eixo X
plt.xticks(ordem_crescente_de_faturamento_por_star_rating.index.to_list(),fontsize=7)
# legendas eixo Y
plt.ylabel("Faturamento")
# legendas eixo x
plt.xlabel("Nota do anuncio")
# titulo do grafico
plt.title("Ordem crescente de faturamento por Nota do anuncio")
# exibir grafico e salvar como imagem .png
fig = plt.gcf()
#plt.show()
fig.savefig('ordem_crescente_de_faturamento_por_star_rating.png', format='png')


# passando os dados para gerar o grafico
plt.bar(ordem_crescente_de_faturamento_por_is_superhost.index.to_list(),ordem_crescente_de_faturamento_por_is_superhost.to_list(),color="green")
# legendas eixo X
plt.xticks(ordem_crescente_de_faturamento_por_is_superhost.index.to_list(),fontsize=7)
# legendas eixo Y
plt.ylabel("Faturamento")
# legendas eixo x
plt.xlabel("0=normal 1=superhost")
# titulo do grafico
plt.title("Ordem crescente de faturamento por superhost")
# exibir grafico e salvar como imagem .png
fig = plt.gcf()
#plt.show()
fig.savefig('ordem_crescente_de_faturamento_por_is_superhost.png', format='png')


# passando os dados para gerar o grafico
plt.bar(ordem_crescente_de_faturamento_por_number_of_reviews.index.to_list(),ordem_crescente_de_faturamento_por_number_of_reviews.to_list(),color="green")
# legendas eixo X
plt.xticks(ordem_crescente_de_faturamento_por_number_of_reviews.index.to_list(),fontsize=7)
# legendas eixo Y
plt.ylabel("Faturamento")
# legendas eixo x
plt.xlabel("Reviews")
# titulo do grafico
plt.title("Ordem crescente de faturamento por numero de reviews")
# exibir grafico e salvar como imagem .png
fig = plt.gcf()
#plt.show()
fig.savefig('ordem_crescente_de_faturamento_por_number_of_reviews.png', format='png')


# passando os dados para gerar o grafico
plt.bar(ordem_crescente_de_faturamento_por_number_of_bathrooms.index.to_list(),ordem_crescente_de_faturamento_por_number_of_bathrooms.to_list(),color="green")
# legendas eixo X
plt.xticks(ordem_crescente_de_faturamento_por_number_of_bathrooms.index.to_list(),fontsize=7)
# legendas eixo Y
plt.ylabel("Faturamento")
# legendas eixo x
plt.xlabel("Banheiros")
# titulo do grafico
plt.title("Ordem crescente de faturamento por numero de banheiros")
# exibir grafico e salvar como imagem .png
fig = plt.gcf()
#plt.show()
fig.savefig('ordem_crescente_de_faturamento_por_number_of_bathrooms.png', format='png')