def mostWantedLetter(text):
    letterref = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    anstable = [None] * 26
    for i in text:
        if i not in letterref:
            continue
        x = letterref.index(i)
        if x > 25:
            x = x - 26
        if anstable[x] != None:
            anstable[x] = anstable[x] + 1
        else:
            anstable[x] = 1
    return letterref[anstable.index(max(anstable))].lower()

if __name__ == '__main__':
	print "Enter a string of letters, and I will tell you the letter you"
	print "most frequently used.\n"
	print "If two letters are tied, the alphabetically first letter will be"
	print "returned.\n"
	while True:
		text = raw_input("Enter your string (and make sure it's only letters):\n")
		if text.isalpha():
			print mostWantedLetter(text)
			break
		else:
			print "Something went wrong.\n"