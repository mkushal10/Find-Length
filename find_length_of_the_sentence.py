# Use a Python function that takes a list of words and returns the length of the string.

def getLongestWordLength(input_str):
    len_list = []
    for each in input_str:
        len_list.append(len(each))
    return max(len_list)

if __name__ == "__main__":
    list_word = input('Enter the sentence : ').split()
    print(getLongestWordLength(list_word))
