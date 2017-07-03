# ud036_StarterCode
Source code for a Movie Trailer website.

# Test Project

Follow these steps to build the project

* Install python on your machine. 
* On Terminal or Command prompt navigate to project folder.
* Run command ** python entertainment_center.py ** 

It will open web page on your browser.

## Add Movies to list

The movies are hard coded in function **prepare_data**. In order to add new movie to list add following code
```
bahubali = media.Movie("Bahubali",
                       "One with strong arms",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/Baahubali_poster.jpg/220px-Baahubali_poster.jpg",
                       "https://www.youtube.com/watch?v=sOEg_YZQsTI")

```
Now add movie object to data list as follow
```
data_list = [munna_bhai, gabbar, bahubali, dangal, sholay, mrs_doubtfire, toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
```