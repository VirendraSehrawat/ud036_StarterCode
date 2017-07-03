import media
import fresh_tomatoes

def prepare_data():
    '''
    The movie data store is hard coded here for now. This method returns list of movies
    '''
    
    sholay = media.Movie("Sholay",
                         "Revenge goes a long way",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/5/52/Sholay-poster.jpg/220px-Sholay-poster.jpg",
                         "https://www.youtube.com/watch?v=EwT6RdS-Nac")
    gabbar = media.Movie("Gabbar is back",
                         "Gabbar is back",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Gabbar_is_back_first_look.jpg/220px-Gabbar_is_back_first_look.jpg" , 
                         "https://www.youtube.com/watch?v=T95zFC4Z2pY")
    bahubali = media.Movie("Bahubali",
                           "One with strong arms",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/Baahubali_poster.jpg/220px-Baahubali_poster.jpg",
                           "https://www.youtube.com/watch?v=sOEg_YZQsTI")
    dangal = media.Movie("Dangal",
                         "Girls have equal power",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/9/99/Dangal_Poster.jpg/220px-Dangal_Poster.jpg",
                         "https://www.youtube.com/watch?v=x_7YlGv9u1g")
    mrs_doubtfire = media.Movie("Mrs Doubtfire",
                                "Mrs Doubtfire",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/5/5a/Mrs_Doubtfire.jpg/220px-Mrs_Doubtfire.jpg" ,
                                "https://www.youtube.com/watch?v=IYyNDWjIivo")
    munna_bhai = media.Movie("Munna Bahi M.B.B.S",
                             "Munna Bahi M.B.B.S", 
                             "https://upload.wikimedia.org/wikipedia/en/thumb/1/19/Munna_Bhai_M.B.B.S.%2C_2003_Hindi_film_poster.jpg/220px-Munna_Bhai_M.B.B.S.%2C_2003_Hindi_film_poster.jpg",
                             "https://www.youtube.com/watch?v=amwbqk8iDwA")
    toy_story = media.Movie("Toy Story", 
                            "Watch the movie",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=azyK_k52R1w")
    avatar = media.Movie("Avatar", 
                         "Allainz with aleins",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", 
                         "https://www.youtube.com/watch?v=5PSNL1qE6VY")
    school_of_rock = media.Movie("School of Rock", 
                                 "This is all about rock school",
                                 "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                                 "https://www.youtube.com/watch?v=oP7kExN8LFA")
    ratatouille = media.Movie("Ratatouille",
                              "How a mouse becomes best cook in town",
                              "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                              "https://www.youtube.com/watch?v=3YG4h5GbTqU")
    midnight_in_paris = media.Movie("Midnight in paris", 
                                    "Midnight in paris",
                                    "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/220px-Midnight_in_Paris_Poster.jpg",
                                    "https://www.youtube.com/watch?v=BYRWfS2s2v4")
    hunger_games = media.Movie("Hunger Games", 
                               "Hunger Games Description",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg",
                               "https://www.youtube.com/watch?v=4S9a5V9ODuY")
   
    # making a list of all the movie objects
    data_list = [munna_bhai, gabbar, bahubali, dangal, sholay, mrs_doubtfire, toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

    return data_list

def open_webapp():
    '''
    It calls fresh_tomatoes with list of Movie objects
    '''
    fresh_tomatoes.open_movies_page(prepare_data());

#invoking open_webapp 
open_webapp()