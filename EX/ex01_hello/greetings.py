"""EX01 Greetings."""


greeting_word = str(input("Enter a greeting: "))
recipient = str(input("Enter a recipient: "))
multiplier = int(input("How many times to repeat: "))
greeting = (greeting_word + ' ' + recipient + '! ') * multiplier
print(greeting)
