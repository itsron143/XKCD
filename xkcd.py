import os
import click
import json
import urllib.request
import json
import urllib
from PIL import Image
import requests
from io import BytesIO
from random import randint


@click.command()
@click.option('--random', flag_value='random', default=False, help='Get Random Comic!')
def cli(random):
    """XKCD Terminal Tool"""
    #click.echo('Hello World!')
    # os.system('figlet -c "X K C D" | lolcat')
    # print(random)
    try:
        from sh import lolcat, figlet # Hacky fix for Build to pass system packages
        print(lolcat(figlet("-c", "X K C D")))
    except ImportError:
        print("Welcome to xkcd Comics!")
    rand_digits = randint(100, 999)
    try:
        if random == 'random':
            endpoint = "https://xkcd.com/{}/info.0.json".format(rand_digits)
        else:
            endpoint = "https://xkcd.com/info.0.json"

        with urllib.request.urlopen(endpoint) as url:
            data = json.loads(url.read().decode())
            response = requests.get(data['img'])
            img = Image.open(BytesIO(response.content))
            img.show()

    except urllib.error.URLError:
        error_image = Image.open("assets/xkcd_404.jpg")
        error_image.show()
