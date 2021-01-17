fileName = "plik_do_odczytu.txt"
fileOutput = "plik_do_zapisu.txt"

try:
    with open(fileName, "r", encoding='utf8') as f:
        data=f.read()
    with open(fileOutput, "w", encoding='utf8') as fo:
        fo.write(data)

except IOError as e:
    print(e)

finally:
    if 'f' in locals():
        f.close()

    if 'fo' in locals():
        fo.close()
