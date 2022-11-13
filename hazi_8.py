def destroyfile(filepath): 
    with open(filepath, 'r') as novella:

        line = novella.readline()
        punctuation = ".,?!"
        wovel = "aáeéiíoóöőuúüű"
        result = []

        while line:
            if not line.isspace():
                newline = line.translate(line.maketrans('', '', punctuation)).translate(line.maketrans('', '', wovel))  #ékezetes betűket nem távolítja el, de azt feltételezem, hogy ez nem a kód hibája, hanem valami encoding probléma
                result.append(newline)
            line = novella.readline()

    return result        

def writefile(filepath, text):
    with open(filepath, 'w') as g:
        for index, line in enumerate(text, start= 1):
            if(index % 3 == 0):
                g.write(line)        

writefile("result.txt", destroyfile("be.txt"))