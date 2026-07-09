from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Static
from components.footer import Footer
from components.logo import BrandHeader , TitleBlock







class HomeScreen(Screen):
    def compose(self):
        elements = [["tab", "cycle options"], ["← →", "change value"],  ["ctrl+q", "quit"]]
        yield BrandHeader()
        yield Footer(elements=elements, id="main-footer")