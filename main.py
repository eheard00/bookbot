def main():
    with open("books/frankenstein.txt") as book:
        text = book.read()
        #print(text+"\n")

    print("               Report on the text of Frankenstein\n----------------------------------------------------------------")
    count_words(text)
    count_chars(text)
    print("----------------------------------------------------------------")

def count_words(text):
    word_count = len(text.split())
    print(f"There are {word_count} words in the text of frankenstein. \n")

def sort_on(dictionary):
    return dictionary["count"]

def count_chars(text):
    lower_text = text.lower()
    output = []
    char_count = {}

    for char in lower_text:
        if char.isalpha() == False:
            None
        elif char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in char_count:
        value = {"char": char, "count": char_count[char]}
        output.append(value)

    output.sort(reverse=True, key=sort_on)

    for char in output:
        print(f"The letter '{char["char"]}' appears {char["count"]} times.")

main()