from typing import KeysView
import urllib
import json
import matplotlib.pyplot as plt
import urllib.request
from datetime import datetime
from bs4 import BeautifulSoup
import requests  # to get image from the url
import shutil  # to save it locally in system
import spacy
import yake
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from typing import KeysView
import urllib
import json
import matplotlib.pyplot as plt
import urllib.request
from datetime import datetime
from bs4 import BeautifulSoup
import requests  # to get image from the url
import shutil  # to save it locally in system
import spacy
import yake
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
 
# Opening JSON file
#f = open('twitter.json', encoding="utf8")
 
# returns JSON object as
# a dictionary
#data = json.load(f)
 
# calculate total reactions
# totalEngagement = {}
 
# for i in data:
#     totalEngagement[i['content']] = i['favorites'] + 1.25 * \
#         i['retweets'] + 1.5 * i['replies']
 
# # sort totalEngagement
# sorted_totalEngagement = sorted(
#     totalEngagement.items(), key=lambda kv: kv[1], reverse=True)
# # print(sorted_totalEngagement)
 
# kw_extractor = yake.KeywordExtractor()
 
 
# #firstText = 'Improve your social media using Hootsuite and instagram stories'
# #secondText = 'topics SmartSweets. Media Week'
 
def generate_keywords(text):
    language = "en"
    max_ngram_size = 2
    deduplication_threshold = 0.5
    numOfKeywords = 20
    custom_kw_extractor = yake.KeywordExtractor(
        lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)
    return keywords
 
 
def getTotalScore(keywords, keywords_relevance):
    totalScore = 0
    for i in keywords:
        for j in keywords_relevance:
            if i[0] == j[0]:
                totalScore += j[1]
    return totalScore
 
 
def compare_posts(firstText, secondText, site):
    f = open('./data/{}_keywords_relevance.json'.format(site), encoding="utf8")
    sorted_keywords_relevance = json.load(f)
    f.close()
    return (getTotalScore(generate_keywords(firstText), sorted_keywords_relevance), getTotalScore(generate_keywords(secondText), sorted_keywords_relevance))
 
 
# returns JSON object as
# a dictionary
 
 
# keywords_relevance = {}
 
# for i in sorted_totalEngagement:
#     for j in generate_keywords(i[0]):
#         if j[0] in keywords_relevance:
#             keywords_relevance[j[0]] += i[1]
#         else:
#             keywords_relevance[j[0]] = i[1]
 
 
# # sort values of keywords_relevance
# sorted_keywords_relevance = sorted(
#     keywords_relevance.items(), key=lambda kv: kv[1], reverse=True)
 
# # save the keywords and their relevance score in a json file\
# with open('twitter_keywords_relevance.json', 'w') as outfile:
#     json.dump(sorted_keywords_relevance, outfile)
 
 
# print(generate_keywords(firstText))
# print(generate_keywords(secondText))
 
 
print(compare_posts('Improve your social media using Hootsuite and instagram stories',
      'Social Media Superpower: Knowing the right keywords to search in order find the perfect GIF for your tweet.', 'facebook'))
# nlp = spacy.load("en_core_web_sm")
# text = """spaCy is an open-source software library for advanced natural language processing,
# written in the programming languages Python and Cython. The library is published under the MIT license
# and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion."""
# doc = nlp(text)
# print(doc.ents)
 
# sentence_1 = "This is a good job.Good I will not miss it for anything"
# sentence_2 = "This is not good at all"
 
# # without smooth IDF
# print("Without Smoothing:")
# # define tf-idf
# tf_idf_vec = TfidfVectorizer(use_idf=True,
#                              smooth_idf=False,
#                              ngram_range=(1, 1), stop_words='english')  # to use only  bigrams ngram_range=(2,2)
# # transform
# tf_idf_data = tf_idf_vec.fit_transform([sentence_1, sentence_2])
 
# # create dataframe
# tf_idf_dataframe = pd.DataFrame(
#     tf_idf_data.toarray(), columns=tf_idf_vec.get_feature_names())
# print(tf_idf_dataframe)
# print("\n")
 
# # with smooth
# tf_idf_vec_smooth = TfidfVectorizer(use_idf=True,
#                                     smooth_idf=True,
#                                     ngram_range=(1, 1), stop_words='english')
 
# tf_idf_data_smooth = tf_idf_vec_smooth.fit_transform([sentence_1, sentence_2])
 
# print("With Smoothing:")
# tf_idf_dataframe_smooth = pd.DataFrame(
#     tf_idf_data_smooth.toarray(), columns=tf_idf_vec_smooth.get_feature_names())
# print(tf_idf_dataframe_smooth)
 
# doc = """
#          Supervised learning is the machine learning task of
#          learning a function that maps an input to an output based
#          on example input-output pairs.[1] It infers a function
#          from labeled training data consisting of a set of
#          training examples.[2] In supervised learning, each
#          example is a pair consisting of an input object
#          (typically a vector) and a desired output value (also
#          called the supervisory signal). A supervised learning
#          algorithm analyzes the training data and produces an
#          inferred function, which can be used for mapping new
#          examples. An optimal scenario will allow for the algorithm
#          to correctly determine the class labels for unseen
#          instances. This requires the learning algorithm to
#          generalize from the training data to unseen situations
#          in a 'reasonable' way (see inductive bias).
#       """
 
# from sklearn.feature_extraction.text import CountVectorizer
 
# n_gram_range = (1, 1)
# stop_words = "english"
 
# # Extract candidate words/phrases
# count = CountVectorizer(ngram_range=n_gram_range, stop_words=stop_words).fit([doc])
# candidates = count.get_feature_names()
 
# from sentence_transformers import SentenceTransformer
 
# model = SentenceTransformer('distilbert-base-nli-mean-tokens')
# doc_embedding = model.encode([doc])
# candidate_embeddings = model.encode(candidates)