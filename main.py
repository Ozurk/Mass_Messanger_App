import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from tkinter import messagebox
from kivy.properties import StringProperty
from kivy.properties import DictProperty
from pprint import pprint
from kivy.event import EventDispatcher
import pandas


def get_dict_from_csv(path_to_csv):
    csv_file = pandas.read_csv(path_to_csv)
    phonebook = csv_file.set_index('Full Name')['Personal Phone'].to_dict()
    result_dict = DictProperty(phonebook)

    return result_dict


class MassMessage(BoxLayout):
    message = StringProperty("")
    phonebook = get_dict_from_csv("data/SF Employee.csv")
    recipients = DictProperty()


    def save_and_notify(self, *args):
        label = self.ids["Input1"]
        self.message = (label.text)
        messagebox.showinfo("Notice", f"Message{self.message} will be sent to")
        print(self.message)
        print(self.phonebook)
    
    def create_user_list(self, *args):
        self.clear_widgets()
        userlist = GridLayout(rows=10, cols=20)
        self.add_widget(userlist)
        for key in self.phonebook:
            new_button = Button(text=f'{key}', font_size=10, height=15)
            userlist.add_widget(new_button)
            print(type(self.phonebook))
        
    
            

            

   


class MassMessageApp(App):
    def build(self):
        return MassMessage()


if __name__ == '__main__':
    app = MassMessageApp()
    app.run()
