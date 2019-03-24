# -*- coding: cp1254 -*-
from varbs import *

import ipAdresiAL,threading

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from popups import Loader
from kivy.uix.image import Image

import socket,cipher,client,threading
import random



class katilSayfa(Screen):

    def __init__(self, app, smager,sock,kul_EKRAN):
        super(katilSayfa,self).__init__()
        self.name = "katilSayfa"
        self.background_color = color_white
        self.APP = app
        self.SMAGER = smager
        self.accs = "mber"
        self.acikKEY = None
        self.kapaliKEY = None
        self.sock = sock
        self.kul_EKRAN = kul_EKRAN

        #��FRELEME ANAHTARLARI KURULUYOR
        

        #POP-UP PENCERES� D�ZENLER�
        self.loader = Loader()

        #HEPS�N� TOPLAYACAK D�ZEN
        self.tumDuzen=BoxLayout(orientation = "vertical")

        #�STTE DURACAK OLAN �UBUK
        self.ustCubuk = BoxLayout(orientation = "horizontal",size_hint_y = .1)
        self.backBtn = Button(background_normal = u"srcs/backico.png",background_down = "srcs/backico_ot.png",size_hint_x = .22)  

        self.backBtn.bind(on_press=self.geriGit)

        self.ustCubuk.add_widget(self.backBtn)
        self.ustCubuk.add_widget(Label(color = black,size_hint_x = .80,font_name = def_font,font_size = fontSize,text = "Sunucu Bilgileri"))
        self.ustCubuk.add_widget(Label(color = black,size_hint_x = .22))

        #ANA D�ZEN TANIMI
        self.anaDuzen = BoxLayout(orientation = "horizontal",size_hint_y = .9)

        #B�Y�K BO� W�DGETLAR
        self.solBosWid0 = Label(size_hint_x = .2)
        self.sagBosWid1 = Label(size_hint_x = .2)
        self.bosWid0 = Label(size_hint_y = .2)
        self.bosWid1 = Label(size_hint_y = .1)

        #ORTA D�ZEN ELEMANLARI VE ORTA D�ZEN TANIMI
        self.ortaDuzen = BoxLayout(size_hint_x = .6, orientation = "vertical")

        self.mtnKtu0 = Label(text = u"IP adresini giriniz: ",size_hint_y = .1,font_size = fontSize,font_name = def_font,color = black)
        self.mtnKtu1 = Label(text = u"PORT numaras�n� giriniz: ",font_size = fontSize,size_hint_y = .1,font_name = def_font,color = black)
        self.mtnKtu2 = Label(text = u"�ifreyi giriniz: ",font_size = fontSize,size_hint_y = .1,font_name = def_font,color = black)

        self.ipAl = TextInput(hint_text = "xxx.xxx.xxx.xxx",hint_text_color = (0,0,0,.5),font_name = def_font,size_hint_y = .1,font_size = fontSize)
        self.portAl = TextInput(input_filter = "int",font_name = def_font,size_hint_y = .1,font_size = fontSize)
        self.sifreAl = TextInput(font_name = def_font,size_hint_y = .1,font_size = fontSize)

        self.tmBtn = Button(text = u"Ba�lan",background_color = primary_color,color = color_white,font_name = def_font,size_hint_y = .1,font_size = fontSize)
        self.tmBtn.bind(on_press = self.baglan)

        #W�DGETLARIN ORTA D�ZENE VE EKRANA EKLENMES�
        self.ortaDuzen.add_widget(self.bosWid0)
        self.ortaDuzen.add_widget(self.mtnKtu0)
        self.ortaDuzen.add_widget(self.ipAl)
        self.ortaDuzen.add_widget(self.mtnKtu1)
        self.ortaDuzen.add_widget(self.portAl)
        self.ortaDuzen.add_widget(self.mtnKtu2)
        self.ortaDuzen.add_widget(self.sifreAl)
        self.ortaDuzen.add_widget(self.tmBtn)
        self.ortaDuzen.add_widget(self.bosWid1)

        self.anaDuzen.add_widget(self.solBosWid0)
        self.anaDuzen.add_widget(self.ortaDuzen)
        self.anaDuzen.add_widget(self.sagBosWid1)

        self.tumDuzen.add_widget(self.ustCubuk)
        self.tumDuzen.add_widget(self.anaDuzen)
        
        self.add_widget(self.tumDuzen)

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

    def sifrekur(self):
        keys = self.keySEC()
        self.acikKEY = cipher.keyTRANS(keys[0])
        self.kapaliKEY = cipher.keyTRANS(keys[1])

        self.kul_EKRAN.kapaliKEY = self.kapaliKEY
        

    def geriGit(self,touch):
        try:
            self.sock.close()
        except:
            pass
        finally:
            self.SMAGER.transition = down
            self.parent.current = "ilkSayfa"
            self.SMAGER.transition = up

    def baglan(self,touch):
        self.IP = self.ipAl.text
        self.PORT = int(self.portAl.text)
        self.SIFRE = self.sifreAl.text

        self.kul_EKRAN.mesajAl.text = ""
        self.kul_EKRAN.mesajKutu.text = ""
        
        self.loader.text.text = u"�ifreleme Anahtar�\nOlu�turuluyor..."
        self.loader.open()
        
        self.baglanma = threading.Thread(target = self.thrBaglan)
        self.baglanma.daemon = True
        self.baglanma.run()

    def thrBaglan(self):
        try:
            
            self.sifrekur()
            self.loader.text.text = u"Ba�lan�l�yor..."
            client.main(self.sock,self.IP,self.PORT,self.SIFRE,self.acikKEY,self.accs,self.loader,self,self.SMAGER,self.kul_EKRAN)
            
        except Exception as e:
            print "HATA\t"+ str(e)
            self.loader.dismiss()
        finally:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        



        

        
