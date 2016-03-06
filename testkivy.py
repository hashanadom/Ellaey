__author__ = 'Matan'
import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemLabel

class Ellaey(App):
    icon = 'icon_for_now_1.PNG'

    def build(self):
        box = BoxLayout(orientation='horizontal')
        t = TextInput(text="You can try and enter a text, maybe i'll help you", multiline=False,
                                  size_hint = (.3,.1 ))
        f = t._get_text()
        c = ListItemLabel()
        box.add_widget(t)
        return box

if __name__ == '__main__':
    Ellaey().run()