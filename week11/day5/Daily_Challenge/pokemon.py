from flask import Flask, render_template, url_for, redirect, request
import requests
import json


app = Flask(__name__)


@app.route('/')
@app.route('/pokemons')
def pokemon_types():
    url = f"https://pokeapi.co/api/v2/type"
    try:
        uResponse = requests.get(url)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    pokemons_types = data['results']
    return render_template('index.html', pokemons=pokemons_types)


@app.route('/pokemon/<id>')
def pokemon(id):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    try:
        uResponse = requests.get(url)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    pokemon_id = data['id']
    type = data['types'][0]['type']['name']
    return render_template('pokemonId.html', pokemon=data, id=pokemon_id, type=type)


@app.route('/pokemons/bytype/<type>')
def pokemon_by_type(type):
    url = f"https://pokeapi.co/api/v2/type/{type}"
    try:
        uResponse = requests.get(url)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    pokemon_names = data['pokemon']
    group_type = type
    return render_template('type.html', pokemons=pokemon_names, type=group_type)


@app.route('/pokemons/byname', methods=['POST', 'GET'])
@app.route('/pokemons/byname/<name>')
def pokemon_by_name(name=''):
    if request.method == 'POST':
        name = request.form.get('search_bar').lower()
    try:
        requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
        return redirect(url_for('pokemon', id=name))
    except requests.ConnectionError:
        return redirect(url_for('all_pokemons'))


@app.route('/pokemons/all')
def all_pokemons():
    url = f"https://pokeapi.co/api/v2/pokemon?limit=1500"
    try:
        uResponse = requests.get(url)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    all_pokemons_names = data['results']
    return render_template('allPokemons.html', all_pokemons=all_pokemons_names)


if __name__ == "__main__":
    app.run(debug=True, port=6845)
