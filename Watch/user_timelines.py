# from Utils.authentication import create_api


# api = create_api()

def user_timelines(api):
    timeline = api.home_timeline()
    return timeline


