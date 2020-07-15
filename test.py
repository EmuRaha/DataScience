file = open("sample.txt","a")
file.write("I am Emu")
file.close()




file = open("sample.txt","r+")
file.truncate(0)
file.close()







