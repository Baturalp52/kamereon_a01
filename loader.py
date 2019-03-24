#-*- coding: cp1254-*-
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from varbs import *



class Loader(ModalView):
    def __init__(self):
        super(Loader,self).__init__()
        self.size_hint = (.8, .1)
        self.background = u"srcs/white.jpg"
        self.auto_dismiss = False

        self.icerikEKLE()

    def icerikEKLE(self):
        self.duzen = BoxLayout(orientation="horizontal")

        self.loader = Image(anim_delay=0, source=u"srcs/Disk.gif", size_hint_x=.2)
        self.text = Label(text=u"Yükleniyor...", size_hint_x=.8, bold=True, color=(0, 0, 0, .5),font_name=def_font)

        self.duzen.add_widget(self.loader)
        self.duzen.add_widget(self.text)

        self.add_widget(self.duzen)
