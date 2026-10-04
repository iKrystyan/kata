def spin_words(sentence):
    # Your code goes here
    words = sentence.split(" ")
    
    for idx, word in enumerate(words):
        if len(word) >= 5:
            words[idx] = word[::-1]

    return " ".join(word for word in words)