from glob import glob
from random import shuffle
from os.path import abspath
from pathlib import Path
import webbrowser

RECURSIVE = True
PARENT_DIR = abspath("./split/")

cards = glob(PARENT_DIR + "/*/*.pdf", recursive=RECURSIVE)
cards_uri = [Path(card).as_uri() for card in cards]

shuffled_cards = cards_uri.copy()
shuffle(shuffled_cards)

arg = None
index = 0
num_cards = len(shuffled_cards)
while (arg != "q") & (index <= num_cards):
    webbrowser.open(shuffled_cards[index], new=0, autoraise=True)
    arg = input("Press any key to continue. 'q' to quit.\n")
    index += 1
