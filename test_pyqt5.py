import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 500, 300)

        btn1 = QPushButton("load",self)
        btn1.clicked.connect(self.btn_fun_FileLoad)      

    def btn_fun_FileLoad(self):        
        fname=QFileDialog.getOpenFileName(self,"File Load",'D:/ubuntu/disks/swap.disk','All File(*);; Text File(*.txt);; PPtx file(*ppt *pptx)', 'PPtx file(*ppt *pptx)' )

        if fname[0]:
            print("파일 선택됨 파일 경로는 아래와 같음")
            print(fname[0])
        else:
            print("파일 안 골랐음")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()