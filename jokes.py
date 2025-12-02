'''Auto-graded task 2
1. Create a new Python fi le in this folder called jokes.py.
2. You are going to create a random joke generator using Python’s random module. This will require a bit of research on your part.
3. Create a list of jokes that include their punchlines.
4. Use the random module to display a random joke each time the code runs.'''

import random

jokes = ["Why did the cat sit on the computer?\nBecause it wanted to keep an eye on the mouse.",
    "What do you call a pile of kittens?\nA meow-tain.",
    "Why are cats bad storytellers?\nThey only have one tail.",
    "What do cats wear to sleep?\nPaw-jamas.",
    "Why did the cat get kicked out of the orchestra?\nIt kept playing by ear.",
    "What’s a cat’s favourite colour?\nPurr-ple.",
    "Why did the cat take a nap on the photocopier?\nIt wanted to make some cat-alogs.",
    "What do you call a cat who loves bowling?\nAn alley cat.",
    "Why don’t cats play poker in the jungle?\nToo many cheetahs.",
    "What do cats eat for breakfast?\nMice Krispies."]

print(random.choice(jokes))
