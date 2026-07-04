print("App Started")
from flask import Flask, request, render_template_string
import speech_recognition as sr

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>AI Speech To Text</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:'Poppins',sans-serif;
}

body{

background:linear-gradient(-45deg,#0f172a,#1e3a8a,#2563eb,#0ea5e9);
background-size:400% 400%;
animation:bg 10s ease infinite;

display:flex;
justify-content:center;
align-items:center;

height:100vh;

overflow:hidden;

}

@keyframes bg{

0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}

}

.card{

width:520px;

background:rgba(255,255,255,.15);

backdrop-filter:blur(20px);

border-radius:25px;

padding:40px;

text-align:center;

box-shadow:0 20px 60px rgba(0,0,0,.35);

border:1px solid rgba(255,255,255,.2);

color:white;

}

.logo{

font-size:70px;

margin-bottom:10px;

}

h1{

font-size:34px;

font-weight:700;

margin-bottom:8px;

}

.subtitle{

font-size:15px;

opacity:.9;

margin-bottom:30px;

}

.upload{

display:block;

padding:18px;

border:2px dashed white;

border-radius:18px;

cursor:pointer;

transition:.3s;

margin-bottom:25px;

}

.upload:hover{

background:rgba(255,255,255,.15);

transform:scale(1.02);

}

input[type=file]{

display:none;

}

button{

width:100%;

padding:16px;

font-size:18px;

font-weight:600;

border:none;

border-radius:15px;

cursor:pointer;

background:linear-gradient(90deg,#00d2ff,#3a7bd5);

color:white;

transition:.4s;

}

button:hover{

transform:translateY(-3px);

box-shadow:0 15px 35px rgba(0,0,0,.35);

}

.result{

margin-top:30px;

}

textarea{

margin-top:15px;

width:100%;

height:180px;

padding:18px;

border:none;

border-radius:15px;

resize:none;

font-size:15px;

background:white;

color:#111827;

}

.footer{

margin-top:30px;

font-size:13px;

opacity:.8;

}

.circle{

position:absolute;

border-radius:50%;

background:rgba(255,255,255,.15);

animation:float 8s infinite ease-in-out;

}

.circle:nth-child(1){

width:180px;
height:180px;
left:5%;
top:10%;

}

.circle:nth-child(2){

width:250px;
height:250px;
right:5%;
bottom:5%;

animation-delay:2s;

}

@keyframes float{

50%{

transform:translateY(-25px);

}

}

</style>

</head>

<body>

<div class="circle"></div>
<div class="circle"></div>

<div class="card">

<div class="logo">🎙️</div>

<h1>Speech To Text AI</h1>

<p class="subtitle">
Upload your audio file and let Artificial Intelligence convert speech into text instantly.
</p>

<form method="POST" enctype="multipart/form-data">

<label class="upload">

📂 Click here to choose a WAV audio file

<input type="file" name="audio" accept=".wav" required>

</label>

<button>

🚀 Convert Speech

</button>

</form>

{% if text %}

<div class="result">

<h2>📝 Transcribed Text</h2>

<textarea readonly>{{text}}</textarea>

</div>

{% endif %}

<div class="footer">

Powered by Flask • Python • SpeechRecognition
<div>Designed by Suriya Prakash</div>

</div>

</div>

</body>

</html>
'''

@app.route("/",methods=["GET","POST"])
def home():

    text=""

    if request.method=="POST":

        file=request.files["audio"]

        file.save("audio.wav")

        recognizer=sr.Recognizer()

        try:

            with sr.AudioFile("audio.wav") as source:
                audio=recognizer.record(source)

            text=recognizer.recognize_google(audio)

        except:
            text="Unable to recognize speech."

    return render_template_string(HTML,text=text)

if __name__=="__main__":
    print("Starting Flask App")
    app.run(host="127.0.0.1", port=5000, debug=True)