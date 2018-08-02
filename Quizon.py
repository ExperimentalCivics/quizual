
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import time
import random
import csv


class StartScreen(Screen):
    pass

class QuizScreen(Screen):
    with open('quiz.csv', newline='') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
         for row in spamreader:
             if row[0][0] == '#':
                 print('commented out')
             else:
                 print(', '.join(row))

class RootWidget(BoxLayout):
    pass

class ColourScreen(Screen):
    colour = ListProperty([1., 0., 0., 1.])

class MyScreenManager(ScreenManager):
    def new_colour_screen(self):
        name = str(time.time())
        s = ColourScreen(name=name,
                         colour=[random.random() for _ in range(3)] + [1])
        self.add_widget(s)
        self.current = name

root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import hex kivy.utils.get_color_from_hex
MyScreenManager:
    transition: FadeTransition()
    StartScreen:
    QuizScreen:

<StartScreen>:
    name: 'start'
    BoxLayout:
        canvas.before:
            Color:
                rgba: hex('#0000b1ff')
            Rectangle:
                pos: self.pos
                size: self.size
        orientation: 'vertical'
        Label:
            text: 'Welcome to the Quiz Challenge!'
            color: hex('#f8ee3fff')
            font_size: 30
        Image:
            source: 'images/redbull_challenge.png'
            allow_stretch: True
            keep_ratio: True
        BoxLayout:
            Button:
                background_normal: ''
                background_color: hex('#0000b1ff')
                #color: hex('#cc2729ff')
                color: hex('#f8ee3fff')
                text: 'start a quiz'
                font_size: 30
                on_release: app.root.current = 'quiz'

<QuizScreen>:
    name: 'quiz'
    BoxLayout:
        canvas.before:
            Color:
                rgba: hex('#0000b1ff')
            Rectangle:
                pos: self.pos
                size: self.size
        orientation: 'vertical'
        Label:
            text: 'What does Red Bull do?'
            font_size: 30
        BoxLayout:
            canvas.before:
                Color:
                    rgba: hex('#0000b1ff')
                Rectangle:
                    pos: self.pos
                    size: self.size
            orientation: 'vertical'
            padding: 10
            spacing: 10
            Button:
                background_normal: ''
                border: (22,22,22,22)
                background_color: hex('#f8ee3fff')
                color: hex('#cc2729ff')
                text: 'It gives you feet!'
                font_size: 30
                on_release: app.root.current = 'start'
            Button:
                border: (22,22,22,22)
                background_normal: ''
                background_color: hex('#f8ee3fff')
                color: hex('#cc2729ff')
                text: 'It gives you wings!'
                font_size: 30
                on_release: app.root.new_colour_screen()

<ColourScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'colour {:.2},{:.2},{:.2} screen'.format(*root.colour[:3])
            font_size: 30
        Widget:
            canvas:
                Color:
                    rgba: root.colour
                Ellipse:
                    pos: self.pos
                    size: self.size
        BoxLayout:
            Button:
                text: 'goto start screen'
                font_size: 30
                on_release: app.root.current = 'start'
            Button:
                text: 'get random colour screen'
                font_size: 30
                on_release: app.root.new_colour_screen()
''')

class QuizonApp(App):
    def __init__(self, **kwargs):
        super(QuizonApp, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        app= App.get_running_app()
        if app.root.current == 'start':
            if keycode[1] == '1':
                app.root.current = 'quiz'
            elif keycode[1] == '2':
                app.root.current = 'quiz'
        elif app.root.current == 'quiz':
            if keycode[1] == '1':
                app.root.current = 'start'
            elif keycode[1] == '2':
                app.root.current = 'start'
        return True

    def build(self):
        return root_widget

QuizonApp().run()
