from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.lang import Builder

Builder.load_string("""

<Test2>:
    GridLayout:
        cols:1

        GridLayout:
            rows:1
            Label:
                text:'Does it show all 4 tabs?'
        GridLayout:
            rows:1
            TestForTabbedPanel:
                id: tp

<CustomWidthTabb@TabbedPanelItem>
    width: self.texture_size[0]
    padding: 10, 0
    size_hint_x: None

<TestForTabbedPanel>:
    size_hint: 1,1
    do_default_tab: False
    tab_width: None

    CustomWidthTabb:
        text: "This is a Long Tab"
        Label:
            text: 'First tab content area'

    CustomWidthTabb:
        text: "This is a Long Tab"
        Label:
            text: 'Second tab content area'

    CustomWidthTabb:
        text: "Short Tab"     
        Label:
            text: 'Third tab content area'

    CustomWidthTabb:
        text: "Short Tab#2"   
        Label:
            text: 'Fourth tab content area'

""")


class Test2(Screen):
    def __init__(self, *args, **kwargs):
        super(Test2, self).__init__(*args, **kwargs)
        Clock.schedule_once(self.ids.tp.on_tab_width, 0.1)


class TestForTabbedPanel(TabbedPanel):
    pass


class TabbedPanelApp(App):
    def build(self):
        return Test2()


if __name__ == '__main__':
    TabbedPanelApp().run()