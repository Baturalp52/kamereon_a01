# -*- coding: cp1254 -*-
import socket,threading,cipher

from kivy.core.window import Window
from kivy.app import App


class cliSOCK:
    def __init__(self,ip,key,socket,accs):
        self.ip = ip
        self.key = key
        self.socket = socket
        self.accs = accs



class serverSOCK:
    def __init__(self,socket):
        self.socket = socket

global RECV_BUFFER
RECV_BUFFER = 4096
global CONNECTION
CONNECTION = True

def mesajAL(sock,sun_EKRAN,key,ip):
    global CONNECTION
    kosul = True
    while kosul:
        try:
            mesaj = sock.recv(RECV_BUFFER)

            if mesaj.startswith("0MSG"):
                mesaj = mesaj[4:]
                mesaj = cipher.decipher(sun_EKRAN.kapaliKEY,mesaj)
                sun_EKRAN.mesajAl.text += "<{}> ".format(ip) + mesaj + "\n"

                
            if mesaj.startswith("0KEY"):
                sock.sendall("0KEY"+key)

                
            if mesaj == "QUIT":
                CONNECTION = True
                Window.on_close = App().stop
                sock.close()
                sun_EKRAN.mesajAl.text += u"{} kullanıcısı konuşmadan ayrıldı. ".format(ip) + "\n"

                
        except Exception as e:
            sock.close()
            kosul = False
            hata = e.args[0]
            if hata == 10054:
                sun_EKRAN.mesajAl.text += u"{} kullanıcısının bağlantısı koptu ".format(ip) + "\n"
                Window.on_close = App.stop



def bglntiACIK(loader,sayfa):
    loader.dismiss()
    sayfa.current = "sunucuSayfasi"
    


def baglanti_AL(sock,SIFRE,sun_EKRAN,key):
    global CONNECTION
    while True:
        if CONNECTION:
            cli, addr = sock.accept()

                
            clisock = cliSOCK(addr[0],"",cli,"")

            giris= clisock.socket.recv(RECV_BUFFER)
            sifre = giris[4:giris.index("0KEY")]


            if sifre == SIFRE:
                Window.on_close = sun_EKRAN.kapat
                CONNECTION =False

                sun_EKRAN.mesajAl.text += u"{} adresli kullanıcı bağlandı.".format(addr[0])+"\n"

                clisock.key = giris[giris.index("0KEY")+4:giris.index("ACCS")]            
                if giris[giris.index("ACCS")+4:] == "root":
                    clisock.accs = "root"
                else:
                    clisock.accs = "mber"
                                    
                sun_EKRAN.s_sock = clisock.socket
                sun_EKRAN.acikKEY = clisock.key
                clisock.socket.sendall("0KEY"+key)


                mesajAL0 = threading.Thread(target=mesajAL,args=[clisock.socket,sun_EKRAN,key,clisock.ip])
                mesajAL0.start()

                
            else:
                
                sun_EKRAN.mesajAl.text += u"{} adresli kullanıcı yanlış şifre girdi!".format(addr[0])+"\n"
                clisock.socket.sendall("WPAS")
                clisock.socket.close()
        else:
            continue
    

def main(sock,SIFRE, loader, sayfa,PORT,sun_EKRAN,key):
    

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server = serverSOCK(sock)
    

    
    
    sock.bind(("0.0.0.0",PORT))
    sock.listen(5)
    #BAGLANTI SAGLANDIGINDA OLACAK OLANLAR
    bglntiACIK(loader,sayfa)
    
    #loader, sayfa,
                

    sunucu = threading.Thread(target=baglanti_AL, args=[sock,SIFRE,sun_EKRAN,key])
    sunucu.start()

        

