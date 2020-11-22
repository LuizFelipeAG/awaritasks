# Importar pacotes necessarios
from time import sleep
from whatsapp_api import WhatsApp
import pandas as pd

# Inicialidar o whatsapp
wp = WhatsApp()

input('Pressione enter para continuar apos escanear o QR Code')

df = pd.read_excel("contatos.xlsx")
nomes_palavras_chaves = list(df['Contato'])
lista_mensagens = list(df['Mensagem'])

for nome_contato, mensagem in zip(nomes_palavras_chaves, lista_mensagens):
    wp.search_contact(nome_contato)
    sleep(2)
    wp.send_message(mensagem)

#Timer de 10 segundos para fechar
sleep(10)
wp.driver.close()

