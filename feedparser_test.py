import feedparser
import oauth_login
import re




def get_twitter_userid(author):
    t = oauth_login.login()
    twitter_results= t.users.lookup(screen_name=author)
    name = twitter_results[u'name']
    followers_count = twitter_results[u'followers_count']
    return name + ' : ' + followers_count


d = feedparser.parse('http://www.texastribune.org/feeds/main/')
posts = d['entries']


for post in posts:
    output  = 'author=' + post['author']
    author_info = get_twitter_userid(post['author'])
    #to get public URL, take value below and remove everything past the ?
    # parameter
    feedItemURL = post['links'][0]['href']
    match = re.search(r'(.*)/\?utm.*', feedItemURL)
    output += ', link = ' + match.group(1)
    output += ', publication datetime = ' + post['published'] #also a post
    print output
print d['feed']
print d['feed']['links']
