from app import app
from flask import render_template, request, jsonify, url_for, redirect
from app.generation import *
from app.pokemon import *

gen_pokemon = gen_read()
generations = get_gen(gen_pokemon)

@app.route('/', methods=['GET', 'POST'])
def index():
    #pokemons = ["Please choose a generation, then a pokemon"]

    if request.method == 'POST':
        nat_dex = request.form.get('pokemon')
        return redirect(url_for('get_pokemon_data', nat_dex=nat_dex))

    return render_template('home.html', generations=generations)

@app.route('/pokemon/<int:nat_dex>')
def get_pokemon_data(nat_dex):
    data = pokemon_data(nat_dex)

    return render_template(
        'bulbabadeia.html', 
        name=data['name'], 
        dex=data['id'], 
        height=data['height'], 
        weight=data['weight'])

@app.route('/pokemon/<generation>')
def get_pokemon(generation):
    pokemons = gen_pokemon[generation]

    pokemon_arr = []
    for pokemon in pokemons:
        pokeObj = {}
        pokeObj['nat_dex'] = pokemon[0]
        pokeObj['name'] = pokemon[1]
        pokemon_arr.append(pokeObj)
    
    return jsonify({'pokemon': pokemon_arr})

@app.route('/images/<pokemon>')
def get_pokemon_image(pokemon):
    image = pokemon_image(pokemon)

    return jsonify({'image': image})