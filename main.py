import random
import numpy as np
import string
import os

os.system('clear')

# WORDS = ["apple", "banana", "cherry", "dragonfruit"]
WORDS = ["cat", "dog", "bat", "tab"]
BOARDSIZE = 5

def random_board():
    board = np.zeros((BOARDSIZE, BOARDSIZE), dtype=str)
    for a in range(BOARDSIZE):
        for b in range(BOARDSIZE):
            board[a][b] = random.choice(string.ascii_lowercase)

    return board

def place_words(board):
    word_coords = {a: [] for a in WORDS}
    used_coords = []
    for word in WORDS:
        placed = False
        while not placed:
            direction = random.choice(["horizontal", "vertical", "diagonal"])
            if direction == "horizontal":
                x = random.randint(0, BOARDSIZE - len(word))
                y = random.randint(0, BOARDSIZE - 1)
                if (x, y) not in used_coords:
                    for i in range(len(word)):
                        board[x + i][y] = word[i]
                        word_coords[word].append((x + i, y))
                    used_coords.extend(word_coords[word])
                    placed = True
            elif direction == "vertical":
                bad = True
                while bad:
                    x = random.randint(0, BOARDSIZE - 1)
                    y = random.randint(0, BOARDSIZE - len(word))
                    if (x, y) not in used_coords:
                        for i in range(len(word)):
                            board[x][y + i] = word[i]
                            word_coords[word].append((x, y + i))
                        bad = False
                        for a in word_coords[word]:
                            if a in used_coords:
                                bad = True
                        if bad:
                            bad = False
                            continue
                        used_coords.extend(word_coords[word])
                        placed = True
            elif direction == "diagonal":
                x = random.randint(0, BOARDSIZE - len(word))
                y = random.randint(0, BOARDSIZE - len(word))
                if (x, y) not in used_coords:
                    for i in range(len(word)):
                        board[x + i][y + i] = word[i]
                        word_coords[word].append((x + i, y + i))
                    used_coords.extend(word_coords[word])
                    placed = True


    return board

# print(random_board())
print(place_words(random_board()))