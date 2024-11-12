import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui import errorUI, mainUi , producerCreated
from crud import propetyCrud , propietaryCrud
from models import propety, propietary


class Main(QMainWindow, mainUi.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.addProducer)

    def getInformationFromProducer(self):
        document = self.lineEdit.text()
        name = self.lineEdit_2.text()
        lastName = self.lineEdit_4.text()
        email = self.lineEdit_3.text()
        phone = self.lineEdit_5.text()

        return propietary.propietary(document,name ,lastName , email, phone)
    

    def getInformationFromPropety(self):
        crop = self.comboBox.currentText()
        castralRegister = self.lineEdit_6.text()
        municipality = self.comboBox_7.currentText()

    def addProducer(self):
        producer = self.getInformationFromProducer()
        if propietaryCrud.propietaryCrud.searchPropietaryByDocument(producer.document):
            error = errorUI.Ui_Error()
            error.show()
        else:
            propietaryCrud.propietaryCrud.createProducer(producer)
            done = producerCreated.Ui_producerCreated()
            done.show()
          

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
