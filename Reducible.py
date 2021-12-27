#  File: Reducible.py

#  Description: Input a list of words and find the largest sized word
#  that can be reduced to smaller words. Then print all the words of
#  this size in alphabetical order.

#  Student Name: Anna Dougharty

#  Student UT EID: amd5933

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created: 10/21/2021

#  Date Last Modified: 10/21/2021

import sys


# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime(n):
    if n == 1:
        return False

    limit = int(n ** 0.5) + 1
    div = 2
    while div < limit:
        if n % div == 0:
            return False
        div += 1
    return True


# Input: takes as input a string in lower case and the size
#        of the hash table
# Output: returns the index the string will hash into
def hash_word(s, size):
    hash_idx = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# Input: takes as input a string in lower case and the constant
#        for double hashing
# Output: returns the step size for that string

# USE A SMALL PRIME NUMBER FOR CONSTANT

def step_size(s, const):
    return const - (hash_word(s, const))


# Input: takes as input a string and a hash table
# Output: no output; the function enters the string in the hash table,
#         it resolves collisions by double hashing
def insert_word(s, hash_table):
    # find index of new word that string will hash into
    word_idx = hash_word(s, len(hash_table))
    # if this location in hash table is empty
    if hash_table[word_idx] == '':
        # hash word into table
        hash_table[word_idx] = s
    else:
        # find step size for double hashing (if collision occurs)
        step_val = step_size(s, 3)
        # only increase index by step value if table at index is NOT empty
        while hash_table[word_idx] != '':
            word_idx = (word_idx + step_val) % len(hash_table)
        # once an empty index has been found, hash word into the table
        hash_table[word_idx] = s


# Input: takes as input a string and a hash table
# Output: returns True if the string is in the hash table
#         and False otherwise
def find_word(s, hash_table):
    word_idx = hash_word(s, len(hash_table))
    tracking_idx = word_idx
    if hash_table[tracking_idx] == s:
        return True
    else:
        # find step size for double hashing (if collision occurs)
        step_val = step_size(s, 1)
        count = 0
        # increase by step size until s at index is found
        while tracking_idx < len(hash_table) and hash_table[tracking_idx] != s and count < 3:
            tracking_idx = (tracking_idx + step_val) % (len(hash_table))
            if tracking_idx == word_idx:
                return False
            count += 1
        if tracking_idx >= len(hash_table):
            return False
    # return T/F if word is in hash table at tracking index
    return s == hash_table[tracking_idx]


# Input: string s, a hash table, and a hash_memo
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo
#         and returns True and False otherwise

# LOOK INTO MEMOIZATION FOR THIS
# Avoiding extra recursions in is_reducible by
# checking for cases where it is impossible for
# the word to be reducible

def is_reducible(s, hash_table, hash_memo):
    # if the word 's' is the letter 'a' or 'i' or 'o',
    # then it has reached its final form
    if s == 'a' or s == 'i' or s == 'o':
        return True
    # if the word is found in the hash memo, then it is
    # by definition already reducible
    elif find_word(s, hash_memo):
        return True
    # if it still contains at least one of the three letters
    # 'a', 'i', or 'o', then it has potential to be reducible
    elif 'a' in s or 'i' in s or 'o' in s:
        # if word cannot be found
        if find_word(s, hash_table) is False:
            return False
        # check each of the smaller words
        for i in range(len(s)):
            new_word = s[:i] + s[i + 1:]
            # recursively call for each sub-word
            if is_reducible(new_word, hash_table, hash_memo):
                insert_word(new_word, hash_memo)
                return True
    # if the word fails all criteria above then it is not reducible
    else:
        return False


# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words(string_list):
    max_word_length = 0
    # increase max length until largest size is found
    for word in string_list:
        if len(word) > max_word_length:
            max_word_length = len(word)

    # append words of max size to the list
    max_word_list = []
    for word in string_list:
        if len(word) == max_word_length:
            max_word_list.append(word)

    # sort list alphabetically
    max_word_list.sort()
    return max_word_list


def main():
    # create an empty word_list
    word_list = []

    # read words from words.txt and append to word_list
    for line in sys.stdin:
        line = line.strip()
        word_list.append(line)

    # find length of word_list
    length_words = len(word_list)

    # determine prime number N that is greater than twice
    # the length of the word_list
    prime_num = (length_words * 2) + 1
    while is_prime(prime_num) is False:
        prime_num += 1

    # create an empty hash_list
    hash_table = []

    # populate the hash_list with N blank strings
    for i in range(prime_num):
        hash_table.append('')

    # hash each word in word_list into hash_list
    # for collisions use double hashing
    for word in word_list:
        insert_word(word, hash_table)

    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than
    # 0.2 * size of word_list
    hash_memo = []
    hash_memo_size = int((len(word_list) * 0.2) + 1)
    while is_prime(hash_memo_size) is False:
        hash_memo_size += 1

    # populate the hash_memo with M blank strings
    for i in range(hash_memo_size):
        hash_memo.append('')

    # create an empty list reducible_words
    reducible_word_list = []

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    # as you recursively remove one letter at a time check
    # first if the sub-word exists in the hash_memo. if it does
    # then the word is reducible and you do not have to test
    # any further. add the word to the hash_memo.
    for word in word_list:
        if is_reducible(word, hash_table, hash_memo):
            reducible_word_list.append(word)

    # find the largest reducible words in reducible_words
    reducible_word_largest = get_longest_words(reducible_word_list)

    # print the reducible words in alphabetical order
    # one word per line
    for word in reducible_word_largest:
        print(word)


if __name__ == "__main__":
    main()
