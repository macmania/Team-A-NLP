#Helpful code prepared by XuanZhang and Tarek Kanan
#CS4984 Class (Computational Linguistics) Sept. 2014

import string
import nltk
import re

# For Unit 4, the routine filter_numbers has been added to what was provided for U3.
# The next four functions help clean up the corpus and can be used in various units.
# The last function, findtags, was helpful with U3.

# Remove the non-English words
def filter_non_alpha_words(words):
    result =[]
    for w in words:
        flag = True
        for ch in w:
            if not ch.isalpha():
                flag = False
                break
        if flag:
            result = result + [w]    
    return result

# Remove numbers
def filter_numbers(word_list):
    numbers = re.compile(r'[0-9]')
    word_list = [numbers.sub("", word) for word in word_list] 
    return word_list

# Remove the non English characters, punctuation, and numbers
def filter_non_alpha_chars(str):
    result = ""
    pcSet = set(string.punctuation)
    dgSet = set(string.digits)
    for ch in str:
        if ch.isalpha() or ch in pcSet or ch in dgSet or ch == " ":
            result = result + ch
    return result

# Remove the empty lines
def filter_empty_lines(str, encoding="utf8"):
    lines = str.split("\n")
    result = ""
    for line in lines:
        if len(line.strip()) > 0:
            result = result + "\n" + line.encode(encoding)
    return result


# For U3
def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                   if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].keys()) for tag in cfd.conditions())
