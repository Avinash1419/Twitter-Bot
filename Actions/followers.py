def add_follower(api, name):
    return api.create_friendship(screen_name = name)