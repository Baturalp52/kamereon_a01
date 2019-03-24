# -*- coding: cp1254 -*-
from varbs import *
import random,ipAdresiAL

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from popups import Loader,Error

import cipher,server,threading
import socket,random





class kurSayfa(Screen):

    def __init__(self,app,smager,sock):
        super(kurSayfa,self).__init__()
        self.name = "kurSayfa"
        self.background_color = color_white
        self.IP = self.ipbul()
        self.SIFRE = self.get_PASS()
        self.PORT = self.get_PORT()
        self.APP = app
        self.SMAGER = smager
        self.sock = sock
        self.sun_EKRAN = None

        #HEPSİNİ TOPLAYACAK DÜZEN
        self.tumDuzen=BoxLayout(orientation = "vertical")
        
        #ÜSTTE DURACAK OLAN ÇUBUK
        self.ustCubuk = BoxLayout(orientation = "horizontal",size_hint_y = .1)
        self.backBtn = Button(background_normal = u"srcs/backico.png",background_down = u"srcs/backico_ot.png",size_hint_x = .22)

        self.backBtn.bind(on_press=self.geriGit)

        self.ustCubuk.add_widget(self.backBtn)
        self.ustCubuk.add_widget(Label(color = black,size_hint_x = .80,font_name = def_font,font_size = fontSize,text = "Sunucu Bilgileri"))
        self.ustCubuk.add_widget(Label(color = black,size_hint_x = .22))

        #ALT DUZEN TANIMI
        self.duzen = BoxLayout(orientation = "vertical",size_hint_y = .9)

        #PORT VE IP BÖLÜMÜNÜN YENİ DÜZENİ        
        self.ust = BoxLayout(size_hint_y =.2,orientation = "horizontal")
        self.orta = BoxLayout(size_hint_y =.2,orientation = "horizontal")
        self.alt = BoxLayout(size_hint_y =.2,orientation = "horizontal")
        self.alt2 = BoxLayout(size_hint_y =.2,orientation = "horizontal")
        

        #BÜYÜK BOŞ WIDGETLAR
        self.bosWid0 = Label(background_color=(0,0,0,0),size_hint_y=.4)
        self.bosWid1 = Label(background_color=(0,0,0,0),size_hint_y=.4)

        #KÜÇÜK BOŞ WIDGETLAR
        self.bosWid2 = Label(background_color=(0,0,0,0),size_hint_x=.2)
        self.bosWid3 = Label(background_color=(0,0,0,0),size_hint_x=.2)
        self.bosWid4 = Label(background_color=(0,0,0,0),size_hint_x=.2)
        self.bosWid5 = Label(background_color=(0,0,0,0),size_hint_x=.2)
        self.bosWid6 = Label(background_color=(0,0,0,0),size_hint_x=.2)
        self.bosWid7 = Label(background_color=(0,0,0,0),size_hint_x=.2)
        self.bosWid8 = Label(background_color=(0,0,0,0),size_hint_x=.35)
        self.bosWid9 = Label(background_color=(0,0,0,0),size_hint_x=.35)

        #IP VE PORT WİDGETLARI
        self.ip = Label(text ="IP adresiniz: %s" % self.IP,font_size = fontSize,size_hint_x=.6,color = black,font_name = def_font)
        self.port = Label(text=u"PORT numaranız: %s"% self.PORT,font_size = fontSize,size_hint_x=.6,color = black,font_name = def_font)
        self.sifre = Label(text=u"Şifreniz: %s"% self.SIFRE,size_hint_x=.6,font_size = fontSize,color = black,font_name = def_font)
        self.tamamBtn = Button(text="Tamam",background_color = primary_color,color=color_white,font_size=fontSize,size_hint_x=.30,font_name = def_font)

        #BUTONA GÖREV İLİŞTİRİLİYOR
        self.tamamBtn.bind(on_press =self.oda_sunucuGecis)

        #KUTU ÜZERİNE YERLEŞTİRME
        self.ust.add_widget(self.bosWid2)
        self.ust.add_widget(self.ip)
        self.ust.add_widget(self.bosWid3)

        self.orta.add_widget(self.bosWid4)
        self.orta.add_widget(self.port)
        self.orta.add_widget(self.bosWid5)

        self.alt.add_widget(self.bosWid6)
        self.alt.add_widget(self.sifre)
        self.alt.add_widget(self.bosWid7)

        self.alt2.add_widget(self.bosWid8)
        self.alt2.add_widget(self.tamamBtn)
        self.alt2.add_widget(self.bosWid9)



        #DUZEN NESNESİNE YERLEŞTİRME
        
        self.duzen.add_widget(self.bosWid0)
        self.duzen.add_widget(self.ust)
        self.duzen.add_widget(self.orta)
        self.duzen.add_widget(self.alt)
        self.duzen.add_widget(self.alt2)
        self.duzen.add_widget(self.bosWid1)

        #HEPSİ TOPLAYICI DÜZENE EKLENİYOR
        self.tumDuzen.add_widget(self.ustCubuk)
        self.tumDuzen.add_widget(self.duzen)

        #HEPSİNİ EKRANA AKTARMA
        self.add_widget(self.tumDuzen)

        #SONRADAN KULLANILACAK OLANLAR
        self.loader = Loader()
        self.error = Error()
        self.sunucu = threading.Thread(target=self.kurmaISLEM)
        self.sunucu.daemon = True

    def ipbul(self):
        return ipAdresiAL.ipAL()

    def portsec(self):
        return str(random.randint(2002,20000))

    def paswOlustur(self):
        harf_sysi = random.randint(8,16)
        sifre = ""
        for i in range(harf_sysi):
            sifre += random.choice(sfrKar)

        return sifre

    
    def degsknGonder(self):
        return self.IP,self.PORT,self.SIFRE
    
    def oda_sunucuGecis(self,touch):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sunucu.start()

    def keySEC(self):
        file1 = open("keys","r")
        data = file1.read()
        file1.close()
        keys = random.choice(data.split("\n")[:-1])
        keys = keys.replace("(","")
        keys = keys.replace(")","")
        keys = keys.replace(" ","")
        keys = keys.split(",")
        return (keys[0],keys[1]),(keys[2],keys[3])
        


    def kurmaISLEM(self):
        self.loader.text.text = u"Şifreleme Anahtarı\nOluşturuluyor..."
        self.loader.open()
        self.sifreKEY = self.keySEC()
        self.acikKEY = cipher.keyTRANS(self.sifreKEY[0])
        self.sakliKEY = cipher.keyTRANS(self.sifreKEY[1])

        self.sun_EKRAN.kapaliKEY = self.sakliKEY
        
        
        


        try:
            self.loader.text.text = "Sunucu Kuruluyor..."
            self.sunucu =  threading.Thread(target=self.kurmaISLEM)
            self.sunucu.daemon = True
            server.main(self.sock,self.SIFRE, self.loader, self.parent,int(self.PORT),self.sun_EKRAN,self.acikKEY)


        except Exception as e:
            print e
            self.loader.dismiss()
            self.error.open()
            self.sunucu = threading.Thread(target=self.kurmaISLEM)
            self.sunucu.daemon = True



        
    def geriGit(self,touch):      
        try:
            self.sock.close()
        except:
            pass
        finally:
            self.SMAGER.transition = down
            self.parent.current = self.SMAGER.previous()
            self.SMAGER.transition = up


    def kapat(self,touch):
        try:
            self.sock.close()
        except:
            pass
        finally:
            self.APP.stop()

    def get_PASS(self):
        a = open(u"properties.ini","r")
        f = a.read()
        a.close()
        f = f.split("\n")
        f = f[1]
        pasw = f[6:]
        if pasw == "[%random%]":
            return self.paswOlustur()
        else:
            return pasw

    def get_PORT(self):
        a = open(u"properties.ini","r")
        f = a.read()
        a.close()
        f = f.split("\n")
        f = f[0]
        port = f[6:]
        if port == "[%random%]":
            return self.portsec()
        else:
            return port
        






