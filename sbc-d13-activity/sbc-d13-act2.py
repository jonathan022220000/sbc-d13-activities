def tokenize_sentence(sentence):
    tokens = []
    current_token = ' '
    
    for char in sentence:
        current_token += char
        if char == '.' or char == '?' or char == '!':
            tokens.append(current_token.strip())
            current_token = " "
    
    if current_token:
        tokens.append(current_token.strip())
    
    return tokens

user_sentence = input("Enter a sentence for tokenization: ")

tokenized_sentence = tokenize_sentence(user_sentence)
print(tokenized_sentence)