import click
import json
from PIL import Image
import requests
from io import BytesIO
from random import randint


@click.command()
@click.option('--random', flag_value='random', default=False, help='Get Random Comic!')
@click.option('--metadata', flag_value='metadata', default=False, help='Print Comic Metadata to Terminal')
@click.option('--noimage', flag_value='noimage', default=False, help='Do not display comic image.')
def cli(random,metadata,noimage):
    """XKCD Terminal Tool"""
    try:
        from sh import lolcat, figlet # Hacky fix for Build to pass system packages
        print(lolcat(figlet("-c", "X K C D")))
    except ImportError:
        print("Welcome to xkcd Comics!")
    try:
        with requests.Session() as s:
            content = s.get("https://xkcd.com/info.0.json").content.decode()
            data = json.loads(content)
            HighestNumber = data["num"]

            if random == 'random':
                rand_digits = randint(1, HighestNumber)
                endpoint = "https://xkcd.com/{}/info.0.json".format(rand_digits)
                content = s.get(endpoint).content.decode()
                data = json.loads(content)
            
            if noimage != "noimage":
                res = s.get(data["img"])
                img = Image.open(BytesIO(res.content))
                img.show()

            print("Title: ", data["title"])
            print("Number:", data["num"])

            if metadata == 'metadata':
                print("Date:  ", data["year"]+"/"+data["month"]+"/"+data["day"])
                print("alt:   ", data ["alt"])

    except requests.ConnectionError:
        error_image = Image.open("assets/xkcd_404.jpg")
        error_image.show()
