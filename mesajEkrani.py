# -*- coding: cp1254 -*-
from varbs import *

from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen





class mesajEkrani(Screen):

    def __init__(self,app,smager):
        super(mesajEkrani,self).__init__()
        self.background_color = color_white
        self.APP = app
        self.SMAGER = smager
        

        #ÜST ÇUBUK AYARLARI
        self.ustCubuk = BoxLayout(orientation = "horizontal",size_hint_y = .1)
        self.backBtn = Button(background_normal = u"srcs/backico.png",background_down = u"srcs/backico_ot.png",size_hint_x = .22)       


        self.backBtn.bind(on_press=self.geriGit)

        self.ustCubuk.add_widget(self.backBtn)
        self.ustCubuk.add_widget(Label(color = black,size_hint_x = .80,font_name = def_font,font_size = fontSize,text = u"Mesajlaşma Odası"))
        self.ustCubuk.add_widget(Label(color = black,size_hint_x = .22))



        #EKRAN DÜZENİ AYARLAMASI
        self.duzen = BoxLayout(orientation="vertical",background_color = color_white)
        self.mesajPlfrm = BoxLayout(background_color = color_white,size_hint_y = .1,orientation = "horizontal")

        #ANA WİDGET AYARLAMALARI
        self.mesajAl = TextInput(cursor_color = invisible,readonly = True,color = color_white,size_hint_y = .8,background_color = color_white)
        self.mesajKutu = TextInput(cursor_width = 3,cursor_color=primary_color,size_hint_x =.8,background_color = color_white,multiline = False,autofocus=False)
        self.gonderBtn = Button(background_color = color_white,background_normal = u"srcs/sendico.png",background_down = u"srcs/sendico_ot.png",size_hint_x = .2)

        self.gonderBtn.bind(on_press =self.gonderBtnFonk)
        self.mesajKutu.bind(on_text_validate = self.gonderBtnFonk)
        


        #WİDGETLARA EKLENİYOR
        self.mesajPlfrm.add_widget(self.mesajKutu)
        self.mesajPlfrm.add_widget(self.gonderBtn)

        self.duzen.add_widget(self.ustCubuk)
        self.duzen.add_widget(self.mesajAl)
        self.duzen.add_widget(self.mesajPlfrm)

        self.add_widget(self.duzen)


    def geriGit(self,touch):
        self.SMAGER.transition = down
        self.parent.current = self.SMAGER.previous()
        self.SMAGER.transition = up
        self.mesajAl.text = ""
        self.mesajKutu.text = ""
        self.yenisocket()

    def kapat1(self,touch):
        self.APP.stop()
        self.yenisocket()




 



        
