# WordCloud

###### word_cloud_gen_1.py

##### Here we generate a word cloud in python in any shape that we desire with. We will go through an example of how to create a simple word cloud in the custom shape of a house.


###### word_cloud_gen_2.py
##### Simplest way to generate wordcloud

###### wordcloud_gen_3.py
   1. Installed all the required packages
   2. Extract the plain text content of the page
   3. Define a function to plot word cloud
   4. Generate diff. wordcloud
   5. Save them in .png format

##### Here we can use mask for good visualization. In the word_cloud_gen_1.py I have used a online pic for mask, you can use your local image for creating mask.

## WordCloud function:
   1. **width/height:** You can change the word cloud dimension to your preferred width and height with these.
   2. **random_state:** If you don’t this set this to a number of your choice, you are likely to get a slightly different word cloud every time you run the same script on the same input data. By setting this parameter, you ensure reproducibility of the exact same word cloud. You could play around with random numbers until you find the one that results in the word cloud you like.
   3. **background_colour:** ‘white’ and ‘black’ are common background colours. If you would like to explore more colours, this may come in handy. Please note that some colours may not work. Hope you will find something you fancy. 
   4. **colormap:** With this argument, you can set up the colour theme that the words are displayed in. There are many beautiful Matplotlib colormaps to choose from. Some of my favourites are ‘rainbow’, ‘seismic’, ‘Pastel1’ and Pastel2’.
   5. **collocations:** Set this to False to ensure that the word cloud doesn’t appear as if it contains any duplicate words. Otherwise, you may see ‘web’, ‘scraping’ and ‘web scraping’ as a collocation in the word cloud, giving an impression that words have been duplicated.
   6. **stopwords:** Stopwords are common words which provide little to no value to the meaning of the text. ‘We’, ‘are’ and ‘the’ are examples of stopwords. I have explained stopwords in more detail here (scroll to ‘STEP3. REMOVE STOPWORDS’ section). Here, we used STOPWORDS from the wordcloud package. To see the set of stopwords, use print(STOPWORDS) and to add custom stopwords to this set, use this template STOPWORDS.update(['word1', 'word2']), replacing word1 and word2 with your custom stopwords before generating a word cloud.
   
