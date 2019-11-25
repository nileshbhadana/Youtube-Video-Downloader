import tkinter as tk
import pafy,os,subprocess
from pydub import AudioSegment

#from pytube import YouTube
def downloadVid():
    global E1
    url =E1.get()
    video=pafy.new(url)
    stream=video.allstreams
    s=1
    a=[]
    counter=1
    for i in stream:
        if "mp4" in str(i):
            a.append(i)
        if "audio" in str(i):
            a.append(i)
    for i in a:
        print(str(counter)+". ",end="")
        print(i)
        counter +=1
        s +=1
    stream=a
    n=int(input("Enter your choice: "))
    vid=stream[n-1]
    destination="./"
    checkau=str(vid)
    print(checkau)
    vid.download(destination)
    
    videotitle=video.title
    if "audio" in checkau:
        extension=checkau.split(":")[1].split("@")[0]
        mytitle=videotitle+"."+extension
        print("Converting to MP3...")
        AudioSegment.from_file("./"+mytitle).export("./"+videotitle+".mp3", format="mp3")
        os.remove(mytitle)

    
    if "mp4" in checkau:
        extension=checkau.split(":")[1].split("@")[0]
        
        myvtitle=videotitle+"."+extension
        
        audios=stream[1]
        audios.download(destination+"audios/")
        audios=str(audios)
        if "audio" in audios:
            extension1=audios.split(":")[1].split("@")[0]
            mytitle=videotitle+"."+extension1
            print("Merging Audio and Video")
            while ' ' in mytitle:
                mytitle1=mytitle.replace(' ','-')
                os.rename("./audios/"+mytitle,"./audios/"+mytitle1)
                mytitle=mytitle1
            while ' ' in myvtitle:
                myvtitle1=myvtitle.replace(' ','-')
                os.rename(myvtitle,myvtitle1)
                myvtitle=myvtitle1
            while ' ' in videotitle:
                videotitle=videotitle.replace(' ','-')
            AudioSegment.from_file("./audios/"+mytitle).export("./audios/"+videotitle+".wav", format="wav")
            os.remove("./audios/"+mytitle)
            cmd="ffmpeg -i ./"+myvtitle+" -i ./audios/"+videotitle+".wav -c:v copy -c:a aac -strict experimental "+"1"+myvtitle+" >/dev/null"
            subprocess.call(cmd,shell=True)
            os.remove(myvtitle)
            os.remove("./audios/"+videotitle+".wav")
            os.rename("1"+myvtitle,myvtitle)
       
    print(video.title+"Has been downloaded")
root=tk.Tk()

w=tk.Label(root,text="Youtube Downloader")
w.pack()


E1=tk.Entry(root,bd=5)
E1.pack(side=tk.TOP)


button=tk.Button(root,text="Download",fg="red",command=downloadVid   )
button.pack(side=tk.BOTTOM)

root.mainloop()


#https://www.youtube.com/watch?v=H46J19bCq4A