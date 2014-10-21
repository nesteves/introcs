__author__ = 'nunoe'
import string

class NewsStory(object):

    def __init__(self, guid, titl, subj, summ, link):
        self.guid = guid
        self.titl = titl
        self.subj = subj
        self.summ = summ
        self.link = link

    def getGuid(self):
        return self.guid

    def getTitle(self):
        return self.titl

    def getSubject(self):
        return self.subj

    def getSummary(self):
        return self.summ

    def getLink(self):
        return self.link

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        print self.phrase
        print self.phrase in story.getTitle or self.phrase in story.getSubject or self.phrase in story.getSummary


def isWordIn(word, text):
    return word.lower() in parse_text(text)

def parse_text(text):
    for char in string.punctuation + "'":
        print char
        text.replace(char, ' ')
    return text
    return [word.lower() for word in text.split()]


if __name__ == '__main__':
    pt = PhraseTrigger("New York City")
    a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
    b = NewsStory('', '', "asdfasfdNew York Cityasfdasdfasdf", '', '')
    c = NewsStory('', '', '', "asdfasfdNew York Cityasfdasdfasdf", '')
    noa = NewsStory('', "something something new york city", '', '', '')

    print pt.evaluate(a)
    print pt.evaluate(b)
    print pt.evaluate(c)



