# -*- coding: cp1254 -*-
import sys
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'
reload(sys)
sys.setdefaultencoding('cp1254')

from varbs import *

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.config import Config



from ilkSayfa import ilkSayfa
from kurSayfa import kurSayfa
from sunucuSayfasi import sunucuSayfasi
from katilSayfa import katilSayfa
from kullaniciSayfasi import kullaniciSayfasi

import socket

Config.set("graphics","resizable",0)
Config.write()
Window.clearcolor = (1, 1, 1, 1)
Window.borderless = False
Window.top = 50
Window.left = 50
Window.size=(266.834645669,516.283464567)

class uygulamaOls(App):
    def on_stop(self):
        Window.close()

    def build(self):
     
        #PENCERE VE ANA EKRAN ?ZELL?KLER? TANIMLANIYOR
        self.title = "Kamereon Alpha 0.1"
        self.icon = u"srcs\\kamereon_icon.png"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Y?NET?C? TANIMLANIYOR
        eY = ScreenManager(transition = up)

        #SAYFALAR TANIMLANIYOR
        ilkSayfa0 = ilkSayfa(self,eY)
        
        kurSayfa0 = kurSayfa(self,eY,self.sock)
        sunucuSayfasi0 = sunucuSayfasi(self,kurSayfa0,eY,self.sock)
        kurSayfa0.sun_EKRAN = sunucuSayfasi0
        
        kullaniciSayfasi0 = kullaniciSayfasi(self,kurSayfa0,eY,self.sock)
        katilmaSayfasi0 = katilSayfa(self,eY,self.sock,kullaniciSayfasi0)
        

        #SAYFALAR Y?NET?C?YE EKLEN?YOR
        eY.add_widget(ilkSayfa0)
        eY.add_widget(kurSayfa0)
        eY.add_widget(sunucuSayfasi0)
        eY.add_widget(katilmaSayfasi0)
        eY.add_widget(kullaniciSayfasi0)


        return eY

uygulamaOls().run()
"""
if __name__ == "__main__":
    try:
        uygulamaOls().run()
    except Exception as b:
        f = open("error.ini","w")
        f.write("uygulama" + str(b))
        f.close()

"""

