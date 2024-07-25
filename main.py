import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from tkinter import messagebox
from kivy.properties import StringProperty
from kivy.properties import DictProperty
from pprint import pprint
from kivy.uix.screenmanager import ScreenManager, Screen
import pandas
from kivy.lang.builder import Builder


def get_dict_from_csv(path_to_csv):
    csv_file = pandas.read_csv(path_to_csv)
    phonebook = csv_file.set_index('Full Name')['Personal Phone'].to_dict()
    result_dict = phonebook

    return result_dict


class MassMessage(ScreenManager):
    message = StringProperty("")
    phonebook = get_dict_from_csv("data/SF Employee.csv")
    recipients = DictProperty()


class StartScreen(Screen):
    pass

class NameSelectorScreen(Screen):
    tech_names = MassMessage.phonebook.keys()

        
    def create_tech_names(self):
        namegrid = self.ids.NameGrid
        for tech in self.tech_names:
            btn = Button(text=f"{tech}", size_hint_y=None, height=30)
            namegrid.add_widget(btn)
            


class MassMessageApp(App):
    def build(self):
        return MassMessage()


if __name__ == '__main__':
    app = MassMessageApp()
    app.run()

