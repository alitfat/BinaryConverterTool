import sys
import os

from PyQt5.QtWidgets import QDialog,QApplication,QWidget
from PyQt5.QtGui import QCloseEvent

from GUI.BinaryConverterToolGUI import Ui_BinaryConverterToolGUI
from GUI.BinaryConverterToolGUI_Version import BinaryConverterTool_VerGUI

from Lib.FileSysProcess import FileSysProcess
from Lib.QtLib import qtBoxLib, qtTextEdit
from Lib.BinaryConverterLib import BinaryConverterLib
from config.xmlLib.BinaryConverterToolGUIConfig import BinaryConverterToolConfig

class Ui_BinaryConverterTool(Ui_BinaryConverterToolGUI):

    def __init__(self):
        super(Ui_BinaryConverterTool, self).__init__()
        self.FileSysProcess = FileSysProcess()
        self.qtTextEdit = qtTextEdit()
        self.dstETConfig = BinaryConverterToolConfig(os.getcwd() + "\\config",self)
        #【メニューバー】GUI作成
        self.Form_SetWindowTitle = "【バイナリファイル変換】ツール"
        return
    
    def addUiSetting(self, ui:QWidget) -> None:
        """
        -----------------------------------------------------------------
        BinaryConverterTool ui設定追加処理\n
        -----------------------------------------------------------------
        """
        self.Form = ui

        self.dstETConfig.getConfigSetting()
        
        self.dstETConfig.updateGUISetting()
        self.actionGUI_Update()
        self.overrideSetting()
        return
    

    def actionGUI_Update(self) -> None:
        """
        -----------------------------------------------------------------
        BinaryConverterTool GUI更新処理\n
        -----------------------------------------------------------------
        """
        #【メニューバー】GUI作成
        self.Form_SetWindowTitle = self.dstETConfig.toolName.toolWindowTitle
        self.Form.setWindowTitle(self.Form_SetWindowTitle)
        self.dstETConfig.updateConfigSetting()
        
        return


    def overrideSetting(self) -> None:
        """
        -----------------------------------------------------------------
        BinaryConverterTool overrideSetting処理\n
        -----------------------------------------------------------------
        """
        #ドラッグ処理で【対象ファイルアドレス】内容取得
        self.txObjFileName.dragEnterEvent = lambda e: self.qtTextEdit.DragEnterEvent(e)
        self.txObjFileName.dropEvent = lambda e:self.qtTextEdit.DragEvent_FileAddr(self.txObjFileName, e)
        
        #ドラッグ処理で【生成ファイルパス】内容取得
        self.txDstFilePath.dragEnterEvent = lambda e: self.qtTextEdit.DragEnterEvent(e)
        self.txDstFilePath.dropEvent = lambda e:self.qtTextEdit.DragEvent_FilePath(self.txDstFilePath, e)
        
        #ドラッグ処理で【生成ファイル名称】内容取得
        self.txDstFileName.dragEnterEvent = lambda e: self.qtTextEdit.DragEnterEvent(e)
        self.txDstFileName.dropEvent = lambda e:self.qtTextEdit.DragEvent_FileName(self.txDstFileName, e)

        self.txObjFileName.focusOutEvent = lambda e:self.dstETConfig.updateConfigSetting()
        self.txDstFilePath.focusOutEvent = lambda e:self.dstETConfig.updateConfigSetting()
        self.txDstFileName.focusOutEvent = lambda e:self.dstETConfig.updateConfigSetting()


        self.cbDstFilePath.focusOutEvent = lambda e:self.dstETConfig.updateConfigSetting()
        self.cbDstFileName.focusOutEvent = lambda e:self.dstETConfig.updateConfigSetting()
        self.cbDstFileOverWrite.focusOutEvent = lambda e:self.dstETConfig.updateConfigSetting()
        self.Form.closeEvent = lambda e:self.closeEvent(e)
        return
    
    def closeEvent(self, event: QCloseEvent|None ):
        """
        -----------------------------------------------------------------
        BinaryConverterToolツールクロスイベント\n
        -----------------------------------------------------------------
        """
        self.dstETConfig.updateConfigSetting()
        self.dstETConfig.outputConfigSetting()
        return
    
    
