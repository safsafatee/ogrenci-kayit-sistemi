from ogrenci import *
import sys
import enum 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

#uygulama Gösterme işlemleri

uygulama=QApplication(sys.argv)
pencere=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()




#Database İşlemleri

baglanti=sqlite3.connect("kayit.db")
islem=baglanti.cursor()
baglanti.commit()
islem=baglanti.cursor()
Tablo="""Create Table if NOT Exists ogrenci (
Numara INTEGER PRIMARY KEY NOT NULL,
Ad TEXT NOT NULL,
Soyad TEXT NOT NULL,
Ders TEXT NOT NULL,
Vize INTEGER NOT NULL,
Final INTEGER NOT NULL,
Ortalama REAL NOT NULL,
Harf TEXT NOT NULL,
Durum TEXT NOT NULL


)"""
islem.execute(Tablo)
baglanti.commit()

ui.tableWidget_Liste.setHorizontalHeaderLabels(("Numara","Ad","Soyad","Ders","Vize","Final","Not","Harf","Durum"))
ui.tableWidget_Liste.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

def ekle():
    Numara=int(ui.lineEdit_Numara.text())
    Ad=ui.lineEdit_Ad.text()
    Soyad=ui.lineEdit_Soyad.text()
    Ders=ui.comboBox_Ders.currentText()
    Vize=int(ui.lineEdit_Vize.text())
    Final=int(ui.lineEdit_Final.text())
    Ortalama=int((Vize*0.4)+(Final*0.6))
    Harf=""
    Durum=""
    if Ortalama<50:
        Harf="FF"
    elif Ortalama>=50 and Ortalama<60:
        Harf="DD"
    elif Ortalama>=60 and Ortalama<70 :
        Harf="CC"
    elif Ortalama>=70 and Ortalama<=80:
        Harf="BB"
    elif Ortalama>80:
        Harf="AA"
    else:
        ui.statusbar.showMessage("HAYIR",5000)
        return
    if Ortalama>=50 :
        Durum="GEÇTİ"
    else:
        Durum="KALDI"

    sorgu=f"INSERT INTO Ogrenci (Numara,Ad,Soyad,Ders,Vize,Final,Ortalama,Harf,Durum) VALUES ({Numara},'{Ad}','{Soyad}','{Ders}',{Vize},{Final},{Ortalama},'{Harf}','{Durum}')"
    print(sorgu)
    try:
        #islem.execute(sorgu,(Numara,Ad,Soyad,Ders,Vize,Final,Ortalama,Harf,Durum))
        islem.execute(sorgu)
        print(islem.description)
        baglanti.commit()
        ui.statusbar.showMessage("Kayıt Başarılı",4000)
        listele()
        temizle()
    except:
        ui.statusbar.showMessage("Hata Oluştu",4000)

def sil():
    silme_onay=QMessageBox.question(pencere,"ONAY","Silmek istediğinize emin misiniz?",QMessageBox.Yes|QMessageBox.No)
    if silme_onay==QMessageBox.StandardButton.Yes:
        sorgu="delete from ogrenci where Numara= ?"
        secien_kayit=ui.tableWidget_Liste.selectedItems()
        silinecek_kayit=secien_kayit[0].text()
        try:
            islem.execute(sorgu,(silinecek_kayit,))
            baglanti.commit()
            listele()
            ui.statusbar.showMessage("SİLME BAŞARILI",4000)
        except:
            ui.statusbar.showMessage("SİLME HATASI OLUŞTU",4000)
    else:
        ui.statusbar.showMessage("SİLME İŞLEMİ İPTAL EDİLDİ",4000)
        




def filitrele():
    ui.tableWidget_Liste.clear()
   
    ui.tableWidget_Liste.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.tableWidget_Liste.horizontalHeader().setStyle("color:Red;font-size:16px;fonr-weight:bold")
    ui.tableWidget_Liste.setHorizontalHeaderLabels("Numara","Ad","Soyad","Ders","Vize","Final","Not","Harf","Durum")
    filitre=ui.comboBox_Filitre.currentText()
    sorgu="select * from ogrenci where Ders= ?"
    try:
        islem.execute(sorgu,(filitre,))
        for indexsatir,kayitnumarasi in enumerate(islem):
            for indexsutun,kayıtsutun in enumerate(kayitnumarasi):
                ui.tableWidget_Liste.setItem(indexsatir,indexsutun,QTableWidgetItem(str(kayıtsutun)))
    except:
        ui.statusbar.showMessage("LİSTELENEMESİ",4000)

def listele():
    
    ui.tableWidget_Liste.clear()
    ui.tableWidget_Liste.horizontalHeader().setStyleSheet("color:Red;font-size:16px;font-weight:bold")
    ui.tableWidget_Liste.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.tableWidget_Liste.setHorizontalHeaderLabels(("Numara","Ad","Soyad","Ders","Vize","Final","Not","Harf","Durum"))

    sorgu="SELECT * FROM ogrenci"
    islem.execute(sorgu)
    #ogrenciler=islem.fetchall()
    for indexsatir,kayitnumarasi in enumerate(islem):
        for indexsutun,kayıtsutun in enumerate(kayitnumarasi):
            ui.tableWidget_Liste.setItem(indexsatir,indexsutun,QTableWidgetItem(str(kayıtsutun)))

