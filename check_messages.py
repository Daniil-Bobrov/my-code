import firebase_admin
from firebase_admin import db
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from time import sleep
from kivy.core.window import Window

guild = None
f = False


def callback(scroll_layout, guild_id):
    messages = db.reference(f"/guilds/{guild_id}/messages").get()
    layout = GridLayout(cols=1, size_hint_y=None)
    layout.bind(minimum_height=layout.setter('height'))
    for message in messages:
        message = Message(message["id"], message["text"], message["author"], message["time"])
        btn = Label(text=f"[color=000000]\n{str(message)}[/color]",
                    size_hint=(Window.width*.9, None),
                    pos_hint={"x": 0, "y": 0},
                    halign="right",
                    text_size=(Window.width*.9, 40),
                    # text_size=(290, 40),
                    height=100,
                    markup=True)
        layout.add_widget(btn)
    if len(messages) * 100 < Window.height*.9:
        scroll_layout.height = len(messages)*100
    else:
        scroll_layout.height = Window.height * .9
    scroll_layout.clear_widgets()
    scroll_layout.add_widget(layout)


def func(layout, guild_id):
    return


class Message:
    def __init__(self, id, text, author, time):
        self.id = id
        self.text = text
        self.author = author
        self.time = time

    def __str__(self):
        return str(self.text)


def get_messages(guild_id, layout):
    global scroll, listen
    f = True
    guild = guild_id
    scroll_layout = ScrollView(size_hint=(1, None), size=(Window.width*.9, Window.height * .9))

    layout.clear_widgets()
    callback(scroll_layout, guild_id)
    scroll = scroll_layout
    scroll.pos_hint = {"x": 0, "y": .1}
    # scroll_layout.pos = (Window.height*.1, Window.width*.1)
    layout.add_widget(scroll_layout)
    low_bar = BoxLayout(orientation="horizontal", size_hint=(1, .1), pos_hint={"x": 0, "y": 0})
    low_bar.add_widget(TextInput(size_hint_x=.7))
    low_bar.add_widget(Button(text="отправить", size_hint_x=.3))
    layout.add_widget(low_bar)
    listen = db.reference(f"/guilds/{guild}/messages").listen(lambda event: callback(scroll_layout, guild_id))
    # db.reference(f"/guilds/{guild}/messages").listen(lambda event: callback(scroll_layout, guild_id))
    # ref =
    # while  f:
    #     pass
    # ref
    return listen


def stop():
    global listen
    listen.close()
# ref = db.reference(f"/guilds/1/messages")
scroll = ScrollView(size_hint=(1, None), size=(Window.width*.9, Window.height * .9))
# while f:
#     pass
# ref.listen(lambda event: callback(scroll, guild))
