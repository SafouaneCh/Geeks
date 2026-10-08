
longest_sentence = ""

sentence = input("Enter a sentence without the character “A” is in: ")
while "A" in sentence or "a" in sentence:
    print("The sentence contains the character 'A'. Please try again.")
    sentence = input("Enter a sentence without the character “A” is in: ")
longest_sentence = sentence

while True:
    new_sentence = input("Enter a sentence without the character “A” is in: ")
    while "A" in new_sentence or "a" in new_sentence:
        print("The sentence contains the character 'A'. Please try again.")
        new_sentence = input("Enter a sentence without the character “A” is in: ")

    if len(new_sentence) > len(longest_sentence):
        print("congratulations! you have entered a new longer sentence without the character 'A'")
        longest_sentence = new_sentence
