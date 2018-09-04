from flask import render_template, request
from . import main
from ..requests import get_sources, get_article

# Views

# index - sources route that will have the article sources list

@main.route('/')
def index():

    '''
    View root page function that returns the index page which shows the article sources
    '''

    title = 'The News API'

    # Getting article sources
    article_sources = get_sources('source')
    print(article_sources)
    '''
    renders index.html template
     '''
    return render_template('index.html', title = title, source = article_sources)

# View article route that will have the article lists in each source, an image from the site, the author and the time posted

@main.route('/articles/<id>')
def articles(id):

    '''
    View article sources page function that returns the list of articles from that source, with image, author and description
    '''
    article = get_article(id)
    # article_author = get_article('author')


    return render_template('articles.html', id = article)
