df = pd.read_csv('df.csv')

import nltk
# nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

# Step 1: Text normalization
def normalize_text(text):
    return text.lower()

# Step 2: Removal of special characters and punctuation
def remove_special_characters(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Step 3: Tokenization
def tokenize_text(text):
    return word_tokenize(text)

# Step 4: Removal of stop words
def remove_stop_words(tokens):
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]

# Step 5: Lemmatization
def lemmatize_words(tokens):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in tokens]

# Apply the cleaning steps to the 'Summary' column

# df['Summary_clean'] = df['Summary'].apply(lambda x: remove_bangladesh(x) if isinstance(x, str) else '')
df['Summary_clean'] = df['Summary'].apply(lambda x: normalize_text(x) if isinstance(x, str) else '')
df['Summary_clean'] = df['Summary_clean'].apply(lambda x: remove_special_characters(x) if isinstance(x, str) else '')
df['Summary_clean'] = df['Summary_clean'].apply(lambda x: tokenize_text(x) if isinstance(x, str) else '')
# df['Summary_clean'] = df['Summary'].apply(lambda x: remove_stop_words(x) if isinstance(x, str) else '')
# df['Summary_clean'] = df['Summary'].apply(lambda x: lemmatize_words(x) if isinstance(x, str) else '')

dfToCSV = df.to_csv('df.csv')
# Print the cleaned 'Summary' column
print(df['Summary_clean'])


