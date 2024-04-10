def learn_walrus():
    tweet_limit = 280
    tweet_string = "Blah" * 50
    diff = tweet_limit - len(tweet_string)
    if diff >= 0:
        print("A fitting tweet")
    else:
        print("Went over by", abs(diff))


def learn_walrus_version_2():
    tweet_limit = 280
    tweet_string = "Blah" * 50
    if diff := tweet_limit - len(tweet_string):
        print("A fitting tweet")
    else:
        print("Went over by", abs(diff))


learn_walrus_version_2()
