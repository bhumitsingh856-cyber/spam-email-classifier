import string
import emoji
from nltk.corpus import stopwords
import nltk 
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
def rm_emoji(x):
    return emoji.replace_emoji(x, replace='')   
    
def rm_pn(x):
    return x.translate(str.maketrans('','',string.punctuation))

def rm_num(x):
    txt=""
    for i in x:
        if(not i.isdigit()):
            txt+=i
    return txt

def rm_stop(x):
    arr = word_tokenize(x)
    cleaned=[]
    for i in arr:
        if(not i in stop_words):
            cleaned.append(i)
    return " ".join(cleaned)

def clean_text(x):
    """Chain all cleaning steps in order."""
    x = x.lower()
    x = rm_pn(x)        # Step 1: Remove punctuation
    x = rm_num(x)       # Step 2: Remove numbers
    x = rm_stop(x)      # Step 3: Remove stopwords
    x = rm_emoji(x)     # Step 3: Remove emojies
    return x