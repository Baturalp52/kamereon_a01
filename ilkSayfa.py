# -*- coding: cp1254 -*-
from varbs import *

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import  Screen
from kivy.core.window import Window






class ilkSayfa(Screen):
    def __init__(self,app,smager):
        super(ilkSayfa,self).__init__()
        self.name = "ilkSayfa"
        self.background_color = color_white
        self.APP = app
        self.SMAGER = smager


        #HEPSİNİ TOPLAYACAK DÜZEN
        self.tumDuzen=BoxLayout(orientation = "vertical")
        
        #ÜSTTE DURACAK OLAN ÇUBUK
        self.ustCubuk = BoxLayout(orientation = "horizontal",size_hint_y = .1)        
        
        self.ustCubuk.add_widget(Label(color = black,size_hint_x = .99,font_name = u"srcs/MullerNarrow",font_size = fontSize,text = "Kamereon"))


        #ALT DÜZEN
        self.duzen = BoxLayout(orientation = "horizontal",size_hint_y = .9)

        #BUTON AYARLAMALARI
        self.btn_duzen = BoxLayout(size_hint_x=.50,orientation="vertical")
        
        self.btn1 = Button(text = "Oda Kur",font_size = fontSize, background_color = primary_color, size_hint_y =.15, bold = False, font_name = u"srcs/MullerNarrow")
        self.btn1.bind(on_press =self.oda_kurGecis)

        self.btn2 = Button(text=u"Odaya Katıl",font_size = fontSize, background_color = primary_color,size_hint_y = .15, bold = False, font_name = u"srcs/MullerNarrow")
        self.btn2.bind(on_press = self.oda_baglanGecis)

        
        #BUTON DÜZENLERİ İÇİN BOŞ WİDGETLAR
        self.bt_bosWid = Image(source = u"srcs/kamereon_icon.png",size_hint_y=.25)
        self.bt_bosWid2 = Label(background_color=(0,0,0,0),size_hint_y=.10)
        self.bt_bosWid3 = Label(background_color=(0,0,0,0),size_hint_y=.25)

        #BUTON ALANINA EKLEMELER
        self.btn_duzen.add_widget(self.bt_bosWid)
        self.btn_duzen.add_widget(self.btn1)
        self.btn_duzen.add_widget(self.bt_bosWid2)
        self.btn_duzen.add_widget(self.btn2)
        self.btn_duzen.add_widget(self.bt_bosWid3)
        

        #BÜYÜK BOŞ WİDGETLAR HAZIRLANDI
        self.bosWid = Label(background_color=(0,0,0,0),size_hint_x=.25)
        self.bosWid2 = Label(background_color=(0,0,0,0),size_hint_x=.25)

        #SON DÜZENE EKLEMELER YAPILIYOR
        self.duzen.add_widget(self.bosWid)
        self.duzen.add_widget(self.btn_duzen)
        self.duzen.add_widget(self.bosWid2)
        

        #HEPSİ TÜMLEYEN DÜZENE EKLENİYOR
        self.tumDuzen.add_widget(self.ustCubuk)
        self.tumDuzen.add_widget(self.duzen)

        #HEPSİ EKRANDA
        self.add_widget(self.tumDuzen)
        


    def oda_kurGecis(self,touch):
        self.parent.current = "kurSayfa"
        

    def oda_baglanGecis(self,touch):
        self.parent.current = "katilSayfa"

