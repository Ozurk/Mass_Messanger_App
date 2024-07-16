import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

class MassMessage(BoxLayout):
    pass
    

class MassMessageApp(App):
    def build(self):
        return MassMessage()
    

if __name__ == '__main__':
    app = MassMessageApp()
    app.run()