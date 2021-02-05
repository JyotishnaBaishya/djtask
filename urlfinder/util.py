import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter
from nltk.corpus import stopwords

def start(url):
    source_code = requests.get(url).text
    soup= BeautifulSoup(source_code, 'html.parser')
    text= soup.get_text()
    words= text.lower().split()
    stop_words= set(stopwords.words('english'))
    filtered_words= [w for w in words if not w in stop_words]
    final_filtered= []
    for w in filtered_words:
        symbols= '~`!@#$%^&*()_-–+={[}]|\;:"<>?/., '
        for i in range(0, len(symbols)):
            w=w.replace(symbols[i], '')
        if len(w)>0:
            final_filtered.append(w)
    count= Counter(final_filtered)
    ans= dict(count.most_common(10))
    return ans
