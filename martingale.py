import random

RED = "Красный"
BLACK = "Черный"

COIN_VALUES = [RED, BLACK]

def flip_coin():
    return random.choice(COIN_VALUES)

#print(flip_coin())

def play_martingale(starting_founds: int, min_bet: int, max_bet: int) -> int:
    step_to_lose = 0 #количество шагов до поражения 
    curent_funds = starting_founds #текущие средства игрока
    curent_bet = min_bet
    
    while curent_funds > 0:
        print("==========")
        step_to_lose += 1
        curent_funds -= curent_bet
        print(f"{curent_funds=}, {curent_bet=}")
        flip_coin_value = flip_coin()
        
        if flip_coin_value == RED:
            win = curent_bet * 2
            print(f"{win=}")
            curent_bet += win
            curent_bet = min_bet
        else:
            print("loose")
            curent_bet *= 2
            if curent_bet > max_bet:
                curent_bet = min_bet
            if curent_bet > curent_funds:
                curent_bet = curent_funds
                
    return step_to_lose
    
#print(play_martingale(starting_founds = 200, min_bet = 5, max_bet = 300))
    

def simulate_martingale_for_n_players(starting_founds: int, min_bet: int, max_bet: int, n_games: int) -> float:
    total_steps_to_lose = 0
    
    for i in range(n_games):
        step_to_lose = play_martingale(
            starting_founds = starting_founds,
            min_bet = min_bet,
            max_bet = max_bet,
        )
        total_steps_to_lose += step_to_lose
        
    return total_steps_to_lose / n_games

print(
    simulate_martingale_for_n_players(
        starting_founds = 1000,
        min_bet = 10,
        max_bet = 500,
        n_games = 10
    )
)

