from __future__ import print_function
from nltk.corpus import stopwords
import re
import argparse
import string
from gensim import corpora
import gensim
from nltk.stem.wordnet import WordNetLemmatizer
import nltk
nltk.download('stopwords')
 
regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    # domain...
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
 
 
def generate_hashtags(document_path, image_text):
 
    # append text to document
    with open(document_path, 'a') as f:
        f.write(' ')
        f.write(image_text)
 
    stop = set(stopwords.words("english"))
    exclude = set(string.punctuation)
    lemma = WordNetLemmatizer()
    path = document_path
 
    text = ''
 
    if(re.match(regex, path) != None):
        import bs4
        import requests
 
        print('[Url found]')
 
        html = bs4.BeautifulSoup(requests.get(path).text, "html.parser")
 
        data = html.find_all(text=True)
 
        def visible(element):
            if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
                return False
            elif re.match('<!--.*-->', str(element.encode('utf-8'))):
                return False
            return True
 
        results = filter(visible, data)
        text = u" ".join(t.strip() for t in results)
    else:
        text = open(path).read()
 
    doc_complete = text.split('\n')
 
    def clean(doc):
        stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
        punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
        normalized = " ".join(lemma.lemmatize(word)
                              for word in punc_free.split())
        return normalized
 
    doc_clean = [clean(doc).split() for doc in doc_complete]
    dictionary = corpora.Dictionary(doc_clean)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
    Lda = gensim.models.ldamodel.LdaModel
    ldamodel = Lda(doc_term_matrix, num_topics=4,
                   id2word=dictionary, passes=50)
    topic = ldamodel.print_topics(num_topics=5, num_words=5)
 
    hashtags = []
    for t in topic:
        for h in t[1].split('+'):
            hashtags.append('#'+h[h.find('"')+1:h.rfind('"')])
 
    # print("HashTags: ")
    return list(set(hashtags))
 