class BinaryConverterTool(QDialog):
    DstFullFileNameList:list[str] =[]
    def __init__(self,parent=None):
        super(BinaryConverterTool, self).__init__(parent)
        
        # 本ツールGUI画面設定
        self.ui = Ui_BinaryConverterTool()
        self.ui.setupUi(self)
        self.ui.addUiSetting(self)
        
        self.FileSysProcess = FileSysProcess()
        self.qtBoxLib = qtBoxLib()
        
        # 本ツールソフトバジョンGUI画面設定
        self.verInfo = BinaryConverterTool_VerGUI()
        self.BiConverterLib = BinaryConverterLib()
        self.ui.dstETConfig.updateGUISetting()
        self.ui.actionGUI_Update()
        self.cbDstFileName_Click()
        
        # スロットコネクト処理
        self.guiSlotConnect()

        self.rbSpecMemType_Click()
        return


    #スロットコネクト処理
    def guiSlotConnect(self) -> None:
        """
        -----------------------------------------------------------------
        スロットコネクト処理\n
        -----------------------------------------------------------------
        """
        # BinaryConverterToolについて
        self.ui.actionAboutDstDecodeTool.triggered.connect(self.actionAboutPdfEditorTool_Click)
        # その他(未使用)
        self.ui.actionOther.triggered.connect(self.actionOther_Click)

        # 対象ファイル選択処理
        self.ui.btObjFileName.clicked.connect(self.btobjFileName_Click)
        #メモリエリア指定判断処理
        self.ui.cbSpecMemRange.clicked.connect(self.cbSpecMemRange_Click)
        self.ui.rbSpecMemSize.clicked.connect(self.rbSpecMemType_Click)
        self.ui.rbSpecEndAddr.clicked.connect(self.rbSpecMemType_Click)

        # 対象ファイルアドレス変更処理
        self.ui.txObjFileName.textChanged.connect(self.txDstFilePath_Update)
        self.ui.txObjFileName.textChanged.connect(self.txDstFileName_Update)
        self.ui.txObjFileName.textChanged.connect(self.txObjFileName_textChanged)
        # 生成ファイルパス手入力判断処理
        self.ui.cbDstFilePath.toggled.connect(self.cbDstFilePath_Click)
        # 生成ファイルパス選択処理
        self.ui.btDstFilePath.clicked.connect(self.btDstFilePath_Click)
        # 生成ファイル名称手入力判断処理
        self.ui.cbDstFileName.toggled.connect(self.cbDstFileName_Click)

        # 【ファイルへ生成処理】
        self.ui.btDstFileProcess.clicked.connect(self.btDstFileProcess_Click)

        return


    def btobjFileName_Click(self) -> None:
        """
        -----------------------------------------------------------------
        対象ファイル選択処理\n
        -----------------------------------------------------------------
        """
        objFullFileAddr = self.ui.txObjFileName.toPlainText()
        objFullFileAddr = objFullFileAddr.strip(" ")
        self.ui.btObjFileName.setEnabled(False)
        objFullFileAddr = self.qtBoxLib.GetBinFileName(objFullFileAddr)

        self.ui.btObjFileName.setEnabled(True)
        self.ui.txObjFileName.setText(objFullFileAddr)

        self.txDstFilePath_Update()
        self.txDstFileName_Update()
        return

    def cbSpecMemRange_Click(self) -> None:
        """
        -----------------------------------------------------------------
        メモリエリア指定判断処理\n
        -----------------------------------------------------------------
        """
        if (self.ui.cbSpecMemRange.isChecked()):
            self.rbSpecMemType_Click()
            self.ui.gbSpecMemType.setHidden(False)

            self.ui.gbSpecMemRange.setHidden(False)
            self.ui.txStartAddr.setEnabled(True)
            self.ui.txMemorySize.setEnabled(True)
        else:
           self.ui.gbSpecMemType.setHidden(True)

           self.ui.gbSpecMemRange.setHidden(True)
           self.ui.txStartAddr.setEnabled(False)
           self.ui.txMemorySize.setEnabled(False)
        return
    
    def rbSpecMemType_Click(self) -> None:
        """
        -----------------------------------------------------------------
        メモリエリアタイプ判断処理\n
        -----------------------------------------------------------------
        """
        if (self.ui.rbSpecMemSize.isChecked()):
            strMemroyType = self.ui.rbSpecMemSize.text()
        else:
            strMemroyType = self.ui.rbSpecEndAddr.text()
        strMemroyType = strMemroyType.replace('【', '').replace('】', '')
        strMemoryTypeList = strMemroyType.split('/')
        self.ui.lbStartAddr.setText(strMemoryTypeList[0])
        self.ui.lbMemorySize.setText(strMemoryTypeList[1])
        return

    def cbDstFilePath_Click(self) -> None:
        """
        -----------------------------------------------------------------
        生成結果ファイルパス手入力判断処理\n
        -----------------------------------------------------------------
        """
        if (self.ui.cbDstFilePath.isChecked()):
            self.ui.txDstFilePath.setEnabled(True)
            self.ui.btDstFilePath.setEnabled(True)
        else:
           self.ui.txDstFilePath.setEnabled(False)
           self.ui.btDstFilePath.setEnabled(False)
           self.txDstFilePath_Update()
        return


    def btDstFilePath_Click(self) -> None:
        """
        -----------------------------------------------------------------
        生成結果ファイルパス選択処理\n
        -----------------------------------------------------------------
        """
        pdfFilePath = self.ui.txDstFilePath.toPlainText()
        pdfFilePath = pdfFilePath.strip(" ")
        self.ui.btDstFilePath.setEnabled(False)
        pdfFilePath = self.qtBoxLib.getFilePathByPathDialog(pdfFilePath)
        self.ui.btDstFilePath.setEnabled(True)
        self.ui.txDstFilePath.setText(pdfFilePath)
        return


    def cbDstFileName_Click(self) -> None:
        """
        -----------------------------------------------------------------
        生成結果ファイル名称手入力判断処理\n
        -----------------------------------------------------------------
        """
        if (self.ui.cbDstFileName.isChecked()):
            self.ui.txDstFileName.setEnabled(True)
        else:
           self.ui.txDstFileName.setEnabled(False)
           self.txDstFileName_Update()
        return


    def txDstFilePath_Update(self) -> None:
        """
        -----------------------------------------------------------------
        生成結果ファイルパス内容更新処理\n
        -----------------------------------------------------------------
        """
        if (self.ui.cbDstFilePath.isChecked()):
            return

        objFullFileAddr = self.ui.txObjFileName.toPlainText()
        objFullFileAddr = objFullFileAddr.strip(" ")

        resultList = self.FileSysProcess.getDirByFileFullAddr(objFullFileAddr)

        if resultList[0] == False :
            return
        self.ui.txDstFilePath.setText(resultList[1])
        return


    def txDstFileName_Update(self) -> None:
        """
        -----------------------------------------------------------------
        生成結果ファイル名称内容更新処理\n
        -----------------------------------------------------------------
        """
        if (self.ui.cbDstFileName.isChecked()):
            return

        objFullFileAddr = self.ui.txObjFileName.toPlainText()
        objFullFileAddr = objFullFileAddr.strip(" ")

        bResult = self.FileSysProcess.judgeFileExsit(objFullFileAddr)
        if ( bResult  == False ) :
            return

        objFileName: list[str]  = []
        bResult = self.FileSysProcess.getFileNameInfoByFileFullAddr(objFullFileAddr, objFileName)
        if ( bResult  == False ) :
            return

        self.ui.txDstFileName.setText(objFileName[1])

        return
    
    
    def txObjFileName_textChanged(self) -> None:
        """
        -----------------------------------------------------------------
        生成結果ファイル内容変更処理\n
        -----------------------------------------------------------------
        """
        objFullFileAddr = self.ui.txObjFileName.toPlainText()
        objFullFileAddr = objFullFileAddr.strip(" ")
        
        bResult = self.FileSysProcess.judgeFileExsit(objFullFileAddr)
        if ( bResult  == False ) :
            return

        objFileName: list[str]  = []
        bResult = self.FileSysProcess.getFileNameInfoByFileFullAddr(objFullFileAddr, objFileName)
        if ( bResult  == False ) :
            return
        
        return



    def btDstFileProcess_Click(self) -> None:
        """
        -----------------------------------------------------------------
        ツール実施処理\n
        -----------------------------------------------------------------
        """
        self.ui.btDstFileProcess.setEnabled(False)
        # GUI画面更新処理
        QApplication.processEvents()

        #GUI入力内容判定処理
        bResult:bool = self.btDstFileProcess_CheckGUISetting()
        if ( bResult  == False ) :
            self.ui.btDstFileProcess.setEnabled(True)
            return
        
        msgTitle = self.ui.Form_SetWindowTitle
        objFileName= self.ui.txObjFileName.toPlainText() #対象ファイルアドレス内容取得
        DstFilePath= self.ui.txDstFilePath.toPlainText() #生成ファイルパス内容取得
        DstFileName= self.ui.txDstFileName.toPlainText() #生成ファイル名称内容取得
        
        #ファイルアドレス設定
        DstFullFileName = DstFilePath + '\\' + DstFileName
        if DstFilePath[len(DstFilePath) - 1:]  == '\\' :
            DstFullFileName = DstFilePath + DstFileName
        
        self.DstFullFileNameList.clear()
        self.DstFullFileNameList.append(DstFullFileName + '.txt')
        if self.ui.cb2ExcelFile.isChecked() :
            self.DstFullFileNameList.append(DstFullFileName + '.xlsx')
        bResultList = self.FileSysProcess.judgeFilesExsit(self.DstFullFileNameList,True)
        if len(bResultList) != 0:
            DstExsitFileList:list[str] = []
            for FileAddrInfo in bResultList:
                DstExsitFileList.append(FileAddrInfo[1])
            if ( not self.ui.cbDstFileOverWrite.isChecked() ) :
                bResult = self.qtBoxLib.JudgeOverWriteFiles(DstExsitFileList, msgTitle)
                if ( bResult  == False ) :
                    self.ui.btDstFileProcess.setEnabled(True)
                    return

            if ( bResult  == True ) :
                for DstExsitFile in DstExsitFileList:
                    bResult = self.qtBoxLib.delFile(DstExsitFile, msgTitle)
                    if ( bResult  == False ) :
                        self.ui.btDstFileProcess.setEnabled(True)
                        return
        self.DstFileProcess(objFileName)

        return

    
    def DstFileProcess(self, srcFileName:str) -> None:
        """
        -----------------------------------------------------------------
        対象ファイルへ生成処理\n
        【引数 】\n
            srcFileName:対象ファイルアドレス\n
        【戻り値】無し\n
        -----------------------------------------------------------------
        """
        msgTitle:str = self.ui.Form_SetWindowTitle
        msgStr:str = ""

        #【メモリエリア指定(Hex)】判定処理
        if self.ui.cbSpecMemRange.isChecked():
            startAddr = int(self.ui.txStartAddr.toPlainText(), 16)
            startSize = int(self.ui.txMemorySize.toPlainText(), 16)
            if self.ui.rbSpecEndAddr.isChecked():
                startSize = startSize - startAddr + 1
        else :
            startAddr = -1
            startSize = -1
  
        #SPIDecodeLib処理
        bResult:bool = self.BiConverterLib.BinaryConverterLib_Process(srcFileName, self.DstFullFileNameList, startAddr, startSize)

        if ( bResult  == False ) :
            msgStr = "ファイル変換失敗\n"
            msgStr += "変換失敗理由:\n"
            msgStr += "下記のファイルが解析失敗、ファイル内容が正しいかどうかをご確認ください\n"
            msgStr += srcFileName
            self.qtBoxLib.showErrMsgBoxInfo(msgTitle, msgStr)
        else:
            msgStr = "生成結果は以下通りです。\n"
            msgStr += "生成ファイル名称：\n    "
            for DstFullFileName in self.DstFullFileNameList:
                msgStr += DstFullFileName + "\n    "
            self.qtBoxLib.showStdMsgBoxInfo( msgTitle, msgStr )
        
        self.ui.btDstFileProcess.setEnabled(True)
        return

    def btDstFileProcess_CheckGUISetting(self) -> bool:
        """
        -----------------------------------------------------------------
        GUI入力内容判定処理\n
        -----------------------------------------------------------------
        """
        msgTitle:str = self.ui.Form_SetWindowTitle
        msgObjFileName =  "【" + self.ui.lbObjFileName.text() + "】"
        msgDstFilePath =  "【" + self.ui.lbDstFilePath.text() + "】"
        msgDstFileName =  "【" + self.ui.lbDstFileName.text() + "】"
        bResult:bool = False
        
        #【対象ファイルアドレス】内容取得
        objFileName = self.ui.txObjFileName.toPlainText()
        bResult = self.qtBoxLib.judgeFileExsit(objFileName, msgTitle, msgObjFileName)
        self.ui.txObjFileName.setText(objFileName)
        if ( bResult  == False ) :
            return bResult

        #【メモリエリア指定(Hex)】判定処理
        if self.ui.cbSpecMemRange.isChecked():
            strCharacter = self.ui.txStartAddr.toPlainText()
            lbStartAddrName = "【" + self.ui.lbStartAddr.text() + "】"
            bResult = self.qtBoxLib.judgeHexCharacter(strCharacter, msgTitle, lbStartAddrName)
            if bResult  == False :
                return bResult
            
            strCharacter = self.ui.txMemorySize.toPlainText()
            lbMemorySizeName = "【" + self.ui.lbMemorySize.text() + "】"
            bResult = self.qtBoxLib.judgeHexCharacter(strCharacter, msgTitle, lbMemorySizeName)
            if bResult  == False :
                return bResult
            if self.ui.rbSpecEndAddr.isChecked() :
                startAddr = int(self.ui.txStartAddr.toPlainText(), 16)
                endAddr =   int(self.ui.txMemorySize.toPlainText(), 16)
                if endAddr < startAddr:
                    msgStr = lbMemorySizeName +'設定値は'  + lbStartAddrName + 'より小さい'
                    self.qtBoxLib.showErrMsgBoxInfo(msgTitle, msgStr)
                    return False

        #【生成ファイルパス】内容取得
        pdfFilePath = self.ui.txDstFilePath.toPlainText()
        bResult = self.qtBoxLib.judgeDirExsit(pdfFilePath, msgTitle, msgDstFilePath)
        if bResult  == False :
            return bResult

        #【生成ファイル名称】内容取得
        pdfFileName = self.ui.txDstFileName.toPlainText()
        bResult = self.qtBoxLib.judgeIllegalCharacter(pdfFileName, msgTitle, msgDstFileName)
        if bResult  == False :
            return bResult
        
        return bResult

    
    # BinaryConverterToolについて処理
    def actionAboutPdfEditorTool_Click(self) -> None:
        """
        -----------------------------------------------------------------
        BinaryConverterToolについて処理\n
        -----------------------------------------------------------------
        """
        self.verInfo.show()

    def actionOther_Click(self) -> None:
        #self.pdfInfo.show()
        return
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BinaryConverterTool()
    window.show()
    sys.exit(app.exec_())
