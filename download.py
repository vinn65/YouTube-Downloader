from pytube import YouTube


def Download(link):
    DownloadObject = YouTube(link)
    DownloadObject = DownloadObject.streams.get_highest_resolution()