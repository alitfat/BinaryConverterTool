from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel

class BinaryConverterTool_VerGUI(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("バイナリファイル変換ツールについて")
        self.resize(350, 90)
        
        layout = QFormLayout()
        self.lbVer = QLabel("Version   \t：1.2.0\n" + 
                            "Created by \t：GaoHongyu\n" + 
                            "MailAddress\t：alitfat142@gmail.com\n" + 
                            "Created at \t：自宅")
        layout.addWidget(self.lbVer)
        
        self.setLayout(layout)
        
