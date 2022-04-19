from AI_Poker.Poker.Board import Board
from AI_Poker.Poker.Deck import Deck
from AI_Poker.Poker.AIPlayer import NeatPlayer
import os
import neat
from AI_Poker import visualize


def run_batch(players) -> None:
    deck = Deck()
    board = Board(players, deck)
    for i in range(100):
        board.hand()
    for player in players:
        player.self_evaluate()

def evaluation(genomes, config):
    players = [
        NeatPlayer("neat!", 10000, genome, config) for genome_id, genome in genomes
    ]
    num_batches = int(len(players)/20)+1
    print(f"Running {len(players)} players in {num_batches} batches")
    batch_size = len(players)/num_batches
    player_batches = []
    for batch in range(num_batches):
        start = int(batch * batch_size)
        stop = int((batch+1) * batch_size)
        player_batches.append(
            players[start:stop]
        )
    for i, batch in enumerate(player_batches):
        print(f"batch {i}")
        run_batch(batch)

def main() -> None:
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
    p.add_reporter(neat.Checkpointer(5))

    # Run for up to 300 generations.
    winner = p.run(evaluation, 300)

    # Display the winning genome.
    # print('\nBest genome:\n{!s}'.format(winner))

    # # Show output of the most fit genome against training data.
    # print('\nOutput:')
    # winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    # for xi, xo in zip(xor_inputs, xor_outputs):
    #     output = winner_net.activate(xi)
    #     print("input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))

    # node_names = {-1:'A', -2: 'B', 0:'A XOR B'}
    visualize.draw_net(config, winner, True)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
    # p.run(eval_genomes, 10)


if __name__ == '__main__':
    main()
