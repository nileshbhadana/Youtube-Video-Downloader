from flask import Flask, redirect, url_for, request, render_template 
import tkinter as tk
import pafy,os,subprocess
from pydub import AudioSegment
template_dir=os.path.abspath('/var/www/html/flaskyt/templates')
app = Flask(__name__,template_folder=template_dir)
@app.route('/')
def success(url):
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
    return render_template("donwloadlink.html", len = len(a), Pokemons = a)

@app.route('/login',methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        url = request.form['url']
        #url1 = request.args.get('url')
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
        return render_template("donwloadlink.html", len = len(a), Pokemons = a,urltogo=url)
        
        '''url1 = request.form['url']
        success(url1)
        return redirect(url_for('success',url = url1))
    else:
        url1 = request.args.get('url')
        return redirect(url_for('success',url = url1))
        '''

@app.route('/download',methods = ['GET', 'POST'])
def login1():
    if request.method == 'POST':
        url = request.form['url']
        choice=request.form['choice']
        #url1 = request.args.get('url')
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
            counter +=1
            s +=1
        stream=a
        n=int(choice)
        vid=stream[n-1]
        destination="./"
        checkau=str(vid)
        print(checkau)
        vid.download(destination)
        try:
            os.mkdir(destination+"audios")
        except:
            print()
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

        return video.title+"Has been downloaded"   
if __name__=='__main__':
    app.run(debug = True)
