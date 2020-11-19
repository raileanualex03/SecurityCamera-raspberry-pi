from imports import *

app = Flask(__name__)
app.config['VIDEO_DIRECTORY'] = "./Camera/Data"
camera = VideoCamera()


def generateFrames(camera):
    while True:
        frame, difference_frame = camera.get_frame()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    # this function will manage the incoming data from the webcam ( creating a livestream )
    return Response(generateFrames(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

def generateDifferences(camera):
    while True:
        frame, difference_frame = camera.get_frame()

        if waitKey(1) == 27 or 0xFF == ord(q):
            break
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + difference_frame + b'\r\n\r\n')


@app.route('/last_frame')
def last_frame():
    # this function will manage the incoming data from the webcam ( creating a livestream )
    return Response(generateDifferences(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def main():
	return render_template("index.html")

@app.route('/videos')
def videos():
    file = open("videos.txt", 'r')
    elem = file.read()
    elems = elem.split(',')
    file.close()
    return render_template("videos.html", videos=elems[0:len(elems)-1])

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/get-video/<video_name>', methods=["GET"])
def get_video(video_name):
    return send_from_directory(app.config["VIDEO_DIRECTORY"], filename=video_name, as_attachment=False)
    
@app.route('/get-list')
def get_list():
    file = open("videos.txt")
    elem = file.read()
    elems = elem.split(',')
    return jsonify({"data":elems}), 200

if __name__== '__main__':
	app.run(host="0.0.0.0", port="5000")