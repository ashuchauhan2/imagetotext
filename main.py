from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import os
import pytesseract

Builder.load_file('main.kv')

class MyWidget(BoxLayout):
    def open(self, path, filename):
        with open(os.path.join(path, filename[0])) as f:
            print(f.read())

    def selected(self, filename):
        self.ids.textBox.text = pytesseract.image_to_string(filename[0])


class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()