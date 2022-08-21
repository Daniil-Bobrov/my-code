from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

import channel_list
from utils import *


class StartScreenApp(App):
    layout = None

    def build(self):
        import config
        if config.id == "":
            import registration
        config.reset()
        member = Member(config.id)
        Window.size = (312, 672)  # 260 560

        layout = MainScreen()
        label = ChannelList()
        # label2 = MainLayout(pos_hint={'x': .1, 'y': 0}, size_hint=(.9, 1))
        label2 = MainLayout(pos_hint={'x': .1, 'y': 0}, size_hint=(.9, 1))
        label.pos = (0, 0)
        label.size_hint = (.1, 1)
        label.add_widget(channel_list.channel_list(member, label2))
        layout.add_widget(label)
        label2.pos = (Window.width * .1, 0)
        layout.add_widget(label2)
        self.layout = layout

        return layout

    def on_stop(self):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text="Закрытие..."))
        try:
            channel_list.close()
        except: pass


if __name__ == '__main__':
    app = StartScreenApp()
    app.run()
