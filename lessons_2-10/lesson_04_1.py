user_text = input("Enter a sentence consist of two words: ")
first_word, second_word = user_text.split()

new_string_1 = "! %s %s ?" % (second_word.capitalize(), first_word.upper())
new_string_2 = "! {1} {0} ?".format(first_word.upper(), second_word.capitalize())
new_string_3 = f"! {second_word.capitalize()} {first_word.upper()} ?"

file = open("for_print.txt", "w")
print(user_text, new_string_1, new_string_2, new_string_3, sep="<<<>>>", file=file)
file.close()
