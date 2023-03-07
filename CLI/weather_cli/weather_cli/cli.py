"""
The command line interface
"""

import argparse

from __init__ import __version__
from rich.console import Console
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


def generate_icon(weather_id: int):
    if weather_id in range(200, 233):
        print("⛈\n")
    if weather_id in range(300, 322):
        print("\n")
    if weather_id in range(500, 532):
        print("🌧\n")
    if weather_id in range(600, 623):
        print("🌨\n")
    if weather_id in range(701, 742):
        print("🌫\n")
    if weather_id in range(781, 782):
        print("🌪\n")
    if weather_id in range(801, 805):
        print("☁\n")


def format_output():
    console = Console()

    api_data: dict = get_api_data()

    console.print(f"|Country, city", style="blue", end="\t")
    console.print(f"Temperature", style="yellow", end="\t")
    console.print("Description", style="green", end="\t")
    console.print("Icon Description|", style="red", end="\n")
    console.print("+-----------------------------------------"
                  "----------------------+", style="white", end="\n")
    console.print(f"|{api_data['sys']['country']}, {api_data['name']}", style="blue", end="\t")
    console.print(f"  {api_data['main']['temp']}`{'F' if parse_args().units else 'C'}", style="yellow", end="\t")
    console.print(f"{api_data['weather'][0]['description']}   ", style="green", overflow=True, end="\t")
    generate_icon(api_data['weather'][0]['id'])


if __name__ == '__main__':
    format_output()
