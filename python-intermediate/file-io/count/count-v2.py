import collections
import pathlib

def count_unique_words(filename:pathlib.Path):
    # your code here 
    with open(filename) as f:
        text = f.read()
    chars = {".":"", ",":"", "!":"", "?":"", ":":"", ";":"", "\n":" ", "\'":"", "-":"", "[":"", "]":""}
    for key, val in chars.items():
        text = text.replace(key, val)
    text = text.lower()
    word = collections.Counter()
    word.update(text.split())
    for w, cnt in word.most_common(10):
        print(w, cnt)

if __name__ == '__main__':
    count_unique_words(pathlib.Path('./hamlet.txt'))
    