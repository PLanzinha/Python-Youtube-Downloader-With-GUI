import yt_dlp


class BackendYoutube:
    def __init__(self, url, format, output_dir):
        self.url = url
        self.selected_format = format
        self.output_dir = output_dir

    def download_format(self):
        ydl_opts = {'outtmpl': f'{self.output_dir}/%(title)s.%(ext)s'}
        if self.selected_format == "mp4-1080p":
            ydl_opts['format'] = 'bestvideo[ext=mp4[height=1080]]+bestaudio[ext=m4a]/best'
        elif self.selected_format == "m4a":
            ydl_opts['format'] = 'm4a/bestaudio/best'
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])
