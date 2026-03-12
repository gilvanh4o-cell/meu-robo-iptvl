import os

# Conteúdo da sua lista IPTV
conteudo = "#EXTM3U\n#EXTINF:-1, Canal de Teste Gilvan\nhttp://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"

# Criando o arquivo da lista
with open("lista_gilvan.m3u", "w", encoding="utf-8") as f:
    f.write(conteudo)

print("Arquivo lista_gilvan.m3u criado com sucesso!")