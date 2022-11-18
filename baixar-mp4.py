
from pytube import YouTube, streams
from pytube.cli import on_progress

# Instalação das biblioteca do python pelo cmd ou o PowerShell com os comandos abaixo
# pip install pytube
# pip install moviepy
# pip shell

# Digite o link do video no caso a (url) do video do youtube
link = input("Digite o link do video que deseja baixar: ")
yt = YouTube(link, on_progress_callback = on_progress)
print("Titulo = ", yt.title)
print("Baixando... ")

# Vai baixar a maior resolução do video que pretende baixer disponivel do video
ys = yt.streams.get_highest_resolution()
ys.download()
print("Download completo! ")

# O video vai esta na mesma pasta do script acima.
