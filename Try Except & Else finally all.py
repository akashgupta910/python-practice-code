# TRY EXCEPT AND ELSE FINALLY ALL

try:
    f1 = open("file/file.txt")

# except Exception as error:
#     print(error)

except EOFError as eoferror:
    print("IO Error!",eoferror)

except IOError as ioerror:
    print("IO Error!",ioerror)

else:
    print("Exception do not Run.")

finally:
    print("This is very Important.")

