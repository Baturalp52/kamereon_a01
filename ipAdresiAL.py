#IP TANIMLAYICI SCRIPT by ew1g
import urllib


def ipAL():
    ip = urllib.urlopen("http://api.ipify.org/").read()
    return ip

