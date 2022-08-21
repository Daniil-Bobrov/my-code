with open("config.csv", "r") as config:
    text = config.read()
# text = text.split("\n")
# name = text[0]
# password = text[1]
id = text


def write(text: iter):
    with open("config.csv", "w") as config:
        config.write(str(text))


def reset():
    global text, id
    with open("config.csv", "r") as config:
        text = config.read()
    text = text
    id = text


def clear_cache():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        for cat in Cache._categories:
            Cache._objects[cat] = {}


def stop_app(app):
    app.root_window.close()
    clear_cache()


def get_channels():
    global text
    import utils
    reset()
    member = utils.Member(text)
    return [member.guilds[id] for id in member.guilds if not id.isalpha()]
