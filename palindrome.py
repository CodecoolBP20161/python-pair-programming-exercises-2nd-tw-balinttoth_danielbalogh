def is_palindrome(word):

    char_list = []

    for char in list(word):
        if char != " ":
            char_list.append(char)

    word_to_observe = "".join(char_list).lower()

    if word_to_observe == word_to_observe[::-1]:
        return True

    else:
        return False



def main():

    if is_palindrome("Indul a gorog aludni"):
        print("Yes, it is a palindrome.")
    else:
        print("No, it is not a palindrome.")

main()
