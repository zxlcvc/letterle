# LetterLe

LetterLe started as a quick tool I made for a friend who kept getting tilted in Discord’s Letter League.
Originally it was a chaotic joke GUI (on purpose), but I’ve cleaned it up and rebranded it into something actually usable.

Despite the original meme origins, LetterLe is a legitimately useful helper for Letter League, Scrabble, anagrams, Boggle, or any game where you need to quickly see what words you can make from a pile of letters.

# What it does

Takes manual input of letters

Can attempt to detect letters from the screen via OCR
(works, but depends heavily on your setup — think of it as a bonus feature though I wouldn't recomend using it)

Shows the best / longest words you can build

Uses a full Scrabble-legal dictionary (words.txt)

Simple, fast, no nonsense

# Why I made it

A friend of mine kept losing Letter League matches and getting tilted, so I made the original version out of spite and comedy.
That version looked like a 1998 malware pop-up.

This one is actually meant to be usable.

# Requirements

You’ll need:

Python
Python 3.9+

Packages

Install dependencies with:

pip install customtkinter mss pillow pytesseract

Tesseract OCR (optional)

OCR is optional.
If you want it, install Tesseract:

Windows download:
https://github.com/tesseract-ocr/tesseract

Then update the path in the script if needed:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


If you don’t care about OCR, the manual mode works perfectly without it.

# Included dictionary

words.txt contains:

Every valid Scrabble word

Cleaned list, one word per line

Minimum 3 letters

This is the same type of list used in competitive anagram/word-solver tools.

# How to run
python letterle.py


Enter your letters or try the OCR capture button.
The app will list the strongest words you can build.
