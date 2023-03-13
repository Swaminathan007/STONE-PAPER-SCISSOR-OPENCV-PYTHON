from flask import *
import cv2
import handdetector as ha
app = Flask(__name__)
h = ha.Handdetector()
pos = "Nothing"
cam = cv2.VideoCapture(0)
def genframes():
    global pos
    while True:
        suc,img = cam.read()
        if suc:
            img = cv2.flip(img,1)
            img = h.findhand(img)
            poslist = h.findposition(img)
            if(poslist):
                fingers = h.fingersup(poslist)
                if(fingers == [1,1,1,1,1]):
                    pos = "Paper"
                elif(fingers == [0,0,0,0,0]):
                    pos = "stone"
                elif(fingers == [0,1,1,0,0]):
                    pos = "scissor"
                else:
                    pos = "Nothing"
            img = cv2.putText(img, pos, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0,255,0), 1, cv2.LINE_AA)
            ret,buffer = cv2.imencode(".jpg",img)
            img = buffer.tobytes()
        yield(b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" + img + b'\r\n')

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/video")
def video():
    return Response(genframes(),mimetype="multipart/x-mixed-replace; boundary=frame")

app.run(host="0.0.0.0",debug=True)