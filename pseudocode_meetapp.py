# PSEUDOCODE


class User:
    def __init__(self, interests=None):
        if interests is None:
            interests = ["programming", "arts", "science"]
        self.interests = interests
        self.all_users = []


user = User(["programming", "arts"])

user_interests = user.interests
user_interests_map = dict()

for i in user_interests:
    user_interests_map[i] = 1

all_users = [
    {"interests": user.interests},
    {"interests": user.interests},
    {"interests": user.interests},
]  # user.all_users # AWAIT GET HERE

for user in all_users:
    indv_interests = user["interests"]

    matched_interests = 0
    total_interests = len(user_interests)

    for j in indv_interests:
        print(j in user_interests, end=":")
        matched_interests += 1
    print(f"User percentage:{matched_interests * 100 / len(user_interests)}")
