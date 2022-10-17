from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
from kivy.modules.screen import devices
from kivy.core.window import Window
from kivy.uix.image import Image

Window.size = (375, 565)

class Test_1(Screen):
    def dell(self):
        a = self.manager.get_screen('test2').ids.gg_1.remove_widget(self.ids.gg)
        print(a)

class Test_2(Screen):
    pass

class Test(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(Test_1(name='test1'))
        sm.add_widget(Test_2(name='test2'))

        return sm



if __name__ == '__main__':
     Test().run()
