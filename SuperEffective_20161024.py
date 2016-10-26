# This is my solution to Reddit's Daily Programmer challenge of 2016-10-25
# We can use Pokemon API to calculate solution: http://pokeapi.co/api/v2/type/fire/
import requests
import json

NAME = 'name'
DAMAGE_RELATIONS = 'damage_relations'
NO_DAMAGE_TO = 'no_damage_to'
HALF_DAMAGE_TO = 'half_damage_to'
DOUBLE_DAMAGE_TO = 'double_damage_to'


def print_help():
    print('Usage:')
    print('To get a multiplier:           move -> pokemon type')


def print_error(e):
    print("Error: " + e.args[0])
    print("Type 'help' for more info.")


def check_alternative_inputs(line):
    line = line.strip().replace(' ', '-')
    if line == 'help' or line == 'usage':
        print_help()
    else:
        print('Type "help" for more info')


class PokemonMovesCalculatorException(Exception):
    """
        Custom exception to handle errors in this program
    """
    pass


def obtain_pokemon_type(line):
    pokemon = line.split("->")[1].strip()
    return pokemon


def obtain_move(line):
    move = line.split("->")[0].strip()
    return move


def call_multiplier_api(pokemon_type):
    url = 'https://pokeapi.co/api/v2/type/'+str(pokemon_type)+'/'
    result = requests.get(url)
    if result.ok:
        data = json.dumps(result.json())
        return json.loads(data)
    else:
        raise PokemonMovesCalculatorException('"{}" is not a Pokemon Type'.format(pokemon_type))


def parse_response(data_json):
    return data_json[DAMAGE_RELATIONS]


def obtain_multiplier_by_move(multipliers, move):
    zeros = multipliers[NO_DAMAGE_TO]
    halfs = multipliers[HALF_DAMAGE_TO]
    doubles = multipliers[DOUBLE_DAMAGE_TO]
    for i in zeros:
        if move == i[NAME]:
            return '0x'
    for i in halfs:
        if move == i[NAME]:
            return '0.5x'
    for i in doubles:
        if move == i[NAME]:
            return '2x'
    return "1x"


def obtain_multiplier(line):
    pokemon_type = obtain_pokemon_type(line)
    move = obtain_move(line)
    try:
        response = call_multiplier_api(pokemon_type)
        multipliers = parse_response(response)
        return obtain_multiplier_by_move(multipliers, move)
    except PokemonMovesCalculatorException as e:
        raise e


def process_input(line):
    try:
        result = obtain_multiplier(line)
        print(result)
    except PokemonMovesCalculatorException as e:
        print_error(e)
    except Exception as e:
        print_error(e)


def main():
    line = input(' >')
    while len(line) > 0:
        if '->' in line:
            process_input(line)
        else:
            check_alternative_inputs(line)
        line = input('> ')


if __name__ == '__main__':
    main()
