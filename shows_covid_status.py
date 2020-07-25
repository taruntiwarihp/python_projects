import imdb 
   
# creating instance of IMDb 
ia = imdb.IMDb() 
   
# getting top 250 movies 
search = ia.get_top250_movies() 
  
# printing only first 10 movies title 
for i in range(10): 
    print(search[i]['title']) 