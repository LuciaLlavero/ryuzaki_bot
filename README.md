# Hi there, I'm RyuzakiBot!

Looking for a free open source chatbot? RyuzakiBot is a simple retrieval-based chatbot made from scratch in Python using NLTK and scikit-learn. Try it out here: [https://ryuzaki-bot.herokuapp.com/](https://ryuzaki-bot.herokuapp.com/) Please notice that website is deployed on a free Heroku server and it would takes some time to load and to answer for the first time.

## Using your own corpus

If you would like to train RyuzakiBot on a different subject, please just change `corpus.txt` file by your own. It is not difficult to create one, each corpus is just a sample of various input statements and their responses for the chatbot to train itself with. In the above example, it will be using the Wikipedia page for [chatbots](https://en.wikipedia.org/wiki/Chatbot) as its corpus.

## API REST

RyuzakiBot uses microframework [Flask](http://flask.pocoo.org/docs/1.0/) and its extension that adds support for quickly building REST APIs: [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/index.html). You can make HTTPS requests to the API here:[https://ryuzaki-bot-api.herokuapp.com/reply.json?q=what%20is%20a%20conversational%20bot?](https://ryuzaki-bot-api.herokuapp.com/reply.json?q=what%20is%20a%20conversational%20bot?)  `q=` will hold query and all GET requests will return a JSON object. 

## Implementation

This chatbot is written in Python3 and mainly uses:

- **NLTK:** natural language processing (NLP) and artificial intelligence library: NLTK, for text pre-processing (removing noise, stop words, stemming and lemmatizing). Please visit [https://www.nltk.org/](https://www.nltk.org/) for more info.
- **scikit-learn:** data mining and data analysis library: scikit-learn. RyuzakiBot takes all last paragraph pre-processed documents, transforms them into numerical vectors with [TF-IDF method](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) and compares cosine from angles formed between all documents and the one from query with [cosine similary numerical method](https://en.wikipedia.org/wiki/Cosine_similarity). Please find all scikit-learn documentation here: [https://www.nltk.org/](https://www.nltk.org/) 

## About the author

My name is Lucía Llavero Company and I'm a Spanish high-school software developer. Feel free to use this code for any purpose. I hope you find it useful!
