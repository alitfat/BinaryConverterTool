import copy
from Lib.FileSysProcess import FileSysProcess
from Lib.ExcelLib import ExcelLib
from Lib.StrLib import StrLib

from openpyxl.styles.borders import Border, Side,BORDER_THIN, BORDER_DOTTED
from openpyxl.styles.colors import BLACK

memoryBorderL1 = Border(top=Side(style=BORDER_THIN, color=BLACK), 
                        bottom=Side(style=BORDER_THIN, color=BLACK), 
                        left=Side(style=BORDER_THIN, color=BLACK),
                        right=Side(style=BORDER_DOTTED, color=BLACK))
memoryBorderL2 = Border(top=Side(style=BORDER_THIN, color=BLACK), 
                        bottom=Side(style=BORDER_THIN, color=BLACK), 
                        left=Side(style=BORDER_DOTTED, color=BLACK),
                        right=Side(style=BORDER_DOTTED, color=BLACK))
memoryBorderL3 = Border(top=Side(style=BORDER_THIN, color=BLACK), 
                        bottom=Side(style=BORDER_THIN, color=BLACK), 
                        left=Side(style=BORDER_DOTTED, color=BLACK),
                        right=Side(style=BORDER_DOTTED, color=BLACK))
memoryBorderL4 = Border(top=Side(style=BORDER_THIN, color=BLACK), 
                        bottom=Side(style=BORDER_THIN, color=BLACK), 
                        left=Side(style=BORDER_DOTTED, color=BLACK),
                        right=Side(style=BORDER_THIN, color=BLACK))