def temizle():
    ui.lineEdit_Ad.clear()
    ui.lineEdit_Soyad.clear()
    ui.lineEdit_Numara.clear()
    ui.lineEdit_Vize.clear()
    ui.lineEdit_Final.clear()
    ui.comboBox_Ders.setCurrentIndex(-1)
    ui.comboBox_Filitre.setCurrentIndex(-1)

        













"""

                kayitlar=veri.fetchone()
                print(kayitlar[0])
                finalnotu=kayitlar["Final"]
                print(finalnotu)

"""





def tumkayitlar():
    listele()

def guncelle():
    
 
 
    Ad=ui.lineEdit_Ad.text()
    Soyad=ui.lineEdit_Soyad.text()
    Ders=ui.comboBox_Ders.currentText()
    Vize=ui.lineEdit_Vize.text()
    Final=ui.lineEdit_Final.text()
    numara_kontrol=ui.lineEdit_Numara.text()
    """

    
    Ortalama=int((Vize*0.4)+(Final*0.6))
    Harf=""
    Durum=""
    if Ortalama<50:
        Harf="FF"
    elif Ortalama>=50 and Ortalama<60:
        Harf="DD"
    elif Ortalama>=60 and Ortalama<70 :
        Harf="CC"
    elif Ortalama>=70 and Ortalama<=80:
        Harf="BB"
    elif Ortalama>80:
        Harf="AA"
    else:
        ui.statusbar.showMessage("HAYIR",5000)
        return
    if Ortalama>=50 :
        Durum="GEÇTİ"
    else:
        Durum="KALDI"
     """   
    guncelleme_onay=QMessageBox.question(pencere,"GÜNCELLEME","Kaydı güncellemek istediğinizden emin misiniz?",QMessageBox.Yes|QMessageBox.No)    
    if guncelleme_onay==QMessageBox.StandardButton.Yes:
        print(Numara)
        try:
            if Soyad=="" and Ders=="" and Vize=="" and Final=="":
                Numara=int(ui.lineEdit_Numara.text())
                sorgu="Update ogrenci Ad= ? where Numara=?"
                islem.execute(sorgu,(Ad,Numara))
            elif Ad=="" and Ders=="" and Vize=="" and Final=="":
                Numara=int(ui.lineEdit_Numara.text())
                sorgu="update ogrenci set Soyad= ?  where Numara=?"
                islem.execute(sorgu,(Soyad,Numara))
            elif Ad=="" and Soyad=="" and Vize=="" and Final=="":
                sorgu="update ogrenci set Ders= ?  where Numara=?"
                islem.execute(sorgu,(Ders,Numara)) 
            elif Ad=="" and Soyad=="" and Ders=="" and Final=="":
                print("Vize")
                vize_al=int(ui.lineEdit_Vize.text())
                final_sorgu="select Final from ogrenci where Numara= ?"
                print(final_sorgu)
                veri=islem.execute(final_sorgu,(Numara,))
        
                sorgu="update ogrenci set Vize= ?  where Numara=?"
                islem.execute(sorgu,(Ders,vize_al)) 
            elif Ad=="" and Soyad=="" and Ders=="" and Vize=="":
                final_al=int(ui.lineEdit_Final.text())
                sorgu="update ogrenci set Final= ?  where Numara=?"
                islem.execute(sorgu,(Ders,vize_al)) 
            elif Ad!="" and Soyad!="" and Ders!="" and Vize!="" and Final!="":
                final_al=int(ui.lineEdit_Final.text())
                vize_al=int(ui.lineEdit_Vize.text())
                Ortalama=int((vize_al*0.4)+(final_al*0.6))
                Harf=""
                Durum=""
                if Ortalama<50:
                    Harf="FF"
                elif Ortalama>=50 and Ortalama<60:
                    Harf="DD"
                elif Ortalama>=60 and Ortalama<70 :
                    Harf="CC"
                elif Ortalama>=70 and Ortalama<=80:
                    Harf="BB"
                elif Ortalama>80:
                    Harf="AA"
                else:
                    ui.statusbar.showMessage("HAYIR",5000)
                    return
                if Ortalama>=50 :
                    Durum="GEÇTİ"
                else:
                    Durum="KALDI"
                sorgu="update ogrenci set Final= ?  where Numara=?"
                islem.execute(sorgu,(Ders,vize_al))                          
            baglanti.commit()
            listele()
        except:
            pass






ui.pushButton_Ekle.clicked.connect(ekle)
ui.pushButton_Sil.clicked.connect(sil)
ui.pushButton_Filitrele.clicked.connect(filitrele)
ui.pushButton_tumKayitlar.clicked.connect(tumkayitlar)
ui.pushButton_Ekle_Guncelle.clicked.connect(guncelle)
ui.pushButton_Ekle_Temizle.clicked.connect(temizle)
listele()

sys.exit(uygulama.exec_())







