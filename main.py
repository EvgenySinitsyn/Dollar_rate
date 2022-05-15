import requests
from bs4 import BeautifulSoup
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


page = requests.get(
    'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4')

soup = BeautifulSoup(page.text, 'html.parser')
convert = soup.find_all("div", {"class": "BNeawe iBp4i AP7Wnd"})
kurs = convert[1].text[:5]


class MyApp(App):

    def __init__(self, kurs):
        super().__init__()
        self.kurs = kurs

    def build(self):
        b1 = BoxLayout(orientation='vertical')
        b1.add_widget(Label(text=str(self.kurs)))
        b1.add_widget(Button(text='jjj'))
        return b1

MyApp(kurs).run()
