from AI_Poker.Poker.Board import Board
from AI_Poker.Poker.Deck import Deck
from AI_Poker.Poker.AIPlayer import NeatPlayer, RandomPlayer
import os
import neat
import numpy as np
from AI_Poker import visualize
import matplotlib.pyplot as plt
import copy
from multiprocessing import freeze_support, Pool


def run_batch(players) -> None:
    deck = Deck()
    board = Board(players, deck)
    for i in range(100):
        board.hand()
    for player in players:
        player.self_evaluate()
    # return [
    #     pla
    # ]

def run_all_players_in_batches(players, players_per_batch:int=5):
    num_batches = int((len(players)/players_per_batch)+1)
    print(f"Running {len(players)} players in {num_batches} batches")
    batch_size = len(players)/num_batches
    player_batches = []
    for batch in range(num_batches):
        start = int(batch * batch_size)
        stop = int((batch+1) * batch_size)
        player_batches.append(
            players[start:stop]
        )
    # with Pool() as pool:
    #     pool.map(run_batch, player_batches)
    # for player in players:
    #     print(player.money)
    for i, batch in enumerate(player_batches):
        print(f"batch {i}")
        run_batch(batch)
        
def evaluation(genomes, config):
    players = [
        NeatPlayer("neat!", 10000, genome, config) for genome_id, genome in genomes
    ]
    run_all_players_in_batches(players)

def winner_plot(generation_nums, generation_scores) -> None:
    x = generation_nums
    y = generation_scores
    for num, score in zip(x, y):
        print(f"{num} - {score}")
    plt.plot(x, y)
    plt.xlabel("Generation number")
    plt.ylabel("Final money")
    plt.title("Generation comparison")
    plt.show()


def main() -> None:
    freeze_support()
    max_generations = 10
    checkpoint_every = int(max_generations/20)
    local_dir = os.path.dirname(__file__)
    config_file = os.path.join(local_dir, 'config-feedforward')
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(checkpoint_every))

    # Run for up to 300 generations.
    global_winner = p.run(evaluation, max_generations)

    # Display the winning genome.
    # print('\nBest genome:\n{!s}'.format(winner))

    # # Show output of the most fit genome against training data.
    # print('\nOutput:')
    # winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    # for xi, xo in zip(xor_inputs, xor_outputs):
    #     output = winner_net.activate(xi)
    #     print("input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))

    # node_names = {-1:'A', -2: 'B', 0:'A XOR B'}
    

    generation_winners = []
    gen_numbers = []
    for i in np.arange(start=checkpoint_every-1, stop=max_generations, step=checkpoint_every):
        checkpoint_file = f'neat-checkpoint-{i}'
        gen_numbers.append(i)
        p = neat.Checkpointer.restore_checkpoint(checkpoint_file)
        winner = p.run(evaluation, 1)
        deck = Deck()
        winner_player = NeatPlayer(f"neat!-{i}", 10000, winner, config)
        generation_winners.append(
            NeatPlayer(f"neat!-{i}", 10000, winner, config)
        )
        random = RandomPlayer("random", 10000)
        players = [random, winner_player] 
        board = Board(players, deck)
        for _ in range(10):
            board.hand()
        log_results(i, random, winner_player)

    run_all_players_in_batches(generation_winners, players_per_batch=20)
    
    visualize.draw_net(config, global_winner, True)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)
    winner_plot(gen_numbers, [winner.money for winner in generation_winners])

def log_results(gen_number: int, random_player, winner_player) -> None:
    print(f"-- generation {gen_number} --")
    print(f"random end: {random_player.money}")
    print(f"winner end: {winner_player.money}")
                     

if __name__ == '__main__':
    main()
