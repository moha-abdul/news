from app import app
import urllib.request,json
from .models import source,articles

Source = source.Source
Articles = articles.Articles

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news sources base url
source_base_url = app.config['SOURCES_API_BASE_URL']
article_base_url = app.config['ARTICLE_API_BASE_URL']
# headlines_base_url = app.config['HEADLINES_API_BASE_URL']

def get_sources(source):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = source_base_url.format(source,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

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
    get_article_details_url = article_base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

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
        article_titles: A list of movie objects
    '''
    article_object = []
    for article_item in articles_list:
        id = article_item.get('id')
        title = article_item.get('title')
        overview = article_item.get('description')
        urlToImage = article_item.get('urlToImage')

        article_list = Articles(id,title,overview,urlToImage)
        article_object.append(article_list)

    return article_object