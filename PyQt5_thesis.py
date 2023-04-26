import sys 
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtCore import * 



#butonların görünüşlerini belirliyoruz
Style = """
    QWidget{
        font: 12pt "MV Boli";
        color: rgba(255, 255, 255, 230);
    }

    QLineEdit{

        background-color:rgba(0,0,0,0);
        border:none;
        border-bottom:2px solid rgba(105,118,132,255);
        padding-bottom:7px;
    }
    QPushButton{
        background-color:rgba(0,0,0,0);
        border:none;
        border-bottom:2px solid rgba(105,118,132,255);
        border-top:2px solid rgba(105,118,132,255);
        border-radius: 10px;
        padding-bottom:7px;

    }

    QPushButton:pressed{
        padding-left:5px;
        padding-top:5px;
        background-color:rgba(100,200,255,255);

    }
    QProgressBar{
        border: 2px solid grey;
        color: black ;
        border-radius: 5px;
        text-align: center;
}
    QProgressBar::chunk {
        background-color: rgb(100, 200, 255);
        width: 10px;
        margin: 0.5px;
}
"""
#giriş penceresi
class Kullanici_girisi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        #Arka plan resmi
        self.background = QtWidgets.QLabel(self)
        self.background.setGeometry(0,0,500,300)
        self.background.setStyleSheet("border-image: url(back.png);")
        #pencere boyutu
        self.setGeometry(200,200,500,300)
        #kullanıcı arayüzü giriş kısımı, özellikleri
        self.kullanici_adi = QtWidgets.QLineEdit(self)
        self.kullanici_adi.move(200,55)
        self.parola = QtWidgets.QLineEdit(self)
        self.parola.move(200,135)
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton(self)
        self.giris.setText("Giriş Yap")
        self.giris.setGeometry(225,200,90,55)

        self.hata = QtWidgets.QLabel(self)
        self.hata.setGeometry(150,165,300,50)
        self.kullanici = QtWidgets.QLabel(self)
        self.kullanici.setText("Kullanıcı Adı")
        self.kullanici.move(200,25)
        self.kullanici_paralo = QtWidgets.QLabel(self)
        self.kullanici_paralo.setText("Parola")
        self.kullanici_paralo.move(200,105)

        #Kullanıcı grişi kontrolü, yeni pencere açma işlemleri
        self.giris.clicked.connect(self.yeni_pencere)
       
        self.setWindowTitle("3'lü Su Tankının Raspberry Pi Tabanlı Kontrolü")
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
        if self.kullanici_adi.text() == "paü" and self.parola.text()=="1234":
            self.hata.setText("Hoşgeldiniz")
            self.hata.setStyleSheet("color: green")
            self.pencere2 = Ana_menu()
            self.work(0)
        else:
            self.hata.setText("Kullanici adi veya parola yanlış!")
            self.hata.setStyleSheet("color: red")
