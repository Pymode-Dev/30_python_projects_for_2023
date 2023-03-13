from argparse import ArgumentParser
from rich.console import Console
from rich.table import Table


def parse_arguments():
    cli_parser = ArgumentParser(prog="YouTube CLI Downloader",
                                description="Download YouTube videos using "
                                            "cli",
                                epilog="Thanks for using this tool.")

    subparser_args = cli_parser.add_subparsers(dest="command")

    video = subparser_args.add_parser("video")
    video.add_argument()

    playlist = subparser_args.add_parser("playlist")
    playlist.add_argument("Link")

    channel = subparser_args.add_parser("channel")
    channel.add_argument("Link")

    return cli_parser.parse_args()


def main():
    args = parse_arguments()
    return args


if __name__ == '__main__':
    main()
