#05.05.2023 3'lü su tankının raspberry pi tabanlı kontrolü arayüzü, EÇ
import sys 
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import * 
#butonların görünüşlerini belirliyoruz
Style = """
    QWidget{
        background: white;
    }
    QLabel{
        font: 12pt "MS Sans Serif";
        font-weight:bold;
        color: rgb(0,0,0); 
    }

    QLineEdit{
        font: 10pt "MS Reference Sans Serif";
        font-weight:normal;
        border: None;
        border:2px solid rgb(243,243,243);
        border-radius: 5px;
    }
    QLineEdit:focus{
        border:none;
        border:2px solid rgb(66,163,223);
    }
    QPushButton{
        font: 10pt "MS Reference Sans Serif";
        font-weight:normal;
        text-align: center;
        background-color:white;
    }
    QPushButton:pressed{
        padding-left:1px;
        padding-top:1px;
    }
    QProgressBar {
        border: 2px solid grey;
        color: black ;
        border-radius: 5px;
        text-align: center;
}
    QProgressBar::chunk {
        background-color: rgb(100, 200, 255);
        border-bottom-right-radius: 3px;
        border-bottom-left-radius: 3px;

}
    QMenuBar {
        background-color:rgba(0,0,0,0);
        border:none;
        border-bottom:2px solid rgba(105,118,132,255);
        padding-bottom:7px;
            }
    QMenuBar::item {
        background-color:rgba(0,0,0,0);
        border:none;
        border-bottom:2px solid rgba(105,118,132,255);
        padding-bottom:7px;
        }


    QMenu
{
        background-color:rgba(0,0,0,0);
        border:none;
        border-bottom:2px solid rgba(105,118,132,255);
        padding-bottom:7px;
}
    QMenu::item::selected
{
        padding-left:5px;
        padding-top:5px;
        background-color:rgba(100,200,255,255);
}
"""
#giriş penceresi
class Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
#pencere boyutları tahmini ekran büyüklüğüne göre uygulanmıştır,pencere adı eklenmiş ve show komutuyla pencere açılmıştır
        self.setGeometry(200,200,650,300)
        self.setWindowTitle("3'lü Su Tankının Raspberry Pi Tabanlı Kontrolü")
        #ikinci pencereden alınan değerler,saçma ama çalışıyor
        self.L1 = 0
        self.L3 = 0 
        #arayüzde bulunan katmanlar
        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.helper1_layout = QtWidgets.QVBoxLayout()
        self.helper2_layout = QtWidgets.QHBoxLayout()

        #wigetların belirlenmesi ve özellikleri
        #kullanıcı için açıklamalar
        self.kullanici_adi = QtWidgets.QLabel("Kullanıcı Adı")
        self.kullanici_adi.setAlignment(QtCore.Qt.AlignBottom)
        self.kullanici_parola = QtWidgets.QLabel("Parola")
        self.kullanici_parola.setAlignment(QtCore.Qt.AlignBottom)
        self.hata = QtWidgets.QLabel("")
        self.hata.setAlignment(QtCore.Qt.AlignCenter)
        #kullanıcı inputu
        self.Ad = QtWidgets.QLineEdit()
        self.Ad.setPlaceholderText("Küçük harf kullanın")
        self.Ad.setMinimumHeight(30)
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.parola.setPlaceholderText("Yalnızca rakam")
        self.parola.setMinimumHeight(30)
        #butonlar
        self.new_user = QtWidgets.QPushButton("Hesap Oluştur")
        self.new_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.new_user.setStyleSheet("*{color: #008CBA;font-weight:200;border:None;}"
                                    "*:hover{background-color:#f5fcff;}")
        self.new_user.setMinimumHeight(30)
        self.login1 = QtWidgets.QPushButton("Giriş Yap")
        self.login1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login1.setStyleSheet("*{color: black;border: 2px solid #008CBA;}"+
                                  "*:hover {background-color: #008CBA;color: white;}")
        self.login1.setMinimumHeight(30)
        #butonlara işlev veriliyor
        self.new_user.clicked.connect(self.message_box)
        self.login1.clicked.connect(self.yeni_pencere)
        #widgetların katmanlara yerleştirilmesi
        self.helper2_layout.addWidget(self.new_user)
        self.helper2_layout.addWidget(self.login1)
        #Spacerlar
        self.verticalspacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalspcer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.helper1_layout.addItem(self.verticalspacer)
        self.helper1_layout.addWidget(self.kullanici_adi)
        self.helper1_layout.addWidget(self.Ad)
        self.helper1_layout.addWidget(self.kullanici_parola)
        self.helper1_layout.addWidget(self.parola)
        self.helper1_layout.addWidget(self.hata)
        self.helper1_layout.addLayout(self.helper2_layout)
        self.helper1_layout.addItem(self.verticalspacer)

        self.main_layout.addItem(self.horizontalspcer)
        self.main_layout.addLayout(self.helper1_layout)
        self.main_layout.addItem(self.horizontalspcer)
        #iki buton arasına biraz boşluk ekleyelim
        self.helper2_layout.setSpacing(50)
        #katmanların genişleme katsayıları
        self.helper1_layout.setStretch(0, 1)
        self.helper1_layout.setStretch(1, 1)
        self.helper1_layout.setStretch(2, 1)
        self.helper1_layout.setStretch(3, 1)
        self.helper1_layout.setStretch(4, 1)
        self.helper1_layout.setStretch(5, 1)
        self.helper1_layout.setStretch(6, 1)
        self.helper1_layout.setStretch(7, 1)

        self.main_layout.setStretch(0,1)
        self.main_layout.setStretch(1,2)
        self.main_layout.setStretch(2,1)
        #ana katamnı belirleme işlemi
        self.setLayout(self.main_layout)
        #pencereyi açma işlemi
        self.work(1)
        #sonraki pencereye geçmek için kullanılan bir kontrol mekanizması
    def work(self,check):
        self.check = check
        if self.check == 1:
            self.show()
        else:
            self.close()
    def yeni_pencere(self):
        #kullanıcı adı doğruysa giriş yapılabilir
        if self.Ad.text() == "paü" and self.parola.text()=="1234":
            self.pencere2 = Get_data()
            self.work(0)
        else:
            self.hata.setText("Kullanici adi veya parola yanlış!")
            self.hata.setStyleSheet("color: red")
    def message_box(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText('Üzerinde Çalışıyoruz:)')
        msg.setWindowTitle("Error")
        msg.exec_()
#ikinci sayfa yükseklik girdisi alınıyor
class Get_data(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        #pencere boyutları tahmini ekran büyüklüğüne göre uygulanmıştır,pencere adı eklenmiş ve show komutuyla pencere açılmıştır
        self.setGeometry(200,200,650,300)
        self.setWindowTitle("3'lü Su Tankının Raspberry Pi Tabanlı Kontrolü")
        #arayüzde bulunan katmanlar
        self.main_layout2 = QtWidgets.QHBoxLayout(self)
        self.helper1_layout = QtWidgets.QVBoxLayout()
        self.helper2_layout = QtWidgets.QHBoxLayout()
        self.helper3_layout = QtWidgets.QHBoxLayout()
        #wigetların belirlenmesi ve özellikleri
        #kullanıcı için açıklamalar
        self.kullanici_L1 = QtWidgets.QLabel("L1")
        self.kullanici_L3 = QtWidgets.QLabel("L3")
        self.hata_message = QtWidgets.QLabel("")
        self.hata_message.setAlignment(QtCore.Qt.AlignCenter)
        #kullanıcı inputs, yalnızca rakam girişine izin verilecek
        validator =  QtGui.QRegExpValidator(QRegExp(r'[0-9]+'))
        self.L1_in = QtWidgets.QLineEdit()
        self.L1_in.setMinimumHeight(30)
        self.L1_in.setValidator(validator)
        self.L1_in.setMaxLength(3)
        self.L1_in.setPlaceholderText("Yalnızca rakam")
        self.L3_in = QtWidgets.QLineEdit()
        self.L3_in.setMinimumHeight(30)
        self.L3_in.setValidator(validator)
        self.L3_in.setMaxLength(3)
        self.L3_in.setPlaceholderText("Yalnızca rakam")
        


        #başla butonu
        self.basla = QtWidgets.QPushButton("Başla")
        self.basla.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.basla.setStyleSheet("*{color: #008CBA;font-weight:200;border:None;}"
                                    "*:hover{background-color:#f5fcff;}")
        self.basla.setMinimumHeight(45)
        self.basla.clicked.connect(self.click)
        #spacerlar
        self.verticalspacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalspcer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                
        #katmanlar
        self.helper2_layout.addWidget(self.kullanici_L1)
        self.helper2_layout.addWidget(self.L1_in)

        self.helper3_layout.addWidget(self.kullanici_L3)
        self.helper3_layout.addWidget(self.L3_in)
        
        self.helper1_layout.addItem(self.verticalspacer)
        self.helper1_layout.addLayout(self.helper2_layout)
        self.helper1_layout.addLayout(self.helper3_layout)
        self.helper1_layout.addWidget(self.hata_message)
        self.helper1_layout.addWidget(self.basla)
        self.helper1_layout.addItem(self.verticalspacer)

        self.helper1_layout.setStretch(0,1)
        self.helper1_layout.setStretch(1,2)
        self.helper1_layout.setStretch(2,2)
        self.helper1_layout.setStretch(3,2)
        self.helper1_layout.setStretch(4,2)
        self.helper1_layout.setStretch(5,2)

        self.main_layout2.addItem(self.horizontalspcer)
        self.main_layout2.addLayout(self.helper1_layout)
        self.main_layout2.addItem(self.horizontalspcer)

        #ana katamnı belirleme işlemi
        self.setLayout(self.main_layout2)
        #pencereyi açma işlemi
        self.work(1)
    def work(self,check):
        self.check = check
        if self.check == 1:
            self.show()
        else:
            self.close()
    def click(self):
        if self.L1_in.text() == "" and self.L3_in.text() == "":
            self.hata_message.setText("Bir değer giriniz")
            self.hata_message.setStyleSheet("color: red")
        else:
            pencere.L1 = self.L1_in.text()
            pencere.L3 = self.L3_in.text()
            self.pencere3 = Results()
            self.work(0)
# üçüncü sayfa çalışma durumu, tank sıvı yüksekliği, motorlara uygulanan güç izleniyor
class Results(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        #pencere boyutları tahmini ekran büyüklüğüne göre uygulanmıştır,pencere adı eklenmiş ve show komutuyla pencere açılmıştır
        self.setGeometry(200,200,650,300)
        self.setWindowTitle("3'lü Su Tankının Raspberry Pi Tabanlı Kontrolü")
        #arayüzde bulunan katmanlar
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.helper1_layout = QtWidgets.QHBoxLayout()
        self.tanksv1_layout = QtWidgets.QVBoxLayout()
        self.tanksh1_layout = QtWidgets.QHBoxLayout()
        self.labelh1_layout = QtWidgets.QHBoxLayout()
        self.motors_layout = QtWidgets.QVBoxLayout()
        #kullanıcı için yönlendirmeler
        self.water_level = QtWidgets.QLabel("Sıvı Seviyesi")
        self.water_level.setAlignment(QtCore.Qt.AlignCenter)
        self.L1_l = QtWidgets.QLabel("L1")
        self.L1_l.setAlignment(QtCore.Qt.AlignCenter)
        self.L2_l = QtWidgets.QLabel("L2")
        self.L2_l.setAlignment(QtCore.Qt.AlignCenter)
        self.L3_l = QtWidgets.QLabel("L3")
        self.L3_l.setAlignment(QtCore.Qt.AlignCenter)
        self.motor_power = QtWidgets.QLabel("Motor Güçleri")
        self.motor_power.setAlignment(QtCore.Qt.AlignCenter)
        self.m1 = QtWidgets.QLabel("M1 motoru:")
        self.m2 = QtWidgets.QLabel("M2 motoru:")

        #progress bars
        self.L1_tank = QtWidgets.QProgressBar()
        self.L1_tank.setOrientation(QtCore.Qt.Vertical)
        self.L1_tank.setMinimumWidth(40)
        self.L2_tank = QtWidgets.QProgressBar()
        self.L2_tank.setOrientation(QtCore.Qt.Vertical)
        self.L2_tank.setMinimumWidth(40)
        self.L3_tank = QtWidgets.QProgressBar()
        self.L3_tank.setOrientation(QtCore.Qt.Vertical)
        self.L3_tank.setMinimumWidth(40)
        
        self.m1_bar =QtWidgets.QProgressBar()
        self.m1_bar.setMinimumHeight(30)
        self.m2_bar =QtWidgets.QProgressBar()
        self.m2_bar.setMinimumHeight(30)

        #stop butonu
        self.stop = QtWidgets.QPushButton("Dur")
        self.stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop.setMinimumHeight(45)
        self.stop.setStyleSheet("*{color: black;border: 2px solid #008CBA;}"+
                                  "*:hover {background-color: #008CBA;color: white;}")
        #katmanlara widgetların yerleştirilmesi
        self.tanksh1_layout.addWidget(self.L1_tank)
        self.tanksh1_layout.addWidget(self.L2_tank)
        self.tanksh1_layout.addWidget(self.L3_tank)

        self.labelh1_layout.addWidget(self.L1_l)
        self.labelh1_layout.addWidget(self.L2_l)
        self.labelh1_layout.addWidget(self.L3_l)

        self.tanksv1_layout.addWidget(self.water_level)
        self.tanksv1_layout.addLayout(self.tanksh1_layout)
        self.tanksv1_layout.addLayout(self.labelh1_layout)

        #motorlar layout
        self.motors_layout.addWidget(self.motor_power)
        self.motors_layout.addWidget(self.m1)
        self.motors_layout.addWidget(self.m1_bar)
        self.motors_layout.addWidget(self.m2)
        self.motors_layout.addWidget(self.m2_bar)

        self.helper1_layout.addLayout(self.tanksv1_layout)
        self.helper1_layout.addLayout(self.motors_layout)
        #Spacerlar
        self.verticalspacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.main_layout.addLayout(self.helper1_layout)
        self.main_layout.addWidget(self.stop)
        self.main_layout.addItem(self.verticalspacer)

        print(int(pencere.L1)+int(pencere.L3))

        self.setLayout(self.main_layout)
        self.work(1)
    def work(self,check):
        self.check = check
        if self.check == 1:
            self.show()
        else:
            self.close()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(Style)
    pencere = Login()
    app.exec()