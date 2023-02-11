import pytube
url=input("enter video url")
path="D:"
pytube.YouTube(url).streams.get_highest_resolution().download(path)