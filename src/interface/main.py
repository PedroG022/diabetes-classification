import flet as ft
from fletrt import Router

from pages import Index


def main(page: ft.Page):
    page.title = "Diabetes Analysis"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    page.theme = ft.theme.Theme(
        color_scheme_seed="purple"
    )

    page.theme_mode = ft.ThemeMode.LIGHT

    Router(
        page=page,
        starting_route='/',
        routes={
            '/': Index()
        }
    )


ft.app(target=main, view=ft.WEB_BROWSER, port='40444')
