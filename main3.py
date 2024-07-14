import os
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from transformers import pipeline


os.environ['HUGGINGFACE_API_KEY'] = '#ask for the API key'


generator = pipeline('text-generation', model='gpt2')

class JarvisApp(App):

    def build(self):
        Window.clearcolor = (10/255, 10/255, 10/255, 1)  # Background color

        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.title_label = Label(
            text='JARVIS: Your AI Assistant',
            font_size='32sp',
            color=(1, 1, 1, 1),
            bold=True,
            size_hint_y=None,
            height=50,
            halign='center',
            valign='middle'
        )
        self.title_label.bind(size=self.title_label.setter('text_size'))
        self.layout.add_widget(self.title_label)

        self.text_input = TextInput(
            hint_text='Ask me anything...',
            multiline=True,
            font_size='20sp',
            size_hint_y=None,
            height=150,
            background_color=(26/255, 26/255, 26/255, 1),
            foreground_color=(1, 1, 1, 1),
            padding=(10, 10),
            cursor_color=(0, 1, 1, 1),
            hint_text_color=(1, 1, 1, 0.5)
        )
        self.layout.add_widget(self.text_input)

        self.button = Button(
            text='Ask',
            font_size='20sp',
            size_hint_y=None,
            height=50,
            background_normal='',
            background_color=(0, 204/255, 102/255, 1)
        )
        self.button.bind(on_press=self.on_button_press)
        self.layout.add_widget(self.button)

        self.response_title_label = Label(
            text='Response:',
            font_size='24sp',
            color=(1, 1, 1, 1),
            bold=True,
            size_hint_y=None,
            height=50,
            halign='center',
            valign='middle'
        )
        self.response_title_label.bind(size=self.response_title_label.setter('text_size'))
        self.layout.add_widget(self.response_title_label)

        self.response_label = Label(
            font_size='20sp',
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=150,
            halign='left',
            valign='middle',
            text_size=(600, None)
        )
        self.response_label.bind(size=self.response_label.setter('text_size'))
        self.layout.add_widget(self.response_label)

        return self.layout

    def on_button_press(self, instance):
        user_input = self.text_input.text
        # Generate a response using Hugging Face's GPT-2 model
        response = generator(user_input, max_length=100, num_return_sequences=1)
        bot_response = response[0]['generated_text']
        self.response_label.text = bot_response

if __name__ == '__main__':
    JarvisApp().run()
