
def CountLetters(inputstring):
    dict = {}
    inputstring = inputstring.lower()
    
    for c in inputstring:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1

    print(f"Betűk gyakorisága: {dict}")  
    
# CountLetters függvényhez:  
# Először nem esett le hogy ki lehet egyben iratni a dictionaryt, szóval a vesszőket meg zárójeleket manuálisan rakosgattam oda:
def AltSolution(dict):
    bracket = ""
    for k in dict:
        bracket = bracket + f"'{k}': {dict[k]}, "
    print("{" + bracket[:-2] + "}")    
 #  utána rájöttem hogy túlkomplikáltam de büszke vagyok magamra hogy kilogikáztam így, még ha felesleges is :D 


    
            
def MirrorString(inputstring):
    print("Fordítva: " + inputstring[::-1])

def SplitString(inputstring):
    split = inputstring.split(" ")
    print(f"Listába rendezve szavanként: {split}")
<<<<<<< HEAD

sentence = input("Adjon meg egy mondatot: \n")
CountLetters(sentence)
MirrorString(sentence)
SplitString(sentence)
=======
>>>>>>> 5cc9ced2983913bc03fa0b324acacbacd2baf69d


if __name__ == "__main__":    
    sentence = input("Adjon meg egy mondatot: \n")
    CountLetters(sentence)
    MirrorString(sentence)
    SplitString(sentence)

 



 
