import os

print("--- Iniciando Robo do Gilvan ---")

# Criando o conteúdo da lista
conteudo = "#EXTM3U\n#EXTINF:-1, Canal de Teste Gilvan\nhttp://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"

# Salvando o arquivo m3u
with open("lista_gilvan.m3u", "w", encoding="utf-8") as f:
    f.write(conteudo)

print("--- Lista criada com sucesso! ---")
