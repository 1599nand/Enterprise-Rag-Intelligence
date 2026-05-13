USERS = {
    "alice": "hr",
    "bob": "engineering",
    "charlie": "finance",
    "admin": "admin"
}


def get_user_role(username):
    return USERS.get(username, "guest")