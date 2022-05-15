from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):

    def build(self):
        b1 = BoxLayout(orientation='vertical')
        b1.add_widget(Label(text='asdasd'))
        b1.add_widget(Button(text='jjj'))
        return b1

MyApp().run()