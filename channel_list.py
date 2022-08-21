from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

import create_guild
from check_messages import *
from utils import Guild

member = None
listen = None


def on_press(ins, label):
    global listen
    listen = get_messages(ins.__getattribute__("guild").id, label)


def close():
    stop()


def channel_list(member_1, label):
    global root, btn, g_label, member
    member = member_1
    g_label = label
    layout = GridLayout(cols=1, size_hint_y=None)
    layout.bind(minimum_height=layout.setter('height'))
    for i in member.guilds:
        if i.isalpha():
            continue
        guild = Guild(i)
        btn = Button(text=str(guild), size_hint_y=None, height=40)
        btn.__setattr__("guild", guild)
        btn.bind(on_press=lambda ins: on_press(ins, label))
        layout.add_widget(btn)
    btn = Button(text="+", size_hint_y=None, height=40)
    btn.bind(on_press=lambda x: create_guild.create(label, member))
    layout.add_widget(btn)
    root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * .99))
    root.add_widget(layout)
    return root


def reset():
    global root, btn, g_label, member
    layout: GridLayout = root.children[0]
    root.remove_widget(layout)
    layout.remove_widget(btn)
    guild = Guild(list(member.guilds.keys())[-1])
    btn = Button(text=str(guild), size_hint_y=None, height=40)
    btn.__setattr__("guild", guild)
    layout.add_widget(btn)
    btn = Button(text="+", size_hint_y=None, height=40)
    btn.bind(on_press=lambda x: create_guild.create(g_label, member))
    layout.add_widget(btn)
    root.add_widget(layout)
