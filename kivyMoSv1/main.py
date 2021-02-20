from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (330, 500)

class MyLayout(BoxLayout):
    scr_mngr = ObjectProperty(None)
    def change_screen(self, screen, *args):
        self.scr_mngr.current = screen

class MenuOSApp(MDApp):
    def on_start(self):
        pass

if __name__ == '__main__':
    MenuOSApp().run()