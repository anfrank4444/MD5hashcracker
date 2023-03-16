import hashlib
import itertools
import string

input_hashes = ["5f4dcc3b5aa765d61d8327deb882cf99", "827ccb0eea8a706c4c34a16891f84e7b",                "d8578edf8458ce06fbc5bb76a58c5ca4", "0d107d09f5bbe40cade3de5c71e9e9b7",                "d3eb9c72f6da0c4e52be16e0b0c74e18"]
input_strings = ["password", "12345", "qwerty", "letmein", "monkey"]

wordlist = []
for i in range(1, 7):  # generate all strings of length 1 to 6
    for word in itertools.product(string.ascii_lowercase, repeat=i):
        word = ''.join(word)
        hashed_word = hashlib.md5(word.encode('utf-8')).hexdigest()
        if hashed_word in input_hashes:
            wordlist.append(input_strings[input_hashes.index(hashed_word)])

print(wordlist)
