from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

Window.size = (260, 560)
name = str()
password = str()
password2 = str()


def registration_name(instance, text):
    global name
    if len(text) > len(name) and not text[-1].isalnum():
        instance.text = text[:-1]
    else:
        name = text


def registration_password(instance, text: str):
    global password
    if len(text) > len(password) and not text[-1].isalnum():
        instance.text = text[:-1]
    else:
        password = text


def registration_password2(instance, text: str):
    global password2
    if len(text) > len(password2) and not text[-1].isalnum():
        instance.text = text[:-1]
    else:
        password2 = text


def registration(*args):
    global password, password2, name
    if password == "" or name == "" or password2 == "" or password != password2:
        return
    # text = list()
    import config
    # text.append(name)
    # text.append(password)
    global app
    app.stop()
    import firebase
    config.write(firebase.create_account(name, password))


class MyButton(Button):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(.5, .5, 1, 1)
            Rectangle(pos=self.pos, size=self.size)


class RegistrationScreen(FloatLayout):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(.5, .5, 1, 1)
            Rectangle(pos=self.pos, size=self.size)


class RegistrationApp(App):
    def build(self):
        screen = RegistrationScreen()
        label = Label(
            text="Введите имя:",
            pos_hint={'x': .35, 'y': .8},
            size_hint=(.3, .1),
        )
        screen.add_widget(label)

        name = TextInput(
            multiline=False,
            pos_hint={'x': .1, 'y': .7},
            size_hint=(.8, .1),
        )
        name.bind(text=registration_name)
        screen.add_widget(name)

        label = Label(
            text="Введите пароль:",
            pos_hint={'x': .35, 'y': .6},
            size_hint=(.3, .1),
        )
        screen.add_widget(label)

        password = TextInput(
            multiline=False,
            pos_hint={'x': .1, 'y': .5},
            size_hint=(.8, .1),
            password=True,
        )
        password.bind(text=registration_password)
        screen.add_widget(password)

        label = Label(
            text="Введите пароль:",
            pos_hint={'x': .35, 'y': .4},
            size_hint=(.3, .1),
        )
        screen.add_widget(label)

        password2 = TextInput(
            multiline=False,
            pos_hint={'x': .1, 'y': .3},
            size_hint=(.8, .1),
            password=True,
        )
        password2.bind(text=registration_password2)
        screen.add_widget(password2)

        button = MyButton(
            text="Зарегистрироваться",
            pos_hint={'x': .1, 'y': .2},
            size_hint=(.8, .1),
        )
        button.bind(on_press=registration)
        screen.add_widget(button)
        return screen

    def on_stop(self):
        global app
        import config
        config.stop_app(app)


app = RegistrationApp()
app.run()
