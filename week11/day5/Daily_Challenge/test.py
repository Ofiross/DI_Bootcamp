from flask import Flask, render_template, url_for, redirect, flash
import requests
import json


def pokemon_by_type():
    img = []
    url = f"https://pokeapi.co/api/v2/type/fighting"
    try:
        uResponse = requests.get(url)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    pokemon_names = data['pokemon']
    for id_num in pokemon_names:
        www = id_num['pokemon']["url"]
        li = list(www.split("/")[-2])
        id = ''.join([str(elem) for elem in li])
        num = int(id)
        img.append(num)
    print(img)


pokemon_by_type()
