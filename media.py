class Movie(object):
    """This is a Movie object that contains detail such as title, description,
    image_url and trailer_url"""
    def __init__(self, movie_title, movie_desc, movie_image_url, movie_trailer_url):
        self.title = movie_title
        self.desc = movie_desc
        self.poster_image_url = movie_image_url
        self.trailer_youtube_url = movie_trailer_url
