class Source:
    '''
    Source class to define Source Objects
    '''
    def __init__(self,id,name):
        self.id =id
        self.name = name
        
class Articles:
    '''
    Source class to define Articles Objects
    '''
    def __init__(self, id, title, description, urlToImage, url, author, publishedAt):
        self.id =id
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.author = author
        self.publishedAt = publishedAt