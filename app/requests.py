# from app import app
import urllib.request,json
from .models import Source,Articles

# Getting api key
api_key = None
# Getting the sources base url
source_base_url = None
# Getting the articles base url
article_base_url = None

def configure_request(app):
    global api_key,source_base_url,article_base_url
    # Getting api key
    # api_key = app.config['NEWS_API_KEY']
    api_key = 'a4da06458ea544b4b6838279d94c1a9b'

    # Getting the sources base url
    # source_base_url = app.config['SOURCES_API_BASE_URL']
    source_base_url = 'https://newsapi.org/v2/sources?&apiKey={}'

    # Getting the articles base url
    # article_base_url = app.config['ARTICLE_API_BASE_URL']
    article_base_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=a4da06458ea544b4b6838279d94c1a9b'



def get_sources(source):
    '''
    Function that gets the json response to our url request for the news sources
    '''
    get_sources_url = source_base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        ''' Article sources object '''
        article_sources = None

        if get_sources_response['sources']:
            article_sources_list = get_sources_response['sources']
            article_sources = process_sources(article_sources_list)


    return article_sources

def process_sources(source_list):
    '''
    Function  that processes the article sources and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain article source

    Returns :
        article_sources: A list of article sources object
    '''
    article_sources = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')

        source_object = Source(id,name)
        article_sources.append(source_object)

    return article_sources

def get_article(id):
    '''
    Function that gets the json response to our url request for the news articles
    '''
    get_article_details_url = article_base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        '''
        Articles object
        '''

        article_object = None
        if article_details_response['articles']:
            article_lib = article_details_response['articles']
            article_object = process_articles(article_lib)

    return article_object

def process_articles(articles_list):
    '''
    Function  that processes the article titles and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article titles

    Returns :
        article_titles: A list of news sources objects
    '''
    article_object = []
    for article_item in articles_list:
        id = article_item.get('id')
        title = article_item.get('title')
        description = article_item.get('description')
        urlToImage = article_item.get('urlToImage')
        url = article_item.get('url')
        author = article_item.get('author')
        publishedAt = article_item.get('publishedAt')


        article_list = Articles(id, title, description, urlToImage, url, author, publishedAt)
        article_object.append(article_list)

    return article_object