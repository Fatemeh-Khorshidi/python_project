print("\n\nEnter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it:")
inputText = []
while True:
    try:
        item = input()
    except EOFError:
        break
    inputText.append(item)


output = ""
my_dict = {}
spaceSentence = ""

# compile input text
for item in inputText:
    if item != "<end_of_dic>":
        items = item.split()
        key, values = items[0], items[1:]
        my_dict[key] = values
    else:
        break

spaceSentence = inputText[-1]
isEndOfInput = False
head = 0

while not isEndOfInput:

    pivot = 1
    canSearchForNextWord = False
    candidate = ""

    isFindWord = False

    while not canSearchForNextWord:

        currentSearchingWord = spaceSentence[head: head + pivot]

        if currentSearchingWord in my_dict:
            # find a word in dic
            isFindWord = True
            candidate = currentSearchingWord

        # update pivot until find a word OR reach to end of line
        if head + pivot == len(spaceSentence):
            # reach end of the line
            if isFindWord:
                output += my_dict.get(candidate)[0]
                head = head + len(candidate)
            else:
                output += "."
                head += 1

            output += " "
            canSearchForNextWord = True
            isFindWord = False
        else:
            # go for next cycle
            pivot += 1

    if head == len(spaceSentence):
        isEndOfInput = True

print("\n\noutput: "+output)
