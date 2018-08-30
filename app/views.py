from flask import render_template
from app import app
from .request import get_articles

# Views

# index - sources route that will have the article sources list

@app.route('/')
def index():

    '''
    View root page function that returns the index page which shows the 
    '''

    title = 'The News API .'
    # Getting article sources
    article_sources = get_articles('source')
    print(article_sources)

    return render_template('index.html', title = title, source = article_sources)

# View article route that will have the article lists in each source

@app.route('/articles')
def articles(article_id):

    '''
    View article sources page function that returns the list of articles from that source
    '''
    return render_template('articles.html',id = article_id)

# View individual article, its posting time and author.

@app.route('/article')
def article(article_id):

    '''
    View article function that returns the article and author
    '''
    return render_template('article.html',id = article_id)