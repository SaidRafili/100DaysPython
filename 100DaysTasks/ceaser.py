alphabet = [' ',"a","b","c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print("Welcome to Ceaser Cypher tool!")
text = input('Type your message: ').lower()
key = int(input('Type the number of characters to be shifted: '))
textSeperated = list(text)

for i in textSeperated:
    if i in alphabet:
        indeximsi = alphabet.index(i)
        if indeximsi == 0:
            indeximsi == indeximsi
        else:
            indeximsi += key
            cypher = ""
            cypher += alphabet[indeximsi]
            print(cypher)
    
