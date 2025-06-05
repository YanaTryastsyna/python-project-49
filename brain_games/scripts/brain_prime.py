from brain_games.engine import engine_games
from brain_games.games.prime import GAME_RULES, generate_round


def main():
    engine_games(GAME_RULES, generate_round)


if __name__ == '__main__':
    main()