from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QImage
from visual import Ui_MainWindow
from PopUp import Ui_Dialog as dia2
import time
import cv2
from calculate import calculate
from startsc import Ui_Dialog
import graph

global name


def setName(name1):
    """
    Based on the user input, stores the name of the file in a variable which can be accessed by different classes/
    windows.
    :type name1: String
    :param name1: Name of file/video
    """
    global name
    name = name1


def getName():
    """
    Gets the name of the file that the user entered.
    :return: name of csv file/video.
    """
    global name
    return name


class myWindow(QtWidgets.QDialog):
    """
    Class for start screen. Allows user to enter file name to show that data.
    """

    def __init__(self):
        """
        Initialises start screen.
        Connects button press to <code>clickMethod<code>.
        """
        super(myWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.clickMethod)

    def clickMethod(self):
        """
        When the 'GO' button is pressed, the main window pops up showing the file with the same name
        entered by the user.
        """

        if self.ui.lineEdit.text() != '':
            name = self.ui.lineEdit.text()

            setName(name)
            graph.writeto()
            self.mainWindow = mainWindow()
            self.mainWindow.show()


class External(QThread):
    """
    Runs a thread for the progress bars.
    Opens CSV file and saves the data for each frame in to an array, which is then used to update the progress bars.
    """
    countChanged = pyqtSignal(list)
    row = 1
    pred = []

    def run(self):
        """
        Opens file based on filename given by the user on the start screen.
        Calls the calculate function from the calculate.py file to compute the normalised value for tastes/emotions.
        Sends this data in an array to the main thread.
        If the value for taste/emotion is above 60, it is classified as predominant.
        """

        name = getName()
        with open('../GUI/files/'+str(name)+'.csv', 'r') as f:
            self.rows = sum(1 for line in f)

        time.sleep(0.8)

        while self.row < self.rows:

            values = calculate(self.row, name)

            # Thresholds for predominancy
            for i in range(0, 5):
                if values[i] > 55:
                    External.pred.append(i)

            for i in range(5, 11):
                if values[i] > 60:
                    External.pred.append(i)

            self.row += 1

            if self.row == self.rows:
                values.clear()
                values.append(1)

            self.countChanged.emit(values)
            # OpenFace reads the frames of the video every 0.33 seconds therefore, sleep time = 0.33
            time.sleep(0.033)
            values.clear()


class VideoThread(QThread):
    """
    Runs a Thread to show the video.
    Uses openCV to display the video in a pixmap by iterating through and displaying each frame of the video.
    """
    changePixmap = pyqtSignal(QPixmap)

    def run(self):
        """
        Opens video based on filename given by the user on the start screen.
        Uses openCV to display the video in a pixmap by iterating through and displaying the video frame by frame.
        Resizes the video so it fits proportionally to the GUI (400 x 300).
        """
        name = getName()
        cap = cv2.VideoCapture('../GUI/videos/'+str(name)+'.mp4')
        while True:
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                pix = QPixmap.fromImage(img)
                pix = pix.scaled(400, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                # OpenFace reads the frames of the video every 0.33 seconds therefore, sleep time = 0.33
                time.sleep(0.033)
                self.changePixmap.emit(pix)


class myPopUp(QtWidgets.QDialog):
    """
    Class to initialise the pop up box which shows the predominant emotion/taste.
    """
    def __init__(self):
        super().__init__()
        self.ui = dia2()
        self.ui.setupUi(self)


class mainWindow(QtWidgets.QMainWindow):
    """
    Main class for application which shows the video alongside progress bars visualising the data.
    """
    def __init__(self):
        """
        Initialises all the components for the main window. Starts the threads.
        :param th: Thread to show video
        :param calc: Thread to show progress bars

        """
        super(mainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.th = VideoThread()
        self.th.changePixmap.connect(self.playVideo)
        self.th.start()

        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()
        self.popUp = myPopUp()

    def playVideo(self, image):
        """
        Function to display the video using the VideoThread class.

        :type image: QImage
        :param image: Frame from the video
        """
        self.ui.label_7.setPixmap(image)

    def onCountChanged(self, values):
        """
        Sets the values for each progress bar for both taste and emotion, using the array created in the External
        thread.
        If there are no values left, the pop up will appear

        :type values: int[]
        :param values: Array containing the average, normalised values to show on the progress bar.
        """

        if len(values) == 1:
            self.showPred()
        else:
            self.ui.bitter_bar.setValue(values[0])
            self.ui.sour_bar.setValue(values[1])
            self.ui.salty_bar.setValue(values[2])
            self.ui.sweet_bar.setValue(values[3])
            self.ui.umami_bar.setValue(values[4])

            self.ui.happy_bar.setValue(values[5])
            self.ui.sad_bar.setValue(values[6])
            self.ui.suprise_bar.setValue(values[7])
            self.ui.fear_bar.setValue(values[8])
            self.ui.anger_bar.setValue(values[9])
            self.ui.disgust_bar.setValue(values[10])

    def showPred(self):
        """
        Displays the predominant taste/emotion in the pop up box.
        If the taste/emotion is predominant, as found in the External thread, it is added to an array which is then
        used to add the words to the ListWidget of the pop up.
        """
        predTaste = []
        predEmo = []

        if External.pred.__contains__(0):
            predTaste.append("Bitter")
        if External.pred.__contains__(1):
            predTaste.append("Sour")
        if External.pred.__contains__(2):
            predTaste.append("Salty")
        if External.pred.__contains__(3):
            predTaste.append("Sweet")
        if External.pred.__contains__(4):
            predTaste.append("Umami")
        if External.pred.__contains__(5):
            predEmo.append("Happy")
        if External.pred.__contains__(6):
            predEmo.append("Sad")
        if External.pred.__contains__(7):
            predEmo.append("Surprise")
        if External.pred.__contains__(8):
            predEmo.append("Fear")
        if External.pred.__contains__(9):
            predEmo.append("Anger")
        if External.pred.__contains__(10):
            predEmo.append("Disgust")

        for i in range(len(predTaste)):
            self.popUp.ui.listWidget_taste.addItem(predTaste[i])

        for i in range(len(predEmo)):
            self.popUp.ui.listWidget_emotion.addItem(predEmo[i])

        self.popUp.show()
        graph.showgraph()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = myWindow()
    application.show()
    sys.exit(app.exec_())

# C:\Users\psyha5\AppData\Local\Programs\Python\Python37\Scripts\pyuic5 Z:\SourFace\GUI\visualisation.ui -o visual.py
