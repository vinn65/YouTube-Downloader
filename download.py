from pytube import YouTube

def Download(link):
    DownloadObject = YouTube(link)
    DownloadObject = DownloadObject.streams.get_highest_resolution()
    try:
        print("Downloading videos ... ")
        print("This could take a while")
        DownloadObject.download()
        
    except:
        print("An error Occurred!")    
    print("Download completed.")   

link = input("Enter a youtube link to download a video! URL:") 
Download(link)

