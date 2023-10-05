from pytube import YouTube #inporta o pytube

def baixar_video_youtube(link):
    try:
        # Crie um objeto YouTube com o link fornecido
        yt = YouTube(link)

        # Obtenha a melhor qualidade disponível
        video = yt.streams.get_highest_resolution()

        # Baixe o vídeo
        print(f'Baixando: {yt.title}...')
        video.download(output_path='C:/Users/adeni/Desktop/python/BaixarVideoYouTube/Videos_baixados')
        print('Download concluído com sucesso!')
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    link = input("Digite o link do vídeo do YouTube: ")
    baixar_video_youtube(link)
