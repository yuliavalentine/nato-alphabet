import pandas

nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}

word = input("Please, enter a word: ").upper()
output_list = [nato_dict[letter] for letter in word]
print(output_list)
