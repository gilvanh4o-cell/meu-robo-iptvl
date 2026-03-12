import os
conteudo = "#EXTM3U\n#EXTINF:-1, Canal de Teste Gilvan\nhttp://link.com"
with open("lista_gilvan.m3u", "w", encoding="utf-8") as f:
    f.write(conteudo)
print("Sucesso!")