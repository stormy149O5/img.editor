import os
from PyQt5.QtWidgets import(
    QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QVBoxLayout, QHBoxLayout
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from PIL import Image
from PIL.ImageFilter import SHARPEN

#Step 1
app = QApplication([])
win = QWidget()
win.resize(800, 550)
win.setWindowTitle('Image Editor 😊')

#Step 2
lb_image = QLabel('Image')
btn_dir = QPushButton('Folder')
lw_files = QListWidget()
btn_left = QPushButton('Left')
btn_right = QPushButton('Right')
btn_mirror = QPushButton('Mirror')
btn_sharp = QPushButton('Sharpness')
btn_bw = QPushButton('B/W')

#Step 3
row = QHBoxLayout() #main layout
col1 = QVBoxLayout() #left layout
col2 = QVBoxLayout() #right layout

col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image)
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_mirror)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)

col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)

win.setLayout(row)

def filter_files(files, extensions): #Filter files that end with given extensions
    result = []
    for filename in files:
        for ext in extensions:
            if filename.lower().endswith(ext):
                result.append(filename)
                break 
    return result


workdir = ''
def chooseWorkdir(): #Open the folder
    global workdir #Assign the global variable
    workdir = QFileDialog.getExistingDirectory() #Returns the path to the selected folder

def showFilenamesList():
    extensions = ['.jpg', '.png', 'jpeg', 'gif']
    chooseWorkdir() #open the folder dialog
    if not workdir: #if workdir is empty (don't open anything)
        return #end the function

    filenames = filter_files(os.listdir(workdir), extensions) #Filter files that end with given extensions
    lw_files.clear() #delete all files from the last list
    for filename in filenames:
        lw_files.addItem(filename) #add the filtered files to the list

btn_dir.clicked.connect(showFilenamesList) #connect the function to the button

class ImageProcessor:
    def __init__(self): #constructor
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/" #the folder to save the modifier imgs

    def loadImage(self, filename): #load the img
        self.filename = filename
        fullname = os.path.join(workdir, filename) #full path, join = connect
        self.image = Image.open(fullname) #open the img

    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)): #if the folder doesn't exist or is not a folder
            os.mkdir(path) #create new saved folder
        fullname = os.path.join(path, self.filename) #the path of the saved img
        self.image.save(fullname)

    def do_left(self):
        if self.image is None:
            return
        self.image = self.image.transpose(Image.Transpose.ROTATE_90) #rotate 90
        self.saveImage() #save the img
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_right(self):
        if self.image is None:
            return
        self.image = self.image.transpose(Image.Transpose.ROTATE_270) #rotate 270
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_flip(self):
            if self.image is None:
                return
            self.image = self.image.transpose(Image.Transpose.FLIP_LEFT_RIGHT) #flip the img
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showImage(image_path)

    def do_sharpen(self):
            if self.image is None:
                return
            self.image = self.image.filter(SHARPEN)
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showImage(image_path)

    def showImage(self, path):
         lb_image.hide() #hind the text labelk
         pixmapimage = QPixmap(path) #load the img from the folder
         w, h = lb_image.width(), lb_image.height() #get the size of the label
         pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio) #resize while maintaining proportional
         lb_image.setPixmap(pixmapimage) #put the img to the label
         lb_image.show() #show the label

    def do_bw(self):
            if self.image is None:
                return
            self.image = self.image.convert("L") #change to grey scale
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showImage(image_path)

workimage = ImageProcessor()
def showChoosenImage():
    filename = lw_files.currentItem().text() #get the name of the selected file
    workimage.loadImage(filename) #load the img
    workimage.showImage(os.path.join(workdir, filename)) #show the img

lw_files.currentRowChanged.connect(showChoosenImage) #when we choose another img
btn_bw.clicked.connect(workimage.do_bw) #when we click on the button
btn_left.clicked.connect(workimage.do_left) #when we click on the button
btn_right.clicked.connect(workimage.do_right) #when we click on the button
btn_sharp.clicked.connect(workimage.do_sharpen) #when we click on the button
btn_mirror.clicked.connect(workimage.do_flip) #when we click on the button
btn_dir.setObjectName("btnFolder")
win.setStyleSheet("""
    QWidget{
        background-color: #34813F;
        color: #EFFFF1;
        font-family: "Times New Roman";
        font-size: 20px;
    }
    QLabel{
        background-color: #55A45F;
    }
    QPushButton{
        background-color: #339966;
        border-radius: 4px;
    }
    QPushButton::hover{
        background-color: #3CB679;
    }
    QPushButton#btnFolder{
        background-color: #32369A;
    }
""")

win.show()
app.exec()