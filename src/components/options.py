from textual.widgets import Static
from textual.containers import Horizontal, Vertical, Container
from textual.reactive import reactive
from textual import events
from textual.widget import Widget


class OptionGroup(Container):
    DEFAULT_CSS = """
    OptionGroup {
        layout: vertical;
        content-align: center middle;
        height: auto; 
        width: 30;
        border: solid red;
    }
    
    .header {
        color: $text-muted;
        content-align: center middle;
        width: 100%;
        height: auto;
        margin-bottom: 1;
    }
    .header.selected{
        color: #F5C462;
    }
    #option-cont {
        width: 100%;
        height: auto;
        align: center middle;
    }
    
    .option {
        color: $text-muted;
        margin: 0 2; 
        content-align: center middle;
        width:auto;
    }
    
    .option:hover {
        color: $text; 
    }
    
    .option.selected {
        color: #F5C462;
        text-style: underline;
    }
    """

    tab_selected = reactive(False)
    option_selected = reactive(0)

    def __init__(self, optionid: int, header: str, options: list[str] | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.header = header
        self.options = options or []
        self.optionid = optionid

    def compose(self):
        yield Static(self.header, classes="header selected" if self.tab_selected else "header")
        with Horizontal(id="option-cont"):
            for i, option in enumerate(self.options):
                classes = "option selected" if self.tab_selected and i == self.option_selected else "option"
                yield Static(option, classes=classes)
                
    def watch_tab_selected(self, tab_selected: bool) -> None:
        # only touch DOM if compose() has already run
        if not self.is_mounted:
            return
        header = self.query_one(".header", Static)
        header.set_class(tab_selected, "selected")
        self._refresh_option_classes()

    def watch_option_selected(self, option_selected: int) -> None:
        if not self.is_mounted:
            return
        self._refresh_option_classes()

    def _refresh_option_classes(self) -> None:
        options = self.query(".option")
        for i, opt in enumerate(options):
            opt.set_class(self.tab_selected and i == self.option_selected, "selected")


class OptionsTab(Widget):
    DEFAULT_CSS = """
    OptionsTab {
        height: 50%; 
        border: solid red;
        content-align: center middle;
    }
    """

    can_focus = True  
    current_tab = reactive(0)

    def __init__(self, collections: list[dict] | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collections = collections or []
        self.collections_length = len(self.collections)

    def _on_mount(self, event) -> None:
        self.focus()  # actually take focus so key events fire
        if self.collections_length:
            self.select_tab(0, 0)

    def compose(self):
        with Horizontal():
            for key, collection in enumerate(self.collections):
                header, options = collection["header"], collection["options"]
                yield OptionGroup(header=header, options=options, optionid=key)

    def _on_key(self, event: events.Key) -> None:
        if event.key == "tab":
            old = self.current_tab
            new = old + 1 if old + 1 < self.collections_length else 0
            self.select_tab(new, old)

    def select_tab(self, new: int, old: int) -> None:
        groups = self.query(OptionGroup)
        groups[old].tab_selected = False
        groups[new].tab_selected = True
        self.current_tab = new