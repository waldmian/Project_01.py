"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Anna Waldhansová
email: waldmian2@gmail.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]



data = """
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+
"""

import sys

rows = data.strip().split("\n")[3:-1]
registered_users = {}

for row in rows:
  cleared_row = row.strip("|").split("|")
  user = cleared_row[0].strip()
  password = cleared_row[1].strip()
  registered_users[user] = password

paragraphs = {}
for nr, text in enumerate(TEXTS,start=1):
  paragraphs[nr] = text

separator = "-"*40
name = input("username: ")
password = input("password: ")
print(separator)

if name in registered_users and registered_users[name] == password:
  greeting = f"Welcome to the app, {name.title()}. " \
  f"There are {(len(paragraphs.keys()))} texts to be analysed."
  print(greeting)

elif name in registered_users and registered_users[name] != password:
  print("Wrong password entered. Terminating the program.")
  sys.exit(0)

else:
  print("Unregistered user. Terminating the program.")
  sys.exit(0)

print(separator)

text_nr = str(input(
    f"Enter a number btw {(list(paragraphs.keys())[0])} and "
    f"{(list(paragraphs.keys())[-1])}. \nSelected text nr: "
))
print(separator)
text_numbers = str(list(paragraphs.keys())[:])

if not text_nr in text_numbers:
  print("Wrong number / character selected. Terminating the program.")
  sys.exit(0)

    word_count = []
    word_count_title = []
    word_count_upper = []
    word_count_lower = []
    word_count_numeric = {}
    sum_digits = []


  for word in paragraphs[int(text_nr)].split():
    word.strip(",.")
    word_count.append(word)
    if word.istitle():
      word_count_title.append(word.title())

    elif word.isupper():
      word_count_upper.append(word.upper())

    elif word.islower():
      word_count_lower.append(word.lower())

    elif word.isdigit():
      word_count_numeric[word] = word.count(word)
      sum_digits.append(int(word))


print(f"There are {len(word_count)} words in the selected text.")
print(f"There are {len(word_count_title)} titlecase words.")
print(f"There are {len(word_count_upper)} uppercase words.")
print(f"There are {len(word_count_lower)} lowercase words.")
print(f"There are {len(word_count_numeric)} numeric strings.")
print(f"The sum of all the numbers is {sum(sum_digits)}.")

print(separator)
print("LEN|  OCCURENCES  |NR.")
print(separator)

text_copy = paragraphs[text_nr - 1]

separate_words = []
separate_words_length = []
length_occurence = {}

for word in text_copy.split():
  clean_word = word.strip(",.;")
  separate_words.append(clean_word)
  word_length = []
for word in separate_words:
  word_length.append(len(word))
for length in word_length:
  if length not in length_occurence:
    length_occurence[length] = 1
  else:
    length_occurence[length] += 1

for k, v in sorted(length_occurence.items()):
  stars = "*"*v
  first_width = 3
  second_width = 20
  print(f"{k:{first_width}}|{stars:<{second_width}}|{v}")
