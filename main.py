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


class MassMessageApp(App):
    message = StringProperty("")
    phonebook = get_dict_from_csv("data/SF Employee.csv")
    recipients = {}
    recipients_var = StringProperty(str(recipients))

    def send_mass_message(self):
        for team_members in self.recipients:
            print(team_members, f" +1{self.recipients[team_members]}")
    


    def build(self):
        return MassMessage()
    
    
    def update_recipients_var(self):
        self.recipients_var = str(self.recipients).replace(",", "\n")
    
    

class MassMessage(ScreenManager):
    pass


class StartScreen(Screen):
    pass

class ReviewScreen(Screen):
    def on_enter(self, *args):
        app = App.get_running_app()
        app.update_recipients_var()
        self.ids.recipients_label.text = app.recipients_var

    def on_pre_leave(self, *args):
        app = App.get_running_app()
        app.message = self.ids.message_input.text
        return super().on_pre_leave(*args)
    
 
class FinalReview(Screen):
    pass



class NameSelectorScreen(Screen):
    tech_names = MassMessageApp.phonebook.keys()
    def on_enter(self, *args):
        self.create_tech_names()
        return super().on_enter(*args)
        

    def change_button_color(self, instance):
        if instance.background_color == [1, 0, 0, 1]:
            instance.background_color = (1, 1, 1, 1)
            MassMessageApp.recipients.pop(instance.text)
            
        else:
            instance.background_color = (1, 0, 0, 1)
            MassMessageApp.recipients[instance.text] = MassMessageApp.phonebook[instance.text]
            

    def select_unselect_all(self):
        for button in self.ids.NameGrid.children:
            if button.background_color == [1, 0, 0, 1]:
                button.background_color = (1, 1, 1, 1)
                MassMessageApp.recipients.pop(button.text)
            else:
                button.background_color = (1, 0, 0, 1)
                MassMessageApp.recipients[button.text] = MassMessageApp.phonebook[button.text]
            

    def create_tech_names(self):
        namegrid = self.ids.NameGrid
        for tech in self.tech_names:
            btn = Button(text=f"{tech}", size_hint_y=None, height=30)
            btn.bind(on_press=self.change_button_color)
            namegrid.add_widget(btn)
            




if __name__ == '__main__':
    app = MassMessageApp()
    app.run()

