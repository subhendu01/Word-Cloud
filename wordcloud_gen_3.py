import wikipedia
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS# Generate word cloud
import numpy as np
from PIL import Image

# Specify the title of the Wikipedia page
wiki = wikipedia.page('Web scraping')# Extract the plain text content of the page
text = wiki.content# Clean text
text = re.sub(r'==.*?==+', '', text)
text = text.replace('\n', '')
# print(text)

# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(num='Wordcloud',figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud)
    # No axis details
    plt.axis("off");
    plt.show()

# Generate wordcloud
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='salmon',
                      colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(text)
wordcloud.to_file("salmon_wordcloud.png")
plot_cloud(wordcloud)

# Generate wordcloud
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black',
                      colormap='Set2', collocations=False, stopwords = STOPWORDS).generate(text)
wordcloud.to_file("black_wordcloud.png")
plot_cloud(wordcloud)

# Generate wordcloud
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='navy',
                      colormap='rainbow', collocations=False, stopwords = STOPWORDS, mask=None).generate(text)
wordcloud.to_file("navy_wordcloud.png")
plot_cloud(wordcloud)