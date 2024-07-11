def tokenize_characters(sentence):
    tokens = [char for char in sentence]
    return tokens

user_sentence = input("Enter a sentence for character tokenization: ")

tokenized_characters = tokenize_characters(user_sentence.strip().replace("'", '"'))
print(tokenized_characters)