from textual.containers import Vertical
from textual.screen import Screen
from components.footer import Footer
from components.logo import BrandHeader
from components.options import OptionsTab


TABS_DATA = [
    {
        "header" : "mode",
        "options" : ["time", "words", "quote"]
    },
    {
        "header" : "duration",
        "options" : ["15", "30", "60", "120"]
    }
]

footer_elements = [["tab", "cycle options"], ["← →", "change value"],  ["ctrl+q", "quit"]]        



class HomeScreen(Screen):
    def compose(self):
       
        yield BrandHeader()
        yield OptionsTab(collections=TABS_DATA)
        yield Footer(elements=footer_elements)