print("\n<---- Search Engine ---->\n")

sentences = ["What is Python", "How to learn python programming Language", "Python is not snake python", "Learn C++ in one video", "Learn javascript in one video", "Learn PHP login registration", "Learn css framework Bootstrap", "Practise is important to learn programming"]

inpQuery = input("Enter your Query String: ")

results = []

nResult = 0
for sentence in sentences:
    if inpQuery.lower() in sentence.lower():
        results.append(sentence)
        nResult += 1

if nResult < 2:
    print(f"\n{nResult} result found:\n")
else:
    print(f"\n{nResult} results found:\n")

n = 1
for result in results:
    print(f"{n}. {result}")
    n += 1