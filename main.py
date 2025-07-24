with open('count.log', 'r') as file:
    content = file.read()
    content=int(content.split()[-1])
    file.write(str(content+1)+" ")

    