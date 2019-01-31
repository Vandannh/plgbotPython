import characters
import json

with open('characters.json', 'w') as file
    chars = [Character("1337", "warrior"), Character("6969", "warrior")]
    json.dump(chars, file)
