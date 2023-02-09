import collections
import pathlib

def count_unique_words(filename:pathlib.Path):
    with open(filename) as f:
        text = f.read()
    chars = {".":"", ",":"", "!":"", "?":"", ":":"", ";":"", "\n":" ", "\'":"", "-":"", "[":"", "]":""}
    for key, val in chars.items():
        text = text.replace(key, val)
    text = text.split(' ')
    text = [word.strip().lower() for word in text if word!=""]
    final = [f'{word} - {count}' for word, count in 
             sorted(collections.Counter(text).items(), key=lambda x: x[1], reverse=True)]
    return final


if __name__ == '__main__':
    text = count_unique_words(pathlib.Path('./hamlet.txt'))
    for word in text[:10]:
        print(word)