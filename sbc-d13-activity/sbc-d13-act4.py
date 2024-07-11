def subword_tokenizer(word):
    subwords = []
    if word == " ":
        subwords.append(word[:6] + '#' * 3)
        subwords.append(word[-3:])
    else:
        subwords.extend([word[:2], '##' + word[2:]] if len(word) > 3 else [word])
    return subwords

user_word = input("Enter a word: ")

tokenized_subwords = subword_tokenizer(user_word)

print("Subword Tokenization:", tokenized_subwords)