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
    return [
        player.self_evaluate() for player in players
    ]

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
    if stop != len(players):
        lost_batch = []
        for i in np.arange(start=stop, stop=len(players)):
            lost_batch.append(players[i])
        player_batches.append(lost_batch)
            
    with Pool() as pool:
        batch_results = pool.map(run_batch, player_batches)
    for players, batch_result in zip(player_batches, batch_results):
        for player, result in zip(players, batch_result):
            player._genome.fitness = result
        
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
    max_generations = 200
    checkpoint_every = int(max_generations/200)
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
        print(f"determining winner from generation: {i}")
        checkpoint_file = f'neat-checkpoint-{i}'
        gen_numbers.append(i)
        p = neat.Checkpointer.restore_checkpoint(checkpoint_file)
        winner = p.run(evaluation, 1)
        deck = Deck()
        winner_player = NeatPlayer(f"neat!-{i}", 10000, winner, config)
        generation_winners.append(
            NeatPlayer(f"neat!-{i}", 10000, winner, config)
        )

    run_all_players_in_batches(generation_winners, players_per_batch=20)
    
    visualize.draw_net(config, global_winner, True)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)
    winner_plot(gen_numbers, [winner._genome.fitness for winner in generation_winners])

                     

if __name__ == '__main__':
    main()
