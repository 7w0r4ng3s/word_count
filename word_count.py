# import dependencies
import textract, re
import os
import glob

# change dir to the portfolio folder containing all pdf files
os.chdir('portfolio')

# all files names 
file_names = glob.glob("*.pdf")

if len(file_names) == 0:
    print(f'You have {len(file_names)} files in "portfolio" directory: ')
else:   
    for i in file_names:
        print(i)
    
print()

# count the word count of each file and add them together
count = 0
for name in file_names:
    text = textract.process(name)
    words = re.findall(r"[^\W_]+", text.decode('utf-8'), re.MULTILINE)
    print(f'The word count in file {name} is {len(words)}')
    count += len(words)
    
print(f'\nThe total word count of your PORTFOLIO is {count}')