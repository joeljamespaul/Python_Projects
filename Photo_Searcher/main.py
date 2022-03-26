from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def search_image(self):
        # Get text input from the user
        query = self.manager.current_screen.ids.text_input.text
        # Get wikipedia page and get the first image link from list of image links
        page = wikipedia.page(query)
        image_link = page.images[0]
        # Download the image using requests.get() and
        # write the content(binary data) of the request object to the empty jpg file
        # Note: write as wb as the data is of binary form
        # added header to avoud 403 error from get requestss
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/99.0.4844.82 Safari/537.36'}
        req = requests.get(url=image_link, headers=headers)
        with open('files/image.jpg', 'wb') as file:
            file.write(req.content)
        # Set the image in the image widget
        self.manager.current_screen.ids.img.source = 'files/image.jpg'


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
