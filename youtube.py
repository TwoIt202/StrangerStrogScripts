from pytube import YouTube

url = input("Введите URL видео: ")
yt = YouTube(url)

stream = yt.streams.get_highest_resolution()
stream.download()
