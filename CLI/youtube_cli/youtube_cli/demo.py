from pytube import YouTube

youtube = YouTube("https://youtu.be/p2umuNPbTrE")
print(youtube.js)
print(youtube.title)
print(youtube.author)
print(youtube.age_restricted)
print(youtube.caption_tracks)
print(youtube.description)
print(youtube.fmt_streams)
