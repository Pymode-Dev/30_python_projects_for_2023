from configparser import ConfigParser


def parse_api_key() -> str:
    """
    Parse the api key from secrets.ini
    """
    config_parser = ConfigParser()
    config_parser.read("../secrets.ini")
    return config_parser["openweather_api"]["api_key"]
