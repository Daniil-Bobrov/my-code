from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

import channel_list
import firebase
import config
from utils import *


def create_guild(name, layout, member):
    config.reset()
    member.guilds[str(firebase.create_guild(name, config.id))] = name
    layout.clear_widgets()
    channel_list.reset()


def create(layout, member):
    layout.clear_widgets()
    label = Label(
        text="Введите название чата:",
        pos_hint={'x': .35, 'y': .6},
        size_hint=(.3, .1),
    )
    layout.add_widget(label)

    name = TextInput(
        multiline=False,
        pos_hint={'x': .1, 'y': .5},
        size_hint=(.8, .1),
    )
    layout.add_widget(name)

    button = Button(
        text="Создать чат",
        pos_hint={'x': 0, 'y': 0},
        size_hint=(1, .1),
    )
    button.bind(on_press=lambda x: create_guild(name.text, layout, member))
    layout.add_widget(button)
