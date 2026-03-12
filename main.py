# Esse código cria a sua lista de canais
import os

print("Iniciando o Robô do Gilvan...")

# Aqui é onde a mágica acontece. Ele cria o arquivo da lista.
conteudo = "#EXTM3U\n#EXTINF:-1, Canal do Gilvan\nhttp://link-do-seu-canal.com"

with open("lista_canais.m3u", "w") as f:
    f.write(conteudo)

print("Sucesso! O arquivo lista_canais.m3u foi criado.")
