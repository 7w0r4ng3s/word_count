import textract, re
import os
import glob
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 

os.chdir('portfolio')

file_names = glob.glob("*.pdf")

words = []
text = textract.process('Introduction.pdf')
words = re.findall(r"[^\W_]+", text.decode('utf-8'), re.MULTILINE)

words_list = []
for file in file_names:
    text = textract.process(file)
    words = re.findall(r"[^\W_]+", text.decode('utf-8'), re.MULTILINE)
    words_list += words


words_list = list(filter(lambda a: a != 'Commented', words_list))
len(words_list)

unique_string=(" ").join(words_list)
wordcloud = WordCloud(font_path='/word_count/product-sans/Product Sans Regular.ttf',
                      width=1920, 
                      height=1080, 
                      background_color='white'
                      ).generate(unique_string)

plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("word_cloud.png", bbox_inches='tight', dpi=1000, quality=95)
plt.show()
plt.close()