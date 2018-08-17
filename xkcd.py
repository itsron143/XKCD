import os
import click
from PIL import Image
import requests
from io import BytesIO
from random import randint


@click.command()
@click.option('--random', flag_value='random', default=False, help='Get Random Comic!')
def cli(random):
    """XCKD Terminal Tool"""
    #click.echo('Hello World!')
    os.system('figlet -c "X K C D" | lolcat')
    # print(random)
    rand_digits = str(randint(100, 999))
    if random == 'random':
        with requests.get("https://xkcd.com/" + rand_digits + "/info.0.json") as r:
            data = r.json()
            img_url = requests.get(data['img'])
            img = Image.open(BytesIO(img_url.content))
            img.show()
    else:
        with requests.get("https://xkcd.com/info.0.json") as r:
            data = r.json()
            img_url = requests.get(data['img'])
            img = Image.open(BytesIO(img_url.content))
            img.show()
