# coding: utf-8

import constants
from flask import Flask, request
from flask_restful import Resource, Api
import nltk
import random
import simplejson
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import sys
import warnings

def get_formalities_reply(formality) :
    if any(remove_punctuation_marks(formality).lower() in remove_punctuation_marks(greet).lower() for greet in constants.GREETING_INPUTS) :
        return random.choice(constants.GREETING_REPLIES)
    elif any(remove_punctuation_marks(formality).lower() in remove_punctuation_marks(thanks).lower() for thanks in constants.THANKS_INPUTS) :
        return random.choice(constants.THANKS_REPLIES)

def get_lemmatized_tokens(text):
    normalized_tokens = nltk.word_tokenize(remove_punctuation_marks(text.lower()))
    return [nltk.stem.WordNetLemmatizer().lemmatize(normalized_token) for normalized_token in normalized_tokens]

def get_query_reply(query) :    
    documents.append(query)
    tfidf_results = TfidfVectorizer(tokenizer = get_lemmatized_tokens, stop_words = 'english').fit_transform(documents)
    cosine_similarity_results = cosine_similarity(tfidf_results[-1], tfidf_results).flatten()
    # The last will be 1.0 because it is the Cosine Similarity between the first document and itself
    best_index = cosine_similarity_results.argsort()[-2]
    documents.remove(query)
    if cosine_similarity_results[best_index] == 0 :
        return "I am sorry! I don't understand you..."
    else :
        return documents[best_index]

def remove_punctuation_marks(text) :
    punctuation_marks = dict((ord(punctuation_mark), None) for punctuation_mark in string.punctuation)
    return text.translate(punctuation_marks)

class Reply(Resource) :
    def get(self) :
        if request.args.get('q') :
            formality_reply = get_formalities_reply(request.args.get('q'))
            if  formality_reply :
                return simplejson.dumps([{'reply': formality_reply}])
            else :
                return simplejson.dumps([{'reply': get_query_reply(request.args.get('q'))}])
        else :
            return simplejson.dumps([{'error': 'query is empty'}])

if __name__ == "__main__" :
    corpus = open('corpus.txt', 'r' , errors = 'ignore').read().lower()
    documents = nltk.sent_tokenize(corpus)

    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Reply, '/reply.json')
    app.run()
