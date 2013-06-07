import oauth_login

t = oauth_login.login()

# tweets = t.statuses.user_timeline()
#
# for tweet in tweets:
#     print tweet


# tweets3 = t.statuses.user_timeline()
#
# for tweet in tweets3:
#     print tweet[u'id'], tweet[u'retweet_count']
#     # print tweet.id, tweet.retweet_count

# tweets2 = t.statuses.home_timeline(count=200, contributor_details=True)
#
# tweets2 = t.statuses.user_timeline(screen_name='texastribune', count=200)
#

tweets2 = t.search.tweets(q='http://www.texastribune.org/2013/05/30/transportation-lege-backed-tolls-and-debt-over-cas/', count=100, lang='en')

tweets4 = tweets2['statuses']

for tweet in tweets4:
    print 'tweetid =', tweet[u'id'], 'retweet_count', \
        tweet[u'retweet_count'], 'name', \
        tweet[u'user'][u'name']
    if tweet[u'entities'][u'urls'] > 0:
        for url in tweet[u'entities'][u'urls']:
            # lookup users
            user = t.users.lookup(user_id=30203903)
            # print total users
            print url[u'display_url'], url[u'expanded_url']
            # for urls in tweet[u'urls']:
            #     print 3
            # urls = entity[u'urls']
            # for url in urls:
            #     print 'url displayed', url[u'display_url'], 'url_expanded', \
            #         url[u'expanded_url']

# for tweet in tweets2:
#     print tweet
