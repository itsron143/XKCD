import os
import click
import json
import urllib.request
from PIL import Image
import requests
from io import BytesIO
from random import randint
import sh

@click.command()
@click.option('--random', flag_value='random', default=False, help='Get Random Comic!')
def cli(random):
    """XCKD Terminal Tool"""
    #click.echo('Hello World!')
    #os.system('figlet -c "X K C D" | lolcat')
    sh.lolcat(sh.figlet("-c", "X K C D"))
    # print(random)
    rand_digits = str(randint(100, 999))
    if random == 'random':
        with urllib.request.urlopen("https://xkcd.com/" + rand_digits + "/info.0.json") as url:
            data = json.loads(url.read().decode())
            response = requests.get(data['img'])
            img = Image.open(BytesIO(response.content))
            img.show()
    else:
        with urllib.request.urlopen("https://xkcd.com/info.0.json") as url:
            data = json.loads(url.read().decode())
            response = requests.get(data['img'])
            img = Image.open(BytesIO(response.content))
            img.show()
