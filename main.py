import requests
from PIL import Image, ImageDraw, ImageFont
import json
import config
import time
import textwrap

posts = 3

from instagrapi import Client
cl = Client()
cl.login(config.username, config.password)

while True:
    category = 'success'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': config.api_key})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)


    parsed_data = json.loads(response.text)


    quote = parsed_data[0]["quote"]
    author = parsed_data[0]["author"]

    img = Image.open("sigma_male.png")
    title_font = ImageFont.truetype('Upright.otf', 100)
    title_text = quote
    image_editable = ImageDraw.Draw(img)

    margin = offset = 300
    for line in textwrap.wrap(title_text, width=40):
        image_editable.text((margin, offset), line, font=title_font, fill="#FFFFFF")
        offset += title_font.getsize(line)[1]


    img.save("result.jpg")

    media = cl.photo_upload(
        path = 'result.jpg',
    caption = "#"+str(posts),
        extra_data= {
            "disable_comments": False,
            "like_and_view_counts_disabled": False
        }
    )
    time.sleep(120)
    posts += 1