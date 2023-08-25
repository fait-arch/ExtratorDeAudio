'''
    ------------- REQUICITOS --------------- 
        Tener instalada la libreria "pytube"
        pip install pytube

'''
from pytube import YouTube

# URL del video de YouTube
url = "https://www.youtube.com/watch?v=Y56ODjb8ZMo"

# Directorio de descarga
download_dir = "E:\Descargas"

# Crear un objeto YouTube
yt = YouTube(url)

# Obtener el mejor stream de audio
audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()

# Descargar el audio en la carpeta especificada
audio_stream.download(output_path=download_dir)

print("Descarga completada.")
