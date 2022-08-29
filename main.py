from Actions.followers import add_follower
from Utils.authentication import create_api
from Watch.user_timelines import user_timelines
from Actions.status_update import update_status

api = create_api()

## Sample functions for extracting tweets from my timeline
# my_timeline = user_timelines(api)

# for tweet in my_timeline:
#     print(f"{tweet.user.name} said {tweet.text}")

## Sample method to update status
# update_status(api, 'The basic laws of human stupidity')

## Sample method to add follower
# add_follower(api, 'DhawalAgrawal8')