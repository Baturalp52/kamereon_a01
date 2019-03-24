# -*- coding: cp1254 -*-
#ODA KURULDUĞUNDA ÇALIŞACAK SCRİPT
from varbs import *
from kivy.core.window import Window
from mesajEkrani import mesajEkrani
from kivy.app import App
import cipher
import popups

class sunucuSayfasi(mesajEkrani):

    def __init__(self, app, kurSayfa, smager,sock):
        #BAŞLANGIÇ AYARLAMALARI
        super(sunucuSayfasi, self).__init__(app, smager)
        self.name = "sunucuSayfasi"
        self.sock = sock
        self.s_sock = None
        self.acikKEY = None
        self.kapaliKEY = None

        #SUNUCU BİLGİLERİ ALINIYOR
        self.IP = kurSayfa.degsknGonder()[0]
        self.PORT = kurSayfa.degsknGonder()[1]
        self.SIFRE = kurSayfa.degsknGonder()[2]

    def kapat(self):
        self.s_sock.sendall("QUIT")

    def gonderBtnFonk(self,touch):
        try:
            mesaj = unicode(self.mesajKutu.text)
            mesaj ="0MSG" + cipher.cipher(self.acikKEY,mesaj)
            self.s_sock.sendall(mesaj)
            self.mesajAl.text += "<Siz> " + unicode(self.mesajKutu.text) + "\n"
            self.mesajKutu.text = ""
            self.mesajKutu.focused = True
            
        except Exception as a:
            popups.Error().open()
            print a
            
    def yenisocket(self):
        try:
            Window.on_close = App().stop
            if self.s_sock:
                self.s_sock.sendall("QUIT")
        except Exception as e:
            print e
        finally:    
            self.sock.close()
        



        

        


        
        
        
        
