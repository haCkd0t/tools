from pytube import YouTube
url = input("Please enter URL\n")
try:
    YouTube(url).streams.filter(only_audio=True).first().download("/home/joke")
    print("Downloading...")
    print("Download Completed")
except:
    print("Something missing!!")
