print ("Welcome to the Pig Latin Translator!")

original = raw_input("Enter a word: ")

if len(original) > 0 and original.isalpha() :
    print ("You chose: " + original)
    word = original.lower()
else: 
    print ("This is not a valid entry.")