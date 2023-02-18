import flet as ft
from backend import BackendYoutube
from tkinter import filedialog, Tk


class YoutubeDownloader:

    def __init__(self, page: ft.Page):
        self.directory = None
        self.page = page
        self.page.title = "Youtube Downloader"
        self.page.vertical = "center"
        self.page.window_height = 500
        self.page.window_width = 400
        self.selected_format = None

        def on_m4a_clicked(_):
            self.selected_format = "m4a"
            self.step.value = "Selected format: M4A"
            self.page.update()

        def on_mp4_hd_clicked(_):
            self.selected_format = "mp4-1080p"
            self.step.value = "Selected format: MP4 1080p"
            self.page.update()

        self.format = self.selected_format
        self.url_input = ft.TextField(label="Enter YouTube URL")

        self.selected_path = ft.Text()
        self.step = ft.Text(size=12)

        self.selected_path.value = "File Location:"
        self.step.value = "Select a format first:"

        def on_download_clicked(e):
            if not self.url_input.value:
                self.url_input.error_text = "Please enter a valid URL"
                self.page.update()
            else:
                self.url_input.error_text = None
                self.page.update()

            if self.selected_format is not None:
                self.format = self.selected_format
                self.run_backend(self.url_input.value, self.format, self.directory)
            else:
                self.step.value = "No format selected, please select a format first."
            self.page.update()

        def on_directory_clicked(e):
            root = Tk()
            root.withdraw()
            root.wm_attributes("-topmost", 1)
            path = filedialog.askdirectory()
            self.directory = path
            self.selected_path.value = f" {path}"
            root.destroy()
            self.page.update()

        self.selected_directory = ft.TextButton("Choose File Path", on_click=on_directory_clicked)
        self.m4a_button = ft.TextButton("M4A", on_click=on_m4a_clicked)
        self.mp4_hd_button = ft.TextButton("MP4 1080p", on_click=on_mp4_hd_clicked)
        self.download_button = ft.TextButton("Download", on_click=on_download_clicked)

        self.download_complete = ft.Text()

        self.page.add(
            ft.Column(
                [
                    ft.ResponsiveRow([
                        self.url_input
                    ], spacing=20),

                    ft.Row([
                        self.selected_directory
                    ]),

                    ft.Row([
                        self.selected_path,
                    ], wrap=True, spacing=20),

                    ft.Row([
                        self.step
                    ],
                        alignment=ft.MainAxisAlignment.CENTER),

                    ft.Row([
                        self.m4a_button, self.mp4_hd_button
                    ],
                        alignment=ft.MainAxisAlignment.CENTER),

                    ft.Row([
                        self.download_button
                    ],
                        alignment=ft.MainAxisAlignment.CENTER),

                    ft.Row([
                        ft.Text(self.format)
                    ],
                        alignment=ft.MainAxisAlignment.CENTER),

                    ft.Row([
                        self.download_complete
                    ],
                        alignment=ft.MainAxisAlignment.CENTER),
                ])
        )

    def run_backend(self, url, format, output_dir):
        backend = BackendYoutube(url, format, output_dir=self.directory)
        backend.selected_format = format
        backend.download_format()


def run_gui():
    ft.app(target=YoutubeDownloader)


if __name__ == "__main__":
    run_gui()
