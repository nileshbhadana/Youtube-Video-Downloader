import tkinter as tk
import pafy,os
from pydub import AudioSegment

#from pytube import YouTube
def downloadVid():
    global E1
    url =E1.get()
    video=pafy.new(url)
    stream=video.allstreams
    s=1
    counter=1
    for v in stream:
        print(str(counter)+". ",end="")
        print(v)
        counter +=1
        s +=1
    n=int(input("Enter your choice: "))
    vid=stream[n-1]
    destination="./"
    vid.download(destination)
    checkau=str(vid)
    videotitle=video.title
    if "audio" in checkau:
        extension=checkau.split(":")[1].split("@")[0]
        mytitle=videotitle+"."+extension
        print("Converting to MP3...")
        AudioSegment.from_file("./"+mytitle).export("./"+videotitle+".mp3", format="mp3")
        os.remove(mytitle)
    print(video.title+"Has been downloaded")
root=tk.Tk()

w=tk.Label(root,text="Youtube Downloader")
w.pack()


E1=tk.Entry(root,bd=5)
E1.pack(side=tk.TOP)


button=tk.Button(root,text="Download",fg="red",command=downloadVid   )
button.pack(side=tk.BOTTOM)

root.mainloop()