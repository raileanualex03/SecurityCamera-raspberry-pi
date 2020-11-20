  **SECURITY CAMERA**
  
    This project will create a Flask server which will be opened at localhost:5000.
I used this project on a raspberry pi4 B in order to create a security camera for my house. There are a few issues in the rasbian os with the environment installation, contact me if you need any help.
It uses an external webcam which will record any movement that it sees. This project uses cv2 in order to create and save videos.
Functionalities:
   - see live camera on browser.
   - store videos for each run ( videos can be seen at localhost:5000/videos or by pressing videos in menu ), each video can be downloaded.
   - get instant help by calling my personal number.
   - the videos stored will contain just the frames that the algorithm considers that there was any movement in the video in order to maximize the storage-necessity part. ( the purpose of this project was to become a security camera -- this doesn't need to know about not moving frames ).
   - you can see LIVE on browser if there is anything moving in the photo ( "moving" text appears in the left corner of the stream, but it won't appear in the saved video).
   - each video will have a timestamp ( the stream will also have it in the right down side).
   - the algorithm of detecting movement compares two consecutives received frames and checks a certain percentage of the current frame received from the camera in order to decide if this there was any movement or not.
   
   *How to use this project?*
1. Create an empty directory called "Data" in the directory "Camera".
2. Create an environment, it must have flask, cv2, numpy. ( As you can see in the requirements.txt --not implemented yet)
3. Make sure that your camera is connected to your device. If you are using an external camera everything should be just fine. If you want to use the built-in camera, you should change in Camera/Source/camera.py, in the constructor of the class VideoCamera, VideoWriter(0).
4. Run these commands: export FLASK_APP=server.py
                       flask run
                      
