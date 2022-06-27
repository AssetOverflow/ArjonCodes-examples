from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout
from src.config import load_settings


def main() -> None:
    settings = load_settings()
    app = Dash(
        external_stylesheets=[BOOTSTRAP],
    )
    app.title = settings.app.title
    app.layout = create_layout(app, settings)
    app.run_server(debug=settings.debug)


if __name__ == "__main__":
    main()
