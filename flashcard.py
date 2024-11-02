from glob import glob
from random import shuffle
from os.path import abspath, sep, basename
from pathlib import Path
import webbrowser

RECURSIVE = True
PARENT_DIR = abspath("./split/")

topics = glob(abspath(PARENT_DIR + "/*" + sep))
topics_dict = {
    int(basename(topic)[0]): {"name": basename(topic)[2:].strip(), "path": topic}
    for topic in topics
}
print("Select the topic. Leave blank to include all topics.")
for i in range(len(topics_dict)):
    print(f"{i + 1}: {topics_dict[i + 1].get('name')}")

selector = input()
if selector == "":
    glob_dir = PARENT_DIR + "/*/*.pdf"
else:
    glob_dir = topics_dict[int(selector)].get("path") + "/*.pdf"

cards = glob(glob_dir, recursive=RECURSIVE)
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
