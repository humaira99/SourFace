# SourFace

Facial Expression Recognition GUI created as part of my summer internship with the Mixed Reality Lab, University of Nottingham.\
This application detects your taste and emotion based on videos of your face.

### Pre-requisites 
•	Python/Python IDE such as PyCharm
•	OpenFace
•	Video Editing Software e.g. iMovie 

### Editing the Video
1.	After recording the video of the participant eating, import it in to iMovie 
2.	Crop the video so it starts after the PT has put the sample in their mouth. This is because opening of the mouth can classify ‘surprise’ as an emotion and will produce false positive results
3.	If at any point the PT looks to the side/down, edit this section of the video out as it can skew the data. 
NOTE: When running the video on openFace (explained in the next section; if at any point confidence is low – indicated by a red confidence level, crop this section out) 
4.	Save the video in SourFace/GUI/videos in a .mp4 format 

### OpenFace
5.	Download openFace using the following link: https://github.com/TadasBaltrusaitis/OpenFace/wiki/Windows-Installation
6.	Locate and open the Application named ‘OpenFaceOffline’ from the OpenFace directory
7.	Go to Record and deselect everything except ‘Record AUs’. This will ensure only action unit data is recorded in the csv file
8.	Go to File > Open Video and select the edited video of the participant
9.	The video should then start being processed by OpenFace. Make sure the confidence level stays green and the face mapping looks accurate. If not, the video may need to be re-edited, as described in the previous section. 
10.	After the video has finished processing, navigate to OpenFace_2.0.5_win_x64/processed. Move the csv file in to SourFace/GUI/files. Make sure the name of the file is the same as the name of the video. 

### GUI
11.	Ensure the following packages are installed and up to date in your Python interpreter:   
•	Matplotlib 
•	Numpy
•	Opencv-python
•	Pandas
•	Pyqt5
12.	Run the vis.py script
13.	On the start screen, enter the file/video name (which should be the same) 
14.	Press ‘Go’. The video should appear with progress bars showing the level of emotion/taste as the video runs. 
15.	After the video runs, a pop up showing predominant tastes and emotions should appear, along with graphs showing taste and emotion levels for the whole video

