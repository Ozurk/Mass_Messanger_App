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
        userlist = GridLayout(rows=100, cols=5, size_hint_y=None, height=self.height )
        scrollwidget = ScrollView()
        scrollwidget.add_widget(userlist)
        self.add_widget(scrollwidget)
        for key in self.phonebook:
            new_button = Button(text=f'{key}', font_size=10)
            userlist.add_widget(new_button)
        
        

        

            

            

   


class MassMessageApp(App):
    def build(self):
        return MassMessage()


if __name__ == '__main__':
    app = MassMessageApp()
    app.run()
