"""
The command line interface
"""

import argparse
import sys

from requests import exceptions
from rich.console import Console
from rich.table import Table

from __init__ import __version__
from query_api import build_url, query_api


def parse_args():
    parser = argparse.ArgumentParser(
        prog="weather-cli tools",
        epilog="Thanks for using weather-cli tools",
        description="Check your city weather condition in command line.",
    )

    parser.version = f"weather cli v{__version__}"
    parser.add_argument("--version", "-v", action="version")

    parser.add_argument("city", type=str,
                        nargs="+", help="Enter your city's name")
    parser.add_argument("--units", "-u", action="store_true",
                        help="Temperature conversion between Celsius and "
                             "Fahrenheit")
    return parser.parse_args()


def get_api_data():
    """
    This function format the output for the user.
    """
    args = parse_args()

    url = build_url(args.city, args.units)
    api_data = query_api(url)
    return api_data


def generate_icon(weather_id: int) -> str:
    weather_emoji = ""
    if weather_id in range(200, 233):
        weather_emoji = "⛈"
    if weather_id in range(300, 322):
        weather_emoji = ""
    if weather_id in range(500, 532):
        weather_emoji = "🌧"
    if weather_id in range(600, 623):
        weather_emoji = "🌨"
    if weather_id in range(701, 742):
        weather_emoji = "🌫"
    if weather_id in range(781, 782):
        weather_emoji = "🌪"
    if weather_id in range(801, 805):
        weather_emoji = "☁"
    return weather_emoji


def format_output():
    table = Table()
    console = Console(emoji=True)

    try:
        api_data: dict = get_api_data()
        table.add_column(f"Country, city", style="blue")
        table.add_column(f"Temperature", style="yellow")
        table.add_column("Description", style="green", )
        table.add_column("Icon Description|", style="red")
        table.add_row(f"{api_data['sys']['country']}, {api_data['name']}",
                      f"{api_data['main']['temp']}`{'F' if parse_args().units else 'C'}",
                      f"{api_data['weather'][0]['description']}",
                      generate_icon(api_data['weather'][0]['id']))
    except exceptions.ConnectionError:
        console.print("No Internet Connection...", style="red")
        sys.exit()
    except KeyError:
        console.print("City Not Found...", style="red")
    else:
        console.print(table)


if __name__ == '__main__':
    format_output()
