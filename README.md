name: Atualizar IPTV
on:
  workflow_dispatch:
  schedule:
    - cron: '*/15 * * * *' # <-- ISSO AQUI ACORDA O ROBÔ A CADA 15 MINUTOS

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Rodar o Robô
        run: python bot.py
      - name: Salvar Lista
        run: |
          git config --global user.name 'Gilvan'
          git config --global user.email 'gilvan@exemplo.com'
          git add meus_canais.m3u
          git commit -m "Lista atualizada automaticamente" || exit 0
          git push
          
