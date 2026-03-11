import requests
import re

# Fontes de canais que o robô vai varrer
FONTES = [
    "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/br.m3u",
    "https://raw.githubusercontent.com/joaoguidugli/FTA-IPTV-Brasil/master/playlist.m3u8"
]

def montar_lista():
    print("🤖 Robô iniciando varredura...")
    corpo_lista = "#EXTM3U\n"
    
    for url in FONTES:
        try:
            # O robô tenta ler a fonte por 10 segundos
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                # Ele filtra os canais brasileiros
                links = re.findall(r'#EXTINF.*?\nhttp.*', r.text)
                for link in links:
                    corpo_lista += link + "\n"
        except:
            continue
            
    with open("meus_canais.m3u", "w") as f:
        f.write(corpo_lista)
    print("✅ Lista atualizada com sucesso!")

if __name__ == "__main__":
    montar_lista()
