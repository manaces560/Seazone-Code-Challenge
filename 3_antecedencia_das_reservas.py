import pandas as pd
import matplotlib.pyplot as plt


# lendo a tabela
priceav = pd.read_csv("desafio_priceav.csv")


##################### processando "priceav" linha por linha ######################
soma_instervalo_dias=0
dados_validos=0

dados_validos_fim_semana=0
soma_intervalo_dias_fim_semana=0

for n in range (len(priceav["booked_on"])):
    if priceav["booked_on"][n] != "blank":    # removendo as linhas em que "booked_on" esta como "blank"
        dados_validos=dados_validos+1         # contando as linhas validas para a media geral

        data_de_reserva = pd.to_datetime(priceav["booked_on"][n], format="%Y/%m/%d")
        data_da_reserva = pd.to_datetime(priceav["date"][n], format="%Y/%m/%d")

        soma_instervalo_dias = soma_instervalo_dias + abs((data_da_reserva - data_de_reserva).days)

        if data_da_reserva.weekday()==1 or data_da_reserva.weekday()==7:
            dados_validos_fim_semana=dados_validos_fim_semana+1 # contando as linhas validas para a media do fim de semana
            soma_intervalo_dias_fim_semana=soma_intervalo_dias_fim_semana +  abs((data_da_reserva - data_de_reserva).days)


antecedencia_media = soma_instervalo_dias/dados_validos # calculando a media das reservas
print("antecedencia media das reservas = ",int(antecedencia_media)," dias")

antecedencia_media_fim_semana = soma_intervalo_dias_fim_semana/dados_validos_fim_semana # calculando a media das reservas por fim de semana
print("antecedencia media das reservas para fim de semana = ",int(antecedencia_media_fim_semana)," dias")


#### gerando um arquivo com os resultados
resultado = open("antecedencia_das_reservas.csv","w")
resultado.write("antecedencia_media"+","+"antecedencia_media_f_semana"+"\n")
resultado.write(str(antecedencia_media)+","+str(antecedencia_media_fim_semana)+"\n")
resultado.close()


######################### gerando o grafico #####################

# criando o conjunto de dados
sizes=[antecedencia_media,antecedencia_media_fim_semana]

# area da plotagem
fig1, ax1 = plt.subplots()

# criando o grafico
ax1.pie(sizes,autopct='%1.1f%%',shadow=True, startangle=90)

# deixando o grafico circular
ax1.axis('equal')

# titulo do grafico
plt.title("Antecedência media ("+str(int(antecedencia_media))+"d)  X  Antecedência medio por fim de semana("+str(int(antecedencia_media_fim_semana))+"d)")

# exibir grafico e salvar como imagem .png
fig = plt.gcf()
plt.show()
fig.savefig('antecedencia_das_reservas.png', format='png')