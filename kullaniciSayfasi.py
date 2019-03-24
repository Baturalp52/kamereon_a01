# -*- coding: cp1254 -*-
#ODAYA BAĞLANDIĞINDA ÇALIŞACAK SCRİPT
from varbs import *
from mesajEkrani import mesajEkrani
from kivy.core.window import Window
from kivy.app import App
import socket
import popups
import cipher


class kullaniciSayfasi(mesajEkrani):

    def __init__(self, app, kurSayfa, smager,sock):
        #BAŞLANGIÇ AYARLAMALARI
        super(kullaniciSayfasi, self).__init__(app, smager)
        self.name = "kullaniciSayfasi"
        self.sock = sock
        self.acikKEY = None
        self.kapaliKEY = None

        
    def gonderBtnFonk(self,touch):
        try:
            mesaj = unicode(self.mesajKutu.text)
            mesaj = "0MSG" + cipher.cipher(self.acikKEY,mesaj)
            self.sock.sendall(mesaj)
            self.mesajAl.text += "<Siz> " + unicode(self.mesajKutu.text) + "\n"
            self.mesajKutu.text = ""
        except Exception as e:
            popups.Error().open()
            print e

    def yenisocket(self):
        Window.on_close = App().stop
        self.sock.sendall("QUIT")
        self.sock.close()

    def kapat(self):
        self.sock.sendall("QUIT")
        self.sock.close()



        

        


        
        
        
        
