import cipher,threading
global deger
deger = 0
def main():
    while 1:
##        global deger
##        deger+=1
##        if deger != 300:
##            dongu = threading.Thread(target=main)
##            dongu.daemon = True
##            dongu.start()

        data = open("keys","r")
        veri = data.read()
        data.close()
        veri1 = veri
        

        keys = str(cipher.getKEY())
        print keys
        if not keys in veri1:
            veri1+=keys
            file0 =open("keys","w")
            file0.write(veri1+"\n")

            file0.close()

dongu = threading.Thread(target=main)
dongu.daemon = True
dongu.start()

while 1:
    pass
