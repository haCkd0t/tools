from pytube import YouTube
url = input("Please enter URL\n")
try:
    print("Downloading...")
    YouTube(url).streams.filter(only_audio=True).first().download("/home/joke")
    print("Download Completed")
except:
    print("Something missing!!")