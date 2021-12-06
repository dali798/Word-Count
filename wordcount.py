"""Count words in file."""

import sys
def get_files():
    if len(sys.argv) >1:
        return sys.argv[1:]
    return -1
    

def file_to_dic(filename):

    f = open(filename)
    wc = {}

    for line in f:
        line = line.replace(",", "")
        line = line.strip(",?.\n").lower()
        words = line.split()
        for word in words: 
            wc[word] = wc.get(word, 0) + 1
    
    return wc

def print_dic(dictionary):

    for key,val in dictionary.items():
        print(f"{key} {val}")

def tokenize(filename):
    f = open(filename)

    all_words = []
    for line in f:
        line = line.replace(",", "")
        line = line.strip(",?.\n").lower()
        words = line.split()
        all_words += words
    return all_words

def count_words(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def print_word_counts(word_counts):
    print_dic(word_counts)

# print(count_words(["apple", "berry", "cherry", "apple"]))

print_word_counts({"apple": 2, "berry": 1, "cherry": 1})


files = get_files()
if files == -1:
    print("Please enter a file name.")
    sys.exit()
for file in files:
    print(file)
    dic = file_to_dic(file)
    print_dic(dic)
