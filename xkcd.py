import argparse
import os
import json
import json
from PIL import Image
import requests
from io import BytesIO
from random import randint

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
        if random:
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--random",
        action="store_true",
        help="Get a random comic."
    )
    args = parser.parse_args()
    
    cli(args.random)