#ikinci sayfa yükseklik girdisi alınıyor
class Ana_menu(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        #Arka plan resmi
        self.background = QtWidgets.QLabel(self)
        self.background.setGeometry(0,0,500,300)
        self.background.setStyleSheet("border-image: url(back.png);")
        #pencere boyutu
        self.setGeometry(200,200,500,300)

        #arayüz butonlar, yazılar, özellikler
        self.L1 = QtWidgets.QLabel(self)
        self.L1.setText("L1 tankı için sıvı yüksekliği:")
        self.L1.move(170,25)
        self.L2 = QtWidgets.QLabel(self)
        self.L2.setText("L2 tankı için sıvı yüksekliği:")
        self.L2.move(170,105)
        self.hata_mesji = QtWidgets.QLabel(self)
        self.hata_mesji.setGeometry(150,165,300,50)
        self.L1_deger = QtWidgets.QLineEdit(self)
        self.L1_deger.setGeometry(170,55,200,30)
        self.L2_deger = QtWidgets.QLineEdit(self)
        self.L2_deger.setGeometry(170,135,200,30)
        self.basla = QtWidgets.QPushButton(self)
        self.basla.setText("Başla")
        self.basla.setGeometry(225,200,90,55)


        #başla butonu fonksiyonu
        self.basla.clicked.connect(self.click)

        self.setWindowTitle("3'lü Su Tankının Raspberry Pi Tabanlı Kontrolü")
        #pencere geçişi için kontrol mekanizması
        self.work(1)
    def work(self,check):
        self.check = check
        if self.check == 1:
            self.show()
        else:
            self.close()
    def click(self):
        if self.L1_deger.text() == "" and self.L2_deger.text() == "":
            self.hata_mesji.setText("Bir değer giriniz")
            self.hata_mesji.setStyleSheet("color: red")
        else:
            self.pencere3 = Calis()
            self.work(0)
# üçüncü sayfa çalışma durumu, tank sıvı yüksekliği, motorlara uygulanan güç izleniyor
class Calis(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        #Arka plan fotoğrafı
        self.background = QtWidgets.QLabel(self)
        self.background.setStyleSheet("border-image: url(back.png);")
        self.background.setGeometry(0,0,500,300)
        self.setGeometry(200,200,500,300)

        #Sıvı seviyesi yazısı ve özellikleri
        self.sivi = QtWidgets.QLabel(self)
        self.sivi.setText("Sıvı Seviyesi")
        self.sivi.move(85,10)

        #Su tankları - progres barları ve özellikleri
        self.L1_tank = QtWidgets.QProgressBar(self)
        self.L1_tank.setOrientation(QtCore.Qt.Vertical)
        self.L1_tank.setGeometry(50,50,40,120)  
        self.L2_tank = QtWidgets.QProgressBar(self)
        self.L2_tank.setOrientation(QtCore.Qt.Vertical)
        self.L2_tank.setGeometry(110,50,40,120)
        self.L3_tank = QtWidgets.QProgressBar(self)
        self.L3_tank.setOrientation(QtCore.Qt.Vertical)
        self.L3_tank.setGeometry(170,50,40,120)

        #L1, L2, L3 yazısı ve özelikkleri
        self.L1 = QtWidgets.QLabel(self)
        self.L1.setText("L1")
        self.L1.move(60,175)
        self.L2 = QtWidgets.QLabel(self)
        self.L2.setText("L2")
        self.L2.move(120,175)
        self.L3 = QtWidgets.QLabel(self)
        self.L3.setText("L3")
        self.L3.move(180,175)


        #Motor görsetrgeleri ve özellkleri
        self.motor_l = QtWidgets.QLabel(self)
        self.motor_l.setText("Motor Güçleri")
        self.motor_l.move(270,10)
        self.motor_m1 = QtWidgets.QLabel(self)
        self.motor_m1.setText("M1 Motoru")
        self.motor_m1.move(270,50)
        self.motor_m2 = QtWidgets.QLabel(self)
        self.motor_m2.setText("M2 Motoru")
        self.motor_m2.move(270,120)
        self.motor_bar1 = QtWidgets.QProgressBar(self)
        self.motor_bar1.setOrientation(QtCore.Qt.Horizontal)
        self.motor_bar1.setGeometry(270,80,175,20)
        self.motor_bar2 = QtWidgets.QProgressBar(self)
        self.motor_bar2.setGeometry(270,150,175,20)

        #durdurma butonu
        self.stop = QtWidgets.QPushButton(self)
        self.stop.setText("Dur")
        self.stop.setGeometry(200,200,90,55)

        self.setWindowTitle("3'lü Su Tankının Raspberry Pi Tabanlı Kontrolü")
        self.work(1)
    def work(self,check):
        self.check = check
        if self.check == 1:
            self.show()
        else:
            self.close()
        

app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(Style)
pencere = Kullanici_girisi()
app.exec()
