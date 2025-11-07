import time
import requests


server_log = 'server.log' # Coloque aqui o caminho para o server.log do seu server
discord_webhook = 'https://discord.com/api/webhooks/1436121229277794325/iGxmoabpXKw3aCX26UCRW6p_uj0WGzuzJ-MMYgqlJIw6MNzZursRTuPCLg0XL6ux4I-M' # Coloque o webhook aqui !

def abrir_os_logs():
    '''Coloque o caminho para o arquivo server.logs aqui'''

    return open(server_log, 'r')

def mostrar_logs(dados): 
    ''' Aqui ira pegar os dados do logs e enviar para o canal do discord'''

    dados.seek(0, 2)  # Vai para o final do arquivo
    discord_weebhook = '' 

    while True:
        linhas = dados.readlines()
        linhas = [linha.strip() for linha in linhas]

        for linha in linhas:
            requests.post(discord_webhook, json={'content': linha})
            print(linha)

        time.sleep(0.2)
