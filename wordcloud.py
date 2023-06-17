

##### Word cloud ####

import re
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Extract the news articles column from the DataFrame
news_articles = df['Summary_clean'].tolist()
word_to_remove = 'bangladesh'
news_articles = [word for word in news_articles if word != word_to_remove] 
word_to_remove = 'said'
news_articles = [word for word in news_articles if word != word_to_remove] 
word_to_remove = 's'
news_articles = [word for word in news_articles if word != word_to_remove] 
word_to_remove = 'according'
news_articles = [word for word in news_articles if word != word_to_remove] 
word_to_remove = 'may'
news_articles = [word for word in news_articles if word != word_to_remove] 
word_to_remove = 'the'
news_articles = [word for word in news_articles if word != word_to_remove] 
word_to_remove = 'will'
news_articles = [word for word in news_articles if word != word_to_remove] 



# # Flatten the list of lists into a single list
# flattened_articles = [item for sublist in news_articles for item in sublist]

# Join the strings
# Concatenate the news articles into a single string
text = ' '.join(news_articles)

from nltk.corpus import stopwords

# Tokenize the text into individual words
word_tokens = word_tokenize(text)

# Get the list of stopwords
stop_words = set(stopwords.words("english"))

# Remove stopwords from the list of words
filtered_words = [word for word in word_tokens if word.lower() not in stop_words]

# Join the filtered words back into a single string
filtered_text = ' '.join(filtered_words)

words_to_remove = ['may', 'due', 'bangladesh', 'said', 'among', 'one', 'us', 'will', 'went', 'now',
                    'later', 'event', 'even', 'every', 'becae', 'told', 'acced', 'many', 'hoe']
# Remove words from the text
for word in words_to_remove:
    filtered_text = filtered_text.replace(word, '')


# Generate the word cloud
wordcloud = WordCloud(background_color='white').generate(filtered_text)

top_words = dict(list(wordcloud.words_.items())[:75])

# Create a new WordCloud object with the top words
# get colourmap from here: https://www.kaggle.com/code/niteshhalai/wordcloud-colormap
wordcloud_top = WordCloud(background_color='white', width=1000, height=600, colormap="brg").fit_words(top_words)



# Set the plot parameters
plt.figure(dpi = 1200)

# Plot the top top words
plt.imshow(wordcloud_top, interpolation='bilinear')
plt.axis('off')

# Save the word cloud as a high-resolution image
#plt.savefig('wordcloud.pdf', format='pdf', dpi = 1200)
plt.savefig('wordcloud.png', format='png', dpi = 1200)

# plt.show()

