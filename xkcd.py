import click
import json
from PIL import Image
import requests
from io import BytesIO
from random import randint


@click.command()
@click.option('--random', flag_value='random', default=False, help='Get Random Comic!')
def cli(random):
    """XKCD Terminal Tool"""
    try:
        from sh import lolcat, figlet # Hacky fix for Build to pass system packages
        print(lolcat(figlet("-c", "X K C D")))
    except ImportError:
        print("Welcome to xkcd Comics!")
    try:
        if random == 'random':
            rand_digits = randint(100, 999)
            endpoint = "https://xkcd.com/{}/info.0.json".format(rand_digits)
        else:
            endpoint = "https://xkcd.com/info.0.json"

        with requests.Session() as s:
            content = s.get(endpoint).content.decode()
            data = json.loads(content)
            res = s.get(data["img"])
            img = Image.open(BytesIO(res.content))
            img.show()

    except requests.ConnectionError:
        error_image = Image.open("assets/xkcd_404.jpg")
        error_image.show()
