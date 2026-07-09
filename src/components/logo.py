from textual.widget import Widget
from textual.widgets import Static
from textual.containers import Horizontal, Vertical
from lib import state


class BellyLogo(Static):
    def __init__(self, letter="b", **kwargs):
        super().__init__(letter, **kwargs)


class TitleBlock(Vertical):
    def compose(self):
        yield Static("belly", id="app-title")
        yield Static(f"v{state.APP_VERSION}", id="app-version")

class BrandHeader(Horizontal):
    DEFAULT_CSS = """
    BrandHeader{
        content-align: center middle;
    }
    .gold-card {
        width: 5;
        height: 3;
        color: #F5C462;
        border: round #F5C462;
        text-style: bold;
        content-align: center middle;
        margin-top: 1;
    }

    #title-stack {
        height: 4;
        width: 10;
        margin-top: 2;
        margin-left:1;

    }

    #app-title {
        
        color: #f2f2f2;
        text-style: bold;
    }

    #app-version {
        color: #555555;
    }
"""
    def compose(self):
        yield BellyLogo(classes="gold-card")
        yield TitleBlock(id="title-stack")