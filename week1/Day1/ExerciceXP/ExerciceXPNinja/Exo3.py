paragraph = "Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group of sentences or a single sentence that forms a unit” (Lunsford and Connors). Length and appearance do not determine whether a section in a paper is a paragraph."

print(f"The number of characters in the paragraph is: {len(paragraph)}")

sentences = paragraph.split(". ")
print(f"The number of sentences in the paragraph is: {len(sentences)}")

words = paragraph.split(" ")
print(f"The number of words in the paragraph is: {len(words)}")

unique_words = set(words)
print(f"The number of unique words in the paragraph is: {len(unique_words)}")

result = 0
for char in paragraph:
    if char != " ":
        result += 1
print(f"The number of non-space characters in the paragraph is: {result}")

list_of_numbers_of_words = []

for sentence in sentences:
    somme = 0
    for word in sentence.split(" "):
        somme += 1
    list_of_numbers_of_words.append(somme)

print(f"The average amount of words per sentence in the paragraph is: {sum(list_of_numbers_of_words) / len(list_of_numbers_of_words)}")

non_unique_words = 0
for word in words: 
    if word not in unique_words:
        non_unique_words += 1
print(f"The number of non-unique words in the paragraph is: {non_unique_words}")