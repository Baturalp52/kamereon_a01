# -*- coding: cp1254 -*-
import threading,cipher
from popups import WarningP,Alert
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.app import App




def mesajAL(sock,loader1, sayfa,kul_EKRAN,ip,yonetici):
    kosul = True
    alert = Alert()
    warning = WarningP()
    while kosul:
        
        try:
            data = sock.recv(4096)

            if data.startswith("0KEY"):
                
                kul_EKRAN.acikKEY = data[4:]
                if kul_EKRAN.acikKEY == None:
                    sock.sendall("0KEY")

                    
            if data.startswith("0MSG"):
                mesaj = data[4:]
                mesaj = cipher.decipher(sayfa.kapaliKEY,mesaj)
                kul_EKRAN.mesajAl.text+="<{}> ".format(ip) + mesaj +"\n"

                
            if data == "QUIT":
                kosul = False
                alert.text.text = u"{} mesajlaşmadan \n ayrıldı.".format(ip)
                sock.close()
                Window.on_close = App().stop
                yonetici.current = "katilSayfa"
                alert.open()

                
            if data == "WPAS":
                alert.text.text = u"Yanlış şifre girdiniz!"
                sock.close()
                yonetici.current = "katilSayfa"
                alert.open()
                
                
                    
        except Exception as e:
            if e.args == 10054:
                warning.text = u"{}'nın bağlantısı koptu.".format(ip)
                sock.close()
                yonetici.current = "katilSayfa"
                warning.open()
            
            kosul = False
            print e.args[0]



def main(sock,ip,port,sifre,key,accs,loader, sayfa,yonetici,kul_EKRAN):

    

    try:
        sock.connect((ip,port))
        kul_EKRAN.sock = sock

        data = "PASW{}0KEY{}ACCS{}".format(sifre,key,accs)
        sock.sendall(data)
        loader.dismiss()
        yonetici.current = "kullaniciSayfasi"
        Window.on_close  = kul_EKRAN.kapat
        kul_EKRAN.mesajAl.text += u"Bağlantı sağlandı!" + "\n"

        
        veridene = threading.Thread(target=mesajAL,args=[sock,loader,sayfa,kul_EKRAN,ip,yonetici])
        veridene.daemon = True
        veridene.start()
        
        
    except Exception as e:
        print e
        raise ValueError



