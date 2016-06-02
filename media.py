import webbrowser
class Movie():
	def __init__(self, title, story_line, poster_image_url, youtube_trailer_url):
		self.title = title
		self.story_line = story_line
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = youtube_trailer_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

