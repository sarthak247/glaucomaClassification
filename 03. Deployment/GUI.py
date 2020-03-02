# Import Libraries
from PyQt5 import QtCore, QtGui, QtWidgets #GUI
import sys
from models.prediction import predictGlaucoma # Prediction Function
import cv2 #OpenCV


# Glaucoma GUI
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # Main Window
        super().__init__()
        self.title = 'Glaucoma Classification' # Title
        # Dimensions
        self.top = 100
        self.left = 100
        self.width = 480
        self.height = 550
        self.mainicon = 'assets/images/main/front.png'
        self.uploadIcon = 'assets/images/main/upload.png'
        self.uiComponents()
        self.initWindow()
        
    def initWindow(self):
        # Initialize Window
        self.setWindowIcon(QtGui.QIcon(self.mainicon))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap(self.mainicon)
        label.setPixmap(pixmap)
        label.resize(480, 480)
        label.move(0, 0)
        self.dialogs = []
        self.show()

    def clickUpload(self):
        # Image Grab Function
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', 'Image files (*.jpg *.png)')
        imagePath = filename[0]
        im = cv2.imread(imagePath)
        # print(im.shape)
        # print(imagePath)
        im = cv2.resize(im, (im.shape[0]//2, im.shape[1]//2))
        # Select ROI
        r = cv2.selectROI(im)
        # Crop image
        imCrop = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
        cv2.imwrite(imagePath.split('.')[0] + '_crop.png', imCrop)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # print('Image Path: ', imagePath)
        print('Image Name: ', imagePath.split('/')[-1])
        print('Prediction: ', predictGlaucoma(imagePath))
        print('------------------------------')
        # dialog = Second()
        # # self.dialogs.append(dialog)
        # dialog.show()

    def uiComponents(self):
        # Additional UI Components
        upload = QtWidgets.QPushButton(" Upload Image".upper(), self)
        upload.setGeometry(QtCore.QRect(5, 482, 470, 65))
        upload.setIcon(QtGui.QIcon(self.uploadIcon))
        upload.setIconSize(QtCore.QSize(50, 50))
        upload.setToolTip("Upload Image Of The Fundus")
        upload.setToolTipDuration(2500)
        upload.clicked.connect(self.clickUpload)

# Driver Function
if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(App.exec())
