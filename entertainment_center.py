import media
import fresh_tomatoes

movies = []

#create Movie instances
#and add the instances to list movies
pianoist = media.Movie('The Legend of 1900', 'a pianoist story', 'http://www.sinemablog.com/wp-content/uploads/2012/09/1900-Efsanesi-Poster1.jpg', 
	'https://www.youtube.com/watch?v=2uf-LDlZMFE')
movies.append(pianoist)


Legends_of_fall = media.Movie('Legends of the Fall', 'Legends of the Fall', 'https://s-media-cache-ak0.pinimg.com/236x/db/15/31/db15318c37a2eaf311957c16e06cc06a.jpg', 
	'https://www.youtube.com/watch?v=JnJoaUzvXc4')
movies.append(Legends_of_fall)

kontiki = media.Movie('Kontiki', 'kontiki', 'https://s-media-cache-ak0.pinimg.com/736x/54/18/8f/54188ff2a0acc6e223da45d5cbd51dc0.jpg', 
	'https://www.youtube.com/watch?v=0VdQUc1C1Fs')
movies.append(kontiki)

Titanic = media.Movie('Titanic', 'a love story', 'https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg', 
	'https://www.youtube.com/watch?v=CHekzSiZjrY')
movies.append(Titanic)

cinema_paradiso = media.Movie('Cinema Paradiso', 'Nuovo Cinema Paradiso', 'https://s-media-cache-ak0.pinimg.com/236x/fc/ce/f6/fccef6791a51aa47bb3fce006a756e62.jpg', 
	'https://www.youtube.com/watch?v=C2-GX0Tltgw')
movies.append(cinema_paradiso)

forrest_gump = media.Movie('Forrest Gump', 'a touch man', 'http://ext.pimg.tw/ilw4e/49aacecf160f7.jpg', 'https://www.youtube.com/watch?v=uPIEn0M8su0')
movies.append(forrest_gump)

#call the function of open_movies_page in module fresh_tomatoes to create the web page of movies
fresh_tomatoes.open_movies_page(movies)




