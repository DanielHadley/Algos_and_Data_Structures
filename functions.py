# -*- coding: utf-8 -*-
# Self Check
# Here’s a self check that really covers everything so far. You may have heard of the infinite monkey theorem? The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long do you think it would take for a Python function to generate just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”

# You’re not going to want to run this one in the browser, so fire up your favorite Python IDE. The way we’ll simulate this is to write a function that generates a string that is 27 characters long by choosing random letters from the 26 letters in the alphabet plus the space. We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.

# A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s progress this third function should print out the best string generated so far and its score every 1000 tries.
import string
import random

BillSentence = "methinks it is like a weasel"


def monkeyWriting():
	"""simulates monkeys writing on a keyboard"""
	m = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
	i = ''.join(random.choice(string.ascii_lowercase) for _ in range(2))
	ii = ''.join(random.choice(string.ascii_lowercase) for _ in range(2))
	l = ''.join(random.choice(string.ascii_lowercase) for _ in range(4))
	a = ''.join(random.choice(string.ascii_lowercase) for _ in range(1))
	w = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
	return " ".join([m, i, ii, l, a, w]) 


def compareBillToMonkeys():
	score = 0
	monkeySentence = monkeyWriting()
	for m, b in zip(monkeySentence, BillSentence):
		if m == b:
			score += 1
	return [score - 5, monkeySentence] # Because of hte blanks

print compareBillToMonkeys()

def monkeyProgress():		
	score = compareBillToMonkeys()
	while score < 23:
		score = compareBillToMonkeys()

print monkeyProgress()