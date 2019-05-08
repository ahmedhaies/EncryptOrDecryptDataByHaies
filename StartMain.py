# this source is programmed by AhmedHaies
# facebook is http://fb.com/ahmed.haies
from PyQt5 import QtWidgets
from PyQt5.Qt import QFileDialog, QMessageBox, QFontDatabase
from PyQt5.QtCore import QThread, pyqtSignal
from MainGui import Ui_EncryptOrDecryptFilesHaies
from Cryptodome.Cipher import AES
import sys
import os
import os.path

class AppWindowByHaies(QtWidgets.QMainWindow, Ui_EncryptOrDecryptFilesHaies):
    def __init__(self, parent = None):
        super(AppWindowByHaies, self).__init__(parent)
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.HandelButton()

    ## to handel all button
    def HandelButton(self):
        self.toolButtonSelectFile.clicked.connect(self.SelectFile)
        self.toolButtonSelectFolder.clicked.connect(self.SelectFolder)
        self.pushButtonOk.clicked.connect(self.SetOk)
        self.actionExit.triggered.connect(self.Exit)
        self.actionHelp.triggered.connect(self.Help)
        self.radioButtonEncrypt.clicked.connect(self.CheckedEncrypt)
        self.radioButtonDecrypt.clicked.connect(self.CheckedDecrypt)

    ## opration
    def Help(self):
        QMessageBox.information(self, "مساعدة", "تمت برمجة هذا البرنامج بواسطة <strong>أحمد حايس</strong><br>سكايب : <strong>ahmed.haies</strong><br>رقم الموبايل : <strong>01061840978</strong>")

    def Exit(self):
        self.close()

    def CheckedEncrypt(self):
        if len(self.lineEditSelected.text()) > 0 and not os.path.isdir(self.lineEditSelected.text()) and self.lineEditSelected.text().split(".")[-1] == 'Haies':
            self.lineEditSelected.setText(self.lineEditSelected.text().strip(".Haies"))

    def CheckedDecrypt(self):
        if len(self.lineEditSelected.text()) > 0 and not os.path.isdir(self.lineEditSelected.text()) and self.lineEditSelected.text().split(".")[-1] != 'Haies':
            self.lineEditSelected.setText(self.lineEditSelected.text()+".Haies")

    def SelectFile(self):
        file = []
        if self.radioButtonDecrypt.isChecked():
            file = QFileDialog.getOpenFileName(self, "حدد ملف", "", "*.Haies")
        else:
            file = QFileDialog.getOpenFileName(self, "حدد ملف", "", "")
        self.lineEditSelected.setText(file[0])

        if len(self.lineEditSelected.text()) > 0 and os.path.isfile(self.lineEditSelected.text()) and self.lineEditSelected.text().split(".")[-1] == 'Haies':
            self.radioButtonDecrypt.setChecked(True)

    def SelectFolder(self):
        folder = QFileDialog.getExistingDirectory(self, "حدد مجلد", "",QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.lineEditSelected.setText(folder)

    def HandlingCondtion(self):
        if len(self.lineEditSelected.text()) <= 0:
            QMessageBox.warning(self, "خطأ", "يجب أن تحدد ملف أو مجلد")
            return False

        if len(self.lineEditPassword.text()) <= 5:
            QMessageBox.warning(self, "خطأ", "يجب أن تكون كلمة السر أكبر من 5 أحرف أو أرقام")
            return False

        if len(self.lineEditPassword.text()) > 16:
            QMessageBox.warning(self, "خطأ", "يجب أن تكون كلمة السر أقل من 16 حرف أو رقم")
            return False

        if self.lineEditPassword.text() != self.lineEditConfPassword.text():
            QMessageBox.warning(self, "خطأ", "يجب أن يكون كلمتا السر في الخانتين متساويتين")
            return False

        if not os.path.exists(self.lineEditSelected.text()):
            QMessageBox.warning(self, "خطأ", "هذا المجلد أو هذا الملف غير موجود")
            return False

        return True

    def SetOk(self):
        if not self.HandlingCondtion():
            return
        if self.radioButtonEncrypt.isChecked():
            if os.path.isfile(self.lineEditSelected.text()) and self.lineEditSelected.text().split(".")[-1] == 'Haies':
                QMessageBox.warning(self, "خطأ", "هذا الملف مشفر من قبل")
                return
            quiz = QMessageBox.question(self, "تشفير",
                                        "هل تريد تشفير {0}".format(self.lineEditSelected.text()),
                                        QMessageBox.Yes | QMessageBox.No)
            if quiz == QMessageBox.No:
                return
            self.pushButtonOk.setEnabled(False)
            self.StartDecryptOrEncrypt = HaiesThread(self, self.lineEditSelected.text(), 1, self.lineEditPassword.text())
            self.StartDecryptOrEncrypt.progress_update.connect(self.PrograssBarUpdate)
            self.StartDecryptOrEncrypt.progress_updateForEncDec.connect(self.PrograssBarForEncOrDecUpdate)
            self.StartDecryptOrEncrypt.start()

        elif self.radioButtonDecrypt.isChecked():
            if os.path.isfile(self.lineEditSelected.text()) and self.lineEditSelected.text().split(".")[-1] != 'Haies':
                QMessageBox.warning(self, "خطأ", "هذا الملف غير مشفر")
                return

            quiz = QMessageBox.question(self, "فك التشفير", "هل تريد فك تشفير {0}".format(self.lineEditSelected.text()), QMessageBox.Yes | QMessageBox.No)
            if quiz == QMessageBox.No:
                return
            self.pushButtonOk.setEnabled(False)
            self.StartDecryptOrEncrypt = HaiesThread(self, self.lineEditSelected.text(), 2, self.lineEditPassword.text())
            self.StartDecryptOrEncrypt.progress_update.connect(self.PrograssBarUpdate)
            self.StartDecryptOrEncrypt.progress_updateForEncDec.connect(self.PrograssBarForEncOrDecUpdate)
            self.StartDecryptOrEncrypt.start()
        else:
            QMessageBox.warning(self, "خطأ", "يجب أن تختار من بين تشفير أو فك التشفير")

    def PrograssBarUpdate(self, Value):
        if Value == 100:
            self.pushButtonOk.setEnabled(True)
            QMessageBox.information(self, "إكتمال", "لقد تم إكمال هذه العملية")
            self.progressBarForCountFile.setValue(0)
        self.progressBarForCountFile.setValue(Value)

    def PrograssBarForEncOrDecUpdate(self, Value):
        if Value == 100:
            self.progressBarForEncOrDec.setValue(0)
            return
        self.progressBarForEncOrDec.setValue(int(self.progressBarForEncOrDec.value())+Value)

class HaiesThread(QThread):
    progress_update = pyqtSignal(int)
    progress_updateForEncDec = pyqtSignal(int)
    def __init__(self, Self, Dir, Method, PassWord):
        QThread.__init__(self)
        self.Dir = Dir
        self.Method = Method
        self.PassWord = PassWord
        self.Self = Self

    def GetFileList(self, DirHaies, TypeHaies):
        Ext = ['Haies']
        if TypeHaies == 1:
            Ext = [
                # 'exe', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',  # SYSTEM FILES [danger]
                'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',  # Microsoft office
                'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md',
                # OpenOffice, Adobe, Latex, Markdown, etc
                'yml', 'yaml', 'json', 'xml', 'csv',  # structured data
                'db', 'sql', 'dbf', 'mdb', 'iso',  # databases and disc images
                'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css',  # web technologies
                'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx',  # C source code
                'java', 'class', 'jar',  # java source code
                'ps', 'bat', 'vb',  # windows based scripts
                'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',  # linux/mac based scripts
                'go', 'py', 'pyc', 'bf', 'coffee',  # other source code files
                'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', 'tga', 'dds',  # images
                'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape',  # music and sound
                'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',  # Video and movies
                'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak', 'apk'
            ]
        FilesList = []
        for dir, sd, files in os.walk(DirHaies):
            for file_name in files:
                full_path = os.path.join(dir, file_name)
                ex = full_path.split(".")[-1]
                if ex in Ext:
                    FilesList.append(full_path)
        return FilesList

    def Align(self, text):
        return text + (16 - len(text) % 16) * "h"

    def HandlingKeyOrIv(self, KeyOrIv):
        if len(KeyOrIv) > 16:
            KeyOrIv = KeyOrIv.read(16).encode()
        elif len(KeyOrIv) < 16:
            KeyOrIv = self.Align(KeyOrIv).encode()
        elif len(KeyOrIv) == 16:
            KeyOrIv = KeyOrIv.encode()
        return KeyOrIv

    def Encrypt(self, File, Layer=7, BlockSize=16, Key="ahmedhaies", Iv="ahmedhaies"):
        Key = self.HandlingKeyOrIv(Key)
        Iv = self.HandlingKeyOrIv(Iv)
        Crypt = AES.new(Key, AES.MODE_OFB, Iv)
        with open(File, "r+b") as f:
            text = f.read(BlockSize)
            while text:
                f.seek(-len(text), 1)
                EncLayer = Crypt.encrypt(text)
                for x in range(0, Layer):
                    EncLayer = Crypt.encrypt(EncLayer)
                f.write(EncLayer)
                self.progress_updateForEncDec.emit(BlockSize)
                text = f.read(BlockSize)
        os.rename(File, File + ".Haies")
        f.close()
        self.progress_updateForEncDec.emit(100)

    def Decrypt(self, File, Layer=7, BlockSize=16, Key="ahmedhaies", Iv="ahmedhaies"):
        Key = self.HandlingKeyOrIv(Key)
        Iv = self.HandlingKeyOrIv(Iv)
        Decrypt = AES.new(Key, AES.MODE_OFB, Iv)
        with open(File, "r+b") as f:
            text = f.read(BlockSize)
            while text:
                f.seek(-len(text), 1)
                DecLayer = Decrypt.decrypt(text)
                for x in range(0, Layer):
                    DecLayer = Decrypt.decrypt(DecLayer)
                f.write(DecLayer)
                self.progress_updateForEncDec.emit(BlockSize)
                text = f.read(BlockSize)
        os.rename(File, File.strip(".Haies"))
        f.close()
        self.progress_updateForEncDec.emit(100)

    def run(self):
        if os.path.isdir(self.Dir):
            FilesList = self.GetFileList(self.Dir, int(self.Method))
            self.Self.progressBarForCountFile.setMaximum(len(FilesList))
            for File in FilesList:
                if os.path.exists(File):
                    self.Self.progressBarForEncOrDec.setMaximum(int(os.path.getsize(File)))
                    self.progress_update.emit(FilesList.index(File) + 1)
                    if int(self.Method) == 1:
                        self.Encrypt(File, Key=self.PassWord)
                    elif int(self.Method) == 2:
                        self.Decrypt(File, Key=self.PassWord)
        elif os.path.isfile(self.Dir):
            self.Self.progressBarForEncOrDec.setMaximum(int(os.path.getsize(self.Dir)))
            if int(self.Method) == 1:
                self.Encrypt(self.Dir, Key=self.PassWord)
            elif int(self.Method) == 2:
                self.Decrypt(self.Dir, Key=self.PassWord)
        self.progress_update.emit(100)

def main():
    app = QtWidgets.QApplication(sys.argv)
    fontDB = QFontDatabase()
    fontDB.applicationFontFamilies(fontDB.addApplicationFont(":/res/Harmattan.ttf"))
    application = AppWindowByHaies()
    application.show()
    app.exec_()

if __name__ == "__main__":
    main()
