import flet as ft

def main(page: ft.Page):
    # استخدام flet لعرض الموقع بدلاً من المكتبة الخارجية
    page.add(ft.WebView("https://sayedabobakr-droid.github.io/taiping-search/", expand=True))

ft.app(target=main)
