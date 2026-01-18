
try:
    name = input("please tell me your name so as a will remember you well  ")
    user = input(f"Hi! {name}, what you did today?  ").lower()
    tasks = {
        "education": ["coding", "learning", "studying", "teaching"],
        "health":["athlete","swimming","push-ups","sports","walking"],
        "hobbies": ["singing", "drawing", "dancing", "playing", "gaming"],
        "lifestyle": ["drinking", "smoking", "exercising", "working"]
    }
    user_type = "others"
    while user!="exit":
        for task, words in tasks.items():
            for word in words:
                if word in user:
                    user_type = task
                    break

        print(f'>your task is categorized as: {user_type}')
        suggest = {
            "education": "focus on small exercises today!",
            "health":"Do it more and more, your body need to be active",
            "hobbies": "have some fun for a moment",
            "lifestyle": "take some break for it!"
        }
        print(f'>my suggestion is: {suggest[user_type]}')

        feedbacks = input("did you love our suggestion? [yes/no] ").lower()
        responses={
            "yes":"Thank you for your feedback!",
            "no":"Thank you for you feedback, well try to improve our service next time!"
        }
        oth="other"
        for feedback,feedfront in responses.items():
            for feed in feedback:
                if feed in feedbacks:
                    oth=feedfront
        print(f">Dear {name}, {oth}.")


        break

    else:
        print("bye")

except KeyError:
    print("write a suitable activity")


