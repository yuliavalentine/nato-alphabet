import pandas

nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}

word = None

while word == None:
    word = input("Please, enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        word = None
    else:
        print(output_list)
