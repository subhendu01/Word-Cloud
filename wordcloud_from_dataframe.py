from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt

words = 'bed access guest guest apartment area area bathroom bed bed bed bed bed bedroom block coffee coffee coffee coffee entrance entry francisco free garden guest home house kettle kettle kitchen kitchen kitchen kitchen kitchen kitchenliving located microwave neighborhood new park parking place privacy private queen room san separate seperate shared space space space street suite time welcome'

def generate_wordcloud(words_tem):
    word_cloud = WordCloud(width = 512, height = 512, background_color='white', stopwords= None, max_words=20).generate(words_tem)
    plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()

tfidf = TfidfVectorizer(words, lowercase = False)
tfs = tfidf.fit_transform([words])

feature_names = tfidf.get_feature_names()

df = pd.DataFrame(tfs.T.toarray(), index=feature_names, columns= ['weight'])
df = df.sort_values(by = 'weight', ascending = False)
word_lists = df.index.values
unique_str = ' '.join(word_lists)
print(df[0:20])
generate_wordcloud(unique_str)
