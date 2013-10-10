# coding=utf-8

from pattern.vector import Document


s = '''
    The shuttle Discovery, already delayed three times by technical problems
    and bad weather, was grounded again Friday, this time by a potentially
    dangerous gaseous hydrogen leak in a vent line attached to the shipʼs
    external tank. The Discovery was initially scheduled to make its 39th
    and final flight last Monday, bearing fresh supplies and an intelligent
    robot for the International Space Station. But complications delayed the
    flight from Monday to Friday,  when the hydrogen leak led NASA to conclude
    that the shuttle would not be ready to launch before its flight window
    closed this Monday.
'''

d = Document(s)
print d.keywords(top=10)
d._description = 'sample corpus'
print d._description
print d.term_frequency('flight')
print d.tfidf('flight')
print d.features
print d.words
print 'vector = ', d.vector