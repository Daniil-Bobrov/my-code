from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

import firebase
from firebase import db


class Member:
    def __init__(self, id):
        member = firebase.get_member(id)
        self.name = member["name"]
        self.id = member["id"]
        self.guilds = member["guilds"]

    def __str__(self):
        return self.name


class Guild:
    def __init__(self, id):
        guild = firebase.get_guild(id)
        # print(guild)
        self.name = guild["name"]
        self.id = guild["id"]
        self.members = guild["members"]
        self.messages = guild["messages"]
        self.owner_id = guild["owner_id"]

    def __str__(self):
        return self.name


class MyLabel(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1, .5, .5, 1)
            Rectangle(pos=self.pos, size=self.size)


class MainScreen(FloatLayout):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(.5, 1, .5, 1)
            Rectangle(pos=self.pos, size=self.size)


class MainLayout(FloatLayout):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(.5, .5, 1, 1)
            Rectangle(pos=self.pos, size=self.size)


class ChannelList(FloatLayout):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(.4, .4, 1, 1)
            Rectangle(pos=self.pos, size=self.size)


class Message:
    def __init__(self, guild_id, id):
        message = db.reference(f"/guilds/{guild_id}/messages").get()[str(id)]
        self.author = message['author']
        self.author_id = message['author_id']
        self.text = message['text']
        self.time = message['time']

    def __str__(self):
        return self.text
