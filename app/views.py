from flask import render_template
from app import app
from .request import get_sources, get_article

# Views

# index - sources route that will have the article sources list

@app.route('/')
def index():

    '''
    View root page function that returns the index page which shows the 
    '''

    title = 'The News API .'
    # Getting article sources
    article_sources = get_sources('source')
    print(article_sources)

    return render_template('index.html', title = title, source = article_sources)

# View article route that will have the article lists in each source

@app.route('/articles/<id>')
def articles(id):

    '''
    View article sources page function that returns the list of articles from that source
    '''
    article = get_article(id)
    # article_title = get_article(id)
    return render_template('articles.html',id = article)

# View individual article, its posting time and author.

@app.route('/article')
def article(article_id):

    '''
    View article function that returns the article and author
    '''
    return render_template('article.html',id = article_id)