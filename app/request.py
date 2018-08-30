from app import app
import urllib.request,json
from .models import source

Source = source.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config['NEWS_API_BASE_URL']

def get_articles(source):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_sources = None

        if get_articles_response['sources']:
            article_sources_list = get_articles_response['sources']
            article_sources = process_articles(article_sources_list)


    return article_sources

def process_articles(article_list):
    '''
    Function  that processes the article sources and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article source

    Returns :
        article_sources: A list of article sources object
    '''
    article_sources = []
    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')

        # if poster:
        article_object = Source(id,name)
        article_sources.append(article_object)

    return article_sources