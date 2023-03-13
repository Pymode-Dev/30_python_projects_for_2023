from pathlib import Path
from pytube import YouTube
from rich.console import Console
from rich.table import Table


class YtVideo(YouTube):
    def __init__(self, url: str) -> None:
        super().__init__(url)

    def show_video_info(self):
        table = Table()
        console = Console()
        table.add_column("Title")
        table.add_column("Creator")
        table.add_column("Views")

        table.add_row(self.title, self.author, self.views)
        console.print(table)

    def download_video(self, video_resolution):
        video = self.streams.get_by_resolution(video_resolution)
        format_path = Path.home() / "Videos"
        video.download(format_path)
