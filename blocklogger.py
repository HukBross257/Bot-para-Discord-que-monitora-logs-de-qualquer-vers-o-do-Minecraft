import time
import requests
'''Irei melhorar esse codigo em pouco em pouco :)'''

server_log = '' # Coloque aqui o caminho para o server.log do seu server
discord_webhook = ''
def abrir_os_logs():
    '''Coloque o caminho para o arquivo server.logs aqui'''

    return open(server_log, 'r')

def mostrar_logs(dados):
    ''' Aqui ira pegar os dados do logs e enviar para o canal do discord'''
    dados.seek(0, 2)  # Vai para o final do arquivo
    while True:
        linhas = dados.readlines()
        linhas = [linha.strip() for linha in linhas]

        for linha in linhas:
            try:
                requests.post(discord_webhook, json={'content': linha})

            except Exception as e:
                print(f'Aconteceu um erro e nao foi possivel enviar para o Discord {e}')
            print(linha)
        time.sleep(0.2)
