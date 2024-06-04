from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel

class BinaryConverterTool_VerGUI(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("バイナリファイル変換ツールについて")
        self.resize(350, 90)
        
        layout = QFormLayout()
        self.lbVer = QLabel("Version   \t：1.1.0\n" + 
                            "Created by \t：GaoHongyu\n" + 
                            "MailAddress\t：hongyu.gao.zs@kyocera.jp\n" + 
                            "Created at \t：京セラ横浜事務所")
        layout.addWidget(self.lbVer)
        
        self.setLayout(layout)
        
