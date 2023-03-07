"""
The command line interface
"""

import argparse


def parse_args():
    parser = argparse.ArgumentParser(
            prolog="Weather CLI", epilog="Thanks for using weather-cli",
            description="Check your city weather condition")

