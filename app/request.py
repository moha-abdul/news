from app import app
import urllib.request,json
from .models import source

Source = source.Source

# Getting api key
api_key = app.config['MOVIE_API_KEY']

# Getting the movie base url
base_url = app.config["MOVIE_API_BASE_URL"]

def get_articles(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(sources,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['results']:
            article_results_list = get_articles_response['results']
            article_results = process_results(article_results_list)


    return article_results