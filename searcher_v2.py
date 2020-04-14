from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 502)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 641, 291))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.enter_your_keyword = QtWidgets.QLabel(self.centralwidget)
        self.enter_your_keyword.setGeometry(QtCore.QRect(50, 25, 171, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.enter_your_keyword.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.enter_your_keyword.setFont(font)
        self.enter_your_keyword.setFrameShadow(QtWidgets.QFrame.Plain)
        self.enter_your_keyword.setObjectName("enter_your_keyword")
        self.ovdje_tekst = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ovdje_tekst.setGeometry(QtCore.QRect(210, 20, 271, 32))
        self.ovdje_tekst.setObjectName("ovdje_tekst")
        self.gumb_za_submit = QtWidgets.QPushButton(self.centralwidget)
        self.gumb_za_submit.setGeometry(QtCore.QRect(480, 20, 121, 32))
        self.gumb_za_submit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(74, 74, 74);")
        self.gumb_za_submit.setObjectName("gumb_za_submit")
        self.ovdje_output = QtWidgets.QTextEdit(self.centralwidget)
        #or use QTextBrowser
        self.ovdje_output.setGeometry(QtCore.QRect(0, 290, 641, 191))
        self.ovdje_output.setObjectName("ovdje_output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #
       
        self.enter_your_keyword.setText(_translate("MainWindow", "<html><head/><body><p><font color='white'>YOUR KEYWORD:</font><br /></p></body></html>"))
        #adjust size
        #self.enter_your_keyword.adjustSize()
        #
        self.gumb_za_submit.setText(_translate("MainWindow", "Search"))
        #

        # OVAJ GUMB ONCLICK
        self.gumb_za_submit.clicked.connect(self.promjeni_output)

        #AKTIVIRA OVO DA PROMJENI TEKST:ž
        
        self.mojquestion = "Output will appear here. Thank you for using Hox Programs."
        self.ovdje_output.setPlainText(_translate("MainWindow", self.mojquestion))

    def promjeni_output(self):
        #OPERATION START
        self.search_query = self.ovdje_tekst.toPlainText()
        self.ovdje_tekst.clear()
        self.ovdje_output.clear()
        entryQuestion = self.search_query
        allthefiles = os.listdir('./')
        for something in allthefiles:
            if something.endswith('.txt'):
                with open(something, 'r') as reader:
                    try:
                        #
                        key = reader.readlines()
                        for every_line in key:
                            if entryQuestion in every_line:
                                #print("\n[+] in file : {} ".format(something),"found line :\n", every_line)
                                out_way = "\n[+] in file : {} ".format(something) + "found line :\n" + every_line
                                self.ovdje_output.insertPlainText(out_way)
                        reader.close()
                    except:
                        print("Problem occured. Program attempted to load a non-txt file.")

            #read every text file in current dir

            #check if dir
            elif "." in something:
                pass
            #if dir enter it and listdir 
            else:
                lister = os.listdir(f'./{something}/')
                #print(f"In directory {something} : ",lister)
                for each_file in lister:
                    #print(each_file)
                    #if text file open it and check it 
                    if each_file.endswith('.txt'):
                        fixed_file = f'./{something}/{each_file}'
                        with open(fixed_file,'r') as file:
                            try:
                                #
                                key = file.readlines()
                                for someline in key:
                                    if entryQuestion in someline:
                                        #print("\n[+] in file : {} ".format(each_file),"found line :\n", someline)
                                        out_way = "\n[+] in file : {} ".format(each_file) + "found line :\n" + someline
                                        self.ovdje_output.insertPlainText(out_way)
                                file.close()
                            except:
                                print("Problem occured. Program attempted to load a non-txt file.")
                                
                    elif "." in each_file:
                        pass
                    else:
                        dir_two = f"./{something}/{each_file}/"
                        lister_two = os.listdir(dir_two)
                        for every_file_two in lister_two:
                            fixed_file_location = f'{dir_two}{every_file_two}'
                            with open(fixed_file_location,'r') as file_two:
                                try:
                                    #
                                    key_two = file_two.readlines()
                                    for someline_two in key_two:
                                        if entryQuestion in someline_two:
                                            #print("\n[+] in file : {} ".format(fixed_file_location),"found line :\n", someline_two)
                                            out_way = "\n[+] in file : {} ".format(fixed_file_location) + "found line :\n" + someline_two
                                            self.ovdje_output.insertPlainText(out_way)
                                    file_two.close()
                                except:
                                    print("Problem occured. Program attempted to load a non-txt file.")
       


        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
