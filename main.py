from pytube import YouTube

link = input("Digite o link do video que voce deseja baixar: ")

yt = YouTube(link)
print("Baixando", yt.title)

resolucao = yt.streams.filter(progressive=True,file_extension="mp4").order_by("resolution").desc().first()
resolucao.download()

print("Download Concluido")


