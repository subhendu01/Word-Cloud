#import all the required libraries
#if you are using ubuntu system then use pip to install the packages
# if you are using windows then use conda to install

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import requests

#text for creating wordcloud
words = 'access guest guest apartment area area bathroom bed bed bed bed bed bedroom block coffee' \
        ' coffee coffee coffee entrance entry francisco free garden guest home house kettle kettle ' \
        'kitchen kitchen kitchen kitchen kitchen kitchenliving located microwave neighborhood new ' \
        'park parking place privacy private queen room san separate seperate shared space space space ' \
        'street suite time welcome'

#You can take other image for creating mask
mask = np.array(Image.open(requests.get('http://www.clker.com/cliparts/O/i/x/Y/q/P/yellow-house-hi.png', stream=True).raw))


# This function takes in your text and your mask and generates a wordcloud.
def wordcloud_generator(words, mask):
    word_cloud = WordCloud(width=512, height=512, background_color='black', stopwords=STOPWORDS
                           , mask=mask).generate(words)
    #save the wordcloud as .png
    word_cloud.to_file("wordcloud_1.png")
    plt.figure(num='Wordcloud', figsize=(10, 8), facecolor='white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()

# Running the wordcloud function to generate wordcloud
wordcloud_generator(words, mask)
