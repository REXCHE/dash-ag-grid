from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid Layout and Style",
)

text1 = """
# Overview of grid style and conditional cell style
"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.layout.cell_styling", make_layout=make_tabs),
        # up_next("text"),
    ],
)
