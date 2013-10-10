from pattern.en import parse, pprint
from pattern.web import Twitter, plaintext
from pattern.web import Newsfeed

#pattern.web

# s = Twitter().stream('#fail')
# for i in range(10):
#     s.update(bytes=1024)
#     print s[-1].text if s else ""
#
# print Twitter().trends()

#t = Twitter(license='', throttle=1.0, language='en')


from pattern.web import Twitter
print Twitter().trends(cached=False)


#
from pattern.web import Twitter
twitter = Twitter()
last_id = None
for i in range(2):
    for tweet in twitter.search('#stand4life', start=last_id, count=1000,
                                cached=False):
        print tweet.text
        last_id = tweet.id
print last_id



# for tweet in Twitter().search('heroes', cached=False):
#     print plaintext(tweet.description)

# from pattern.web import URL, extension
# url = URL('http://www.sportclips.com/Library/images/logo.png')
# f = open('test' + extension(url.page), 'w')
# f.write(url.download())
# f.close()
#

#How to do RSS
# NATURE = 'http://www.nature.com/nature/current_issue/rss/index.html'
# for result in Newsfeed().search(NATURE)[:5]:
#     print repr(result.title)



#pattern.en
#
# s='The mobile web is more important than mobile apps'
# s = parse(s, relationship=True, lemmata=True)
# pprint(s)


# from pattern.web    import Bing, plaintext
# from pattern.en     import parsetree
# from pattern.search import search
# from pattern.graph  import Graph, Node, Edge, export
#
# g = Graph()
# for i in range(10):
#     for r in Bing().search('"more important than"', start=i+1, count=50):
#         s = r.description.lower()
#         s = plaintext(s)
#         t = parsetree(s)
#         p = '{NP} (VP) more important than {NP}'
#         for m in search(p, t):
#             a = m.group(1).string # Left NP.
#             b = m.group(2).string # Right NP.
#             if a not in g:
#                 g.add_node(a, radius=5, stroke=(0,0,0,0.8))
#             if b not in g:
#                 g.add_node(b, radius=5, stroke=(0,0,0,0.8))
#             g.add_edge(g[b], g[a], stroke=(0,0,0,0.6))
#
# g = g.split()[0] # Largest subgraph.
#
# for n in g.sorted()[:40]: # Sorted by Node.weight.
#     n.fill = (0.0, 0.5, 1.0, 0.7 * n.weight)
#
# export(g, 'test', directed=True, weighted=0.6, distance=6)