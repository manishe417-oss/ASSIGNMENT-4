try:
    file1= open ('sample.txt','r+')
    reading_file = file1.readline()
    reading_file1=file1.readline()
    print('Reading file contexts')
    print('line 1:',reading_file)
    print('line 2:',reading_file1)
    file1.close()
except FileNotFoundError:
    print('The File does not exist')
finally:
    print('thank you')

