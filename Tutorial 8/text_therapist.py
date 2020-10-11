import random

hedges = ( "Please, tell me a little more.",
           "Many of my patients tell me the same thing.",
           "Please, carry on talking." ,
           "What is your point?")

qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")

#I have also changed all functions to use word.lower() so that capitalisation does not lead to the words not being changed.

replacements = {"I":"you", "me":"you", "my":"your","we":"you", "us":"you", "mine":"yours", "am":"are", "you": "I", "are": "am", "you're": "I'm"}

#really don't know any more single-word abbreviations
text_replacements = {
    "you": "u",
    "are": "r",
    "your": "ur",
    "you're": "ur"
}

#dict is inefficient for this but instructions say to use - and this is a tutorial on dicts so I guess I will
vowels = {
    "a": "",
    "e": "",
    "i": "",
    "o": "",
    "u": ""
}

history = []

def removeVowels(word):
    new_word = ""
    for char in word:
        new_word += vowels.get(char.lower(), char) 

    return new_word

def changetoText(sentence):
    words = sentence.split()

    processed_words = []
    for word in words:
        new_word = text_replacements.get(word.lower(), word)

        #some 4 character words are really hard to read with vowels removed. Oh well, instructions haha.
        if len(new_word) > 3:
            processed_words.append(removeVowels(new_word))
        else:
            processed_words.append(new_word)

    return " ".join(processed_words)


def reply(sentence):
    """Builds and returns a reply to the sentence."""
    
    probability = random.randint(1, 20)
    #print(probability) #not getting caught out on this again like in the test where I lost marks for fully removing the print statement, even though it wasn't needed after testing haha.

    history.append(sentence)

    if probability <= 5:
        return random.choice(hedges)
    elif probability >= 18 and len(history) > 5:
        #'Earlier' gets hit really hard by the abbreviations... 'rlr'   
        return f"Earlier, you said that {changePerson(random.choice(history))}"
    else:
        return random.choice(qualifiers) + changePerson(sentence) + " ?"
        
def changePerson(sentence):
    """Replaces first person pronouns with second person pronouns."""
    
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word.lower(),word))
    return " ".join(replyWords)

def main():
    """Handles the interaction between patient and doctor."""
    
    print(changetoText("Good morning, I hope that you are well today ?"))
    print(changetoText("What can I do for you ?"))
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print(changetoText("Have a nice day"))
            break
        print(changetoText(reply(sentence)))

main()
