import socket
import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty

KV = """
MyBL:
        orientation: 'vertical'
        size_hint: (0.95, 0.95)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        
        Label:
                font_size: '12sp'
                multiline: True
                text: root.data_label

        Button:
                text: 'Заблокировать'
                font_size: '12sp'
                background_color: '#232323'
                on_press: root.callback()

        Button:
                text: 'Открыть приложение'
                font_size: '12sp'
                background_color: '#232323'
                on_press: root.callback2()
                
"""

class MyBL(BoxLayout):
        data_label = StringProperty('Управление Legion 7')

        def callback(self):
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(("192.168.51.116", 8080))
                client.send("заблокировать".encode("utf-8"))

        def callback2(self):
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(("192.168.51.116", 8080))
                client.send("открыть приложение".encode("utf-8"))
                

class MyApp(App):
        running = True

        def build(self):
            return Builder.load_string(KV)

        def on_stop(self):
            self.running = False

MyApp().run()

