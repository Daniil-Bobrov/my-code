import firebase_admin
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate("firebase.json")
try:
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL': "https://virus-danil-default-rtdb.firebaseio.com"
    })
except Exception as e:
    pass


# ref = db.reference("/")
# ref.set(
#     {
#         "guilds":
#             {
#                 "0": {
#                     "name": "first_guild",
#                     "id": 0,
#                     "owner_id": 0,
#                     "members": {
#                         "Red_Dragon": 0
#                     },
#                 }
#             },
#         "members":
#             {
#                 "0": {
#                     "name": "Red_Dragon",
#                     "id": 0,
#                     "password": "",
#                     "guilds": [0, 1],
#                 },
#             }
#     }
# )


def create_account(name=None, password=None):
    members = db.reference("/members")
    l = list(members.get())
    l.append(
        {
            "id": len(l),
            "name": name,
            "password": password,
            "guilds": {"id": "name"},
        }
    )
    members.set(l)
    return len(l)-1


def create_guild(name, owner_id=None):
    if owner_id is None:
        import config
        owner_id = int(config.id)
    owner = get_member(owner_id)
    guilds = db.reference("/guilds/")
    l = guilds.get()
    l.append(
        {
            "name": name,
            "id": len(l),
            "owner_id": owner["id"],
            "members": {
                owner["name"]: owner["id"],
            },
            "messages": {
                "id": 0,
            }
        }
    )
    guilds.set(l)
    ref = db.reference(f"/members/{owner['id']}/guilds")
    member = ref.get()
    member[str(len(l)-1)] = name
    # print(member)
    ref.update(member)
    return len(l)-1


def get_member(id):
    members = db.reference("/members/").get()
    # print(members)
    return members[str(id)]


def get_guild(id):
    guilds = db.reference("/guilds/").get()
    # print(guilds, id)
    return guilds[int(id)]


def f():
    ref = db.reference("/members")


# create_account("account1", "password1")
# create_guild("чат", 0)
# print(Message(0))
