from textual.app import App
from textual.widgets import Header, Footer, Button, Static
from textual.containers import Container

class TestRunnerTUI(App):
    CSS = """
    Screen {
        align: center middle;
    }

    Container {
        width: 60;
        height: auto;
        border: solid green;
        padding: 1;
    }

    Button {
        width: 100%;
        margin: 1;
    }

    Static {
        width: 100%;
        height: auto;
        margin: 1;
    }
    """

    BINDINGS = [
        ("q", "quit", "Sair"),
    ]

    def compose(self):
        yield Header()
        yield Footer()
        yield Container(
            Static("qa-auto - Framework de Testes", id="title"),
            Button("Executar Testes API", id="run_api"),
            Button("Executar Testes UI", id="run_ui"),
            Button("Executar Todos", id="run_all"),
            Static("", id="status"),
        )

    def on_button_pressed(self, event):
        button_id = event.button.id
        status = self.query_one("#status", Static)

        if button_id == "run_api":
            status.update("Executando testes de API...")
        elif button_id == "run_ui":
            status.update("Executando testes de UI...")
        elif button_id == "run_all":
            status.update("Executando todos os testes...")

if __name__ == "__main__":
    app = TestRunnerTUI()
    app.run()