class BinaryConverterLib(object):
    
    def __init__(self)->None:
        super(BinaryConverterLib, self).__init__()
        self.FileSysProcess = FileSysProcess()
        self.StrLib = StrLib()
        self.ExcelLib = ExcelLib() 
        return
    
    def BinaryConverterLib_Process(self, srcFileAddr:str, dstFileAddrList:list[str], startAddr:int = -1, MemorySize:int = -1) -> bool:
        """
        --------------------------------------------------
        BinaryConverterLib処理\n
        【引数 】\n
            srtFileAddr:読取対象ファイル\n
            dstFileAddrList:生成結果対象ファイル\n
            startAddr:開始アドレス\n
            MemorySize:メモリサイズ\n
        【戻り値】\n
            bool:処理結果\n
        --------------------------------------------------
        """
        fileBinDataList:dict[int, list[int]] ={}
        dstMemoryDataList:dict[str, list[str]] ={}
        dstFileComment:list[str] = []

        #対象ファイル内容取得処理
        srcfileComment = self.FileSysProcess.getBinFileComment(srcFileAddr, startAddr, MemorySize)
        if srcfileComment is None:
            return False
        
        #対象ファイルからメモリ内容取得
        self.__analyseSrcData(srcfileComment, fileBinDataList, startAddr)

        #出力メモリ内容フォーマット作成
        self.__createMemoryList(fileBinDataList, dstMemoryDataList)

        #メモリテキスト出力フォーマット作成
        self.__createMemoryTextFile(dstMemoryDataList, dstFileComment)
        #メモリテキストファイル出力
        bResult = self.FileSysProcess.writeFileComment(dstFileAddrList[0], dstFileComment)

        if len(dstFileAddrList) >= 2 :
            #Excelファイル出力
            bResult = self.__CreateExcelFile(dstFileAddrList[1], dstMemoryDataList)
        return bResult
    
    def __analyseSrcData(self,srcfileComment:bytes, fileBinDataList:dict[int, list[int]], startAddr:int = -1) -> None:
        if startAddr == -1:
            fileAddr = 0
        else:
            fileAddr = startAddr
        
        rowDecData:list[int] = []
        fileBinDataList.clear()
        index = 0
        for fileBinData in srcfileComment:
            if index == 16:
                index = 0
                fileAddr += 16
                rowDecData.clear()
            rowDecData.append(int(fileBinData))
            if index == 15:
                fileBinDataList[fileAddr] = copy.deepcopy(rowDecData)
            index += 1
        fileBinDataList[fileAddr] = copy.deepcopy(rowDecData)
        return
    
    def __createMemoryList(self,fileBinDataList:dict[int, list[int]], dstMemoryDataList:dict[str, list[str]] ) -> None:
        dstMemoryDataList.clear()
        rowStrData:list[str] = []
        for decAddress, rowDecData in fileBinDataList.items():
            hexAddress = format(decAddress, "06X")
            rowStrData.clear()
            for decData in rowDecData:
                rowStrData.append(format(decData, "02X"))
            dstMemoryDataList[hexAddress] = copy.deepcopy(rowStrData)
        return
    
    def __createMemoryTextFile(self, dstMemoryDataList:dict[str, list[str]], textFileComment:list[str]) -> None:
        textFileComment.clear()
        #タイトル作成
        lineStr = 'Address\t'
        lineStr += '00\t'+'01\t'+'02\t'+'03\t'+'04\t'+'05\t'+'06\t'+'07\t'
        lineStr += '08\t'+'09\t'+'0A\t'+'0B\t'+'0C\t'+'0D\t'+'0E\t'+'0F\n'
        textFileComment.append(lineStr)
        #メモリデータ内容取得
        for address, valueList in dstMemoryDataList.items():
            lineStr = address + "\t"
            for value in valueList:
                lineStr += value + "\t"
            lineStr =lineStr[:-1]
            lineStr +="\n"
            textFileComment.append(lineStr)
        return
    
    def __CreateExcelFile(self,dstFileAddr:str, dstMemoryDataList:dict[str, list[str]]) ->bool:
        #ExcelFile作成
        bResult = self.ExcelLib.createExcelFile(dstFileAddr)
        bResult = self.ExcelLib.setWorkSheet()
        fileName:list[str] = []
        self.FileSysProcess.getFileNameInfoByFileFullAddr(dstFileAddr,fileName)

        #Memoryシート作成
        self.ExcelLib.modifySheetName(dstSheetName=fileName[1])
        self.__CreateExcelFile_MemoryDataSheet(dstMemoryDataList)
        #ExcelFile保存
        self.ExcelLib.save()
        return True
    
    def __CreateExcelFile_MemoryDataSheet(self,dstMemoryDataList:dict[str, list[str]]) ->None:
        #タイトル作成
        rowIndex = 2
        colIndex = 2
        self.ExcelLib.addCellValue(rowIndex,colIndex,'Address')
        colIndex += 1
        colDataIndex = 0
        while(colDataIndex < 16):
            self.ExcelLib.addCellValue(rowIndex,colIndex,format(colDataIndex, "02X"))
            colIndex += 1
            colDataIndex += 1
        
        #列幅設定
        self.ExcelLib.setColumnsWidth(2,2, 9)
        self.ExcelLib.setColumnsWidth(3,18, 3.5)

        #メモリデータ内容出力
        for address, valueList in dstMemoryDataList.items():
            rowIndex += 1
            colIndex = 2
            self.ExcelLib.addCellValue(rowIndex,colIndex, address)
            colIndex += 1
            for value in valueList:
                self.ExcelLib.addCellValue(rowIndex,colIndex, value)
                colIndex += 1

        #枠線設定
        self.ExcelLib.setBorder(2,rowIndex, 2, 2)
        self._SetRowAddrDataBorder(2, rowIndex, 3)

        #タイトル背景色設定
        colorValue = 'B4E6A0'
        self.ExcelLib.setBackGroundColor(2, 2, 18, colorValue)
        colorValue = 'C0C0C0'
        if colIndex != 19:
            self.ExcelLib.setBackGroundColor(rowIndex, colIndex, 18, colorValue)
        return
    

    def _SetRowAddrDataBorder(self, startRowIndex:int, endRowIndex:int, columnIndex:int) ->None:
        self.__SetAddrDataBorder(startRowIndex, endRowIndex, columnIndex)
        columnIndex += 4
        self.__SetAddrDataBorder(startRowIndex, endRowIndex, columnIndex)
        columnIndex += 4
        self.__SetAddrDataBorder(startRowIndex, endRowIndex, columnIndex)
        columnIndex += 4
        self.__SetAddrDataBorder(startRowIndex, endRowIndex, columnIndex)
        return

    def __SetAddrDataBorder(self, startRowIndex:int, endRowIndex:int, columnIndex:int) ->None:
        rowIndex = endRowIndex
        self.ExcelLib.setBorder(startRowIndex, rowIndex, columnIndex, columnIndex, memoryBorderL1)
        columnIndex += 1
        self.ExcelLib.setBorder(startRowIndex, rowIndex, columnIndex, columnIndex, memoryBorderL2)
        columnIndex += 1
        self.ExcelLib.setBorder(startRowIndex, rowIndex, columnIndex, columnIndex, memoryBorderL3)
        columnIndex += 1
        self.ExcelLib.setBorder(startRowIndex, rowIndex, columnIndex, columnIndex, memoryBorderL4)
        return
