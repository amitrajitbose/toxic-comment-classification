import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
stopwords_en = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
def clean_text(text,remove_stopwords=True):
    # -- Converting to lower case
    text = text.lower()
    
    # replacing english abbreviations with full forms
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r"\'scuse", " excuse ", text)
    text = re.sub('\W', ' ', text)
    text = re.sub('\s+', ' ', text)
    
    if(remove_stopwords):
        # -- Lemmatization and segmentation
        filtered_sent = []
        sent = nltk.word_tokenize(text) #word tokenizing
        for i in sent:
            # -- Removing stopwords
            if i not in stopwords_en:
                filtered_sent.append(lemmatizer.lemmatize(i))
        text = ','.join(filtered_sent)
    
    # -- Removing numbers
    retokenizer1 = RegexpTokenizer(r'\D+') #remove numerical values
    text = ','.join(retokenizer1.tokenize(text))
    
    # -- Removing punctuations
    retokenizer2 = RegexpTokenizer(r'\w+') #remove numerical values
    text = ' '.join(retokenizer2.tokenize(text))
    
    """
    print(text)
    # -- Removing non-English words
    sent = text.split(',')
    english_word = []
    for w in sent:
        if(len(w)>2) and detect(w)=='en':
            #this is an english word
            english_word.append(w)
            print(w)
    text = ' '.join(english_word)
    #print(english_word)
    """
    
    return text