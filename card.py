from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

font = ImageFont.truetype("OpenSans-Semibold.ttf", size=25)

def get_green_card(name, img, status, activity):
    g_card = get_card("green", name, img, status, activity)
    return g_card


def get_blue_card(name, img, status, activity):
    b_card = get_card("blue", name, img, status, activity)
    return b_card


def get_purp_card(name, img, status, activity):
    p_card = get_card("purp", name, img, status, activity)
    return p_card


def get_yellow_card(name, img, status, activity):
    y_card = get_card("yellow", name, img, status, activity)
    return y_card


def get_white_card(name, img, status, activity):
    w_card = get_card("white", name, img, status, activity)
    return w_card

def get_card(card_name, name, img, status, activity):
    card = Image.open("cards/{}_card.png".format(card_name))
    draw = ImageDraw.Draw(card)
    draw.text((50, 10), str(name), font=font, fill='black')
    draw.text((50, 190), "status:"+str(status), font=font, fill='black')
    draw.text((50, 125), "activity:"+str(activity), font=font, fill='black')
    response = requests.get(img)
    avatar = Image.open(BytesIO(response.content))#, Image.ANTIALIAS)
    avatar = avatar.resize((130, 130))
    card.paste(avatar, (60, 45, 190, 175))
    card.save("user_cards/{}_{}_card.png".format(card_name, name))
    return "user_cards/{}_{}_card.png".format(card_name, name)


