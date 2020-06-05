import pyperclip, sys, shelve

# Save clipboard content.
shelfFile = shelve.open('mydata')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    shelfFile[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'get':
    try:
        pyperclip.copy(shelfFile[sys.argv[2]])
    except KeyError:
        print("Yor key is not defined,please reffer to the below keys list")
        klist = list(shelfFile.keys())
        print (klist)
elif len(sys.argv) == 2 or len(sys.argv) == 1:
    klist = list(shelfFile.keys())
    print (klist)
shelfFile.close()



