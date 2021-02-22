from kivy.lang import Builder
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

Window.size = (300, 500)

class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
class MyLayout(BoxLayout):
    scr_mngr = ObjectProperty(None)
    def change_screen(self, screen, *args):
        self.scr_mngr.current = screen

class MenuOSApp(MDApp):

    def on_start(self):

        pass

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        instance_tab.ids.label.text = tab_text

if __name__ == '__main__':
    MenuOSApp().run()