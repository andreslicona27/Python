from Words import Words
import genanki
import os
import time

DECK_ID = 789012
MODEL_ID = 123456

# GET WORDS
site = "https://strommeninc.com/1000-most-common-german-words-frequency-vocabulary/"
words = Words(site)
words.get_words()
time.sleep(10)


# CREATE DECK
deck = genanki.Deck(DECK_ID, 'German-English-Words')

# CREATE CARD MODEL
normal_modal = genanki.Model(
    MODEL_ID,
    'Normal card',
    fields=[
        {'name': 'UnknownWord'},
        {'name': 'KnownWord'}
    ],
    templates=[
        {
            'name': 'Vocabulary words',
            'qfmt': '{{UnknownWord}}',
            'afmt': '{{KnownWord}}',
        },
    ])

# ADD WORDS
for unknown_word, known_word in zip(words.unknown_words, words.known_words):
    card = genanki.Note(
        model=normal_modal,
        fields=[unknown_word, known_word]
    )
    deck.add_note(card)


# GENERATE FILE
package = genanki.Package(deck)
user_route = os.path.expanduser('~')
file_name = 'new_deck.apkg'
path_abs = os.path.join(user_route, file_name)

package.write_to_file(path_abs)

