import random
import requests
import webbrowser

for iter in range(15):
    chess_game_template = 'https://www.chess.com/game/live/'
    chess_game_num = random.randint(1, 140000000000)
    chess_game_num = str(chess_game_num)
    stringify_chess_num = chess_game_num.rjust(12, '0')
    game_url = chess_game_template + stringify_chess_num
    client = requests.get(game_url)
    response = client.status_code

    #print(f'The chess game number is: {chess_game_num}')
    #print(f'Chess game response: {response}')
    #print(str(iter) + ' ' + game_url)

    webbrowser.open_new_tab(game_url)