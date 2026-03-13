import requests

url = "https://iptv-org.github.io/iptv/index.m3u"

data = requests.get(url).text

with open("lista.m3u","w") as f:
    f.write(data)

print("lista atualizada")