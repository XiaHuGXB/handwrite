from PySide2.QtWidgets import QApplication, QMessageBox,QFileDialog,QLabel
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QPixmap
from Hwrite import hwrite
from PIL import ImageQt


_DEFAULT_WORD_SPACING = 0
_DEFAULT_LEFT_MARGIN = 0
_DEFAULT_TOP_MARGIN = 0
_DEFAULT_RIGHT_MARGIN = 0
_DEFAULT_BOTTOM_MARGIN = 0


class Config:
    def __init__(self):
        self.left_margin = 0
        self.right_margin = 0
        self.top_margin = 0
        self.bottom_margin = 0
        self.word_spacing = 0
        self.line_spacing = 0
        self.front_size = 0
        self.image_height = 297
        self.image_weight = 210

        self.font_size_sigma = 0
        self.word_spacing_sigma = 0
        self.line_spacing_sigma = 0
        self.perturb_x_sigma = 0
        self.perturb_y_sigma = 0
        self.perturb_theta_sigma = 0



class Imagewindow:
    def __init__(self):
        self.image = QUiLoader().load('../ui/image.ui')
        self.path = './'
        self.qimages = []
        self.count = 0
        self.image.buttondown.clicked.connect(self.nextimg)
        self.image.buttonup.clicked.connect(self.beforimage)
        self.image.savebutton.clicked.connect(self.saveimage)

    def nextimg(self):
        if self.count+1 <= len(self.qimages)-1:
            self.count = self.count + 1
            self.showimage(self.qimages[self.count])

    def beforimage(self):
        if self.count >= 1:
            self.count = self.count - 1
            self.showimage(self.qimages[self.count])

    def saveimage(self):
        for i in range(len(self.qimages)):
            img = self.qimages[i]
            img = ImageQt.fromqpixmap(img)
            img.save(self.path+'/'+str(i)+'.jpg')

    def showimage(self,img):
        pixmap = QPixmap(img)  # 按指定路径找到图片
        self.image.label.setPixmap(pixmap)  # 在label上显示图片
        self.image.label.setScaledContents(True)


class Helpwindow:
    def __init__(self):
        self.ui = QUiLoader().load('../ui/help.ui')



class Mainwindow:
    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('../ui/main.ui')
        self.ui.out_path.clicked.connect(self.msg)
        self.ui.in_path.clicked.connect(self.msg_in)
        self.ui.pushButton_3.clicked.connect(self.btnClicked)
        self.creat_menu()

        self.config = Config()

    def msg(self):
        directory1 = QFileDialog.getExistingDirectory()
        print(directory1)  # 打印文件夹路径
        self.ui.out_text.setText(directory1)

    def msg_in(self):
        directory1 = QFileDialog.getOpenFileName(filter= "TXTs (*.txt)")
        print(directory1)  # 打印存在的文件
        self.ui.in_text.setText(directory1[0])
        with open(directory1[0],'r',encoding='utf-8') as f:
            data = f.readlines()
        txt = ''
        for line in data:
            txt = txt + line
        self.ui.plainTextEdit.setPlainText(txt)

    def windowhelp(self):
        self.win = Helpwindow()
        self.win.ui.show()
        self.win.ui.exec_()

    def windowauthor(self):
        temp = QMessageBox()
        temp.information(self.ui,'作者信息','gxb')


    def btnClicked(self):
        self.chile_Win = Imagewindow()
        convertext = self.ui.plainTextEdit.toPlainText()  #文本
        self.update_config()  #更新参数
        images = hwrite(convertext,self.config)
        qimages = []
        for img in images:
            qimg = ImageQt.ImageQt(img)
            qimg = QPixmap(qimg)
            qimages.append(qimg)
        self.chile_Win.qimages = qimages
        text = self.ui.out_text.text()
        if text:
            self.chile_Win.path = text
        self.chile_Win.showimage(qimages[0])
        self.chile_Win.image.show()
        self.chile_Win.image.exec_()

    def update_config(self):
        self.config.left_margin = self.ui.left_margin.value()
        self.config.right_margin = self.ui.right_margin.value()
        self.config.top_margin = self.ui.top_margin.value()
        self.config.bottom_margin = self.ui.bottom_margin.value()
        self.config.word_spacing = self.ui.word_spacing.value()
        self.config.line_spacing = self.ui.line_spacing.value()
        self.config.front_size = self.ui.front_size.value()
        self.config.image_height = self.ui.image_height.value()
        self.config.image_weight = self.ui.image_weight.value()

        # random
        self.config.font_size_sigma = self.ui.font_size_sigma.value()
        self.config.word_spacing_sigma = self.ui.word_spacing_sigma.value()
        self.config.line_spacing_sigma = self.ui.line_spacing_sigma.value()
        self.config.perturb_x_sigma = self.ui.perturb_x_sigma.value()
        self.config.perturb_y_sigma = self.ui.perturb_y_sigma.value()
        self.config.perturb_theta_sigma = self.ui.perturb_theta_sigma.value()

    def creat_menu(self):
        mainMenu = self.ui.menuBar()
        fileMenu = mainMenu.addMenu("File")
        helpMenu = mainMenu.addMenu("Help")
        #editMenu = mainMenu.addMenu("Edit")
        #fileMenu.triggered.connect(self.tset)
        Actionbackground = fileMenu.addAction('选择背景图片')
        Actionhelp = helpMenu.addAction('help')
        Actionhelp.triggered.connect(self.windowhelp)
        Actionmseeage = helpMenu.addAction('author')
        Actionmseeage.triggered.connect(self.windowauthor)
        Actionbackground.triggered.connect(self.background)

    def background(self):
        print('test')








app = QApplication([])
stats = Mainwindow()
newWin = Imagewindow()
stats.ui.show()
app.exec_()