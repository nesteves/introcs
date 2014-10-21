__author__ = 'nunoe'


class NewsStory(object):

    def __init__(self, guid, titl, subj, summ, link):
        self.guid = guid
        self.titl = titl
        self.subj = subj
        self.summ = summ
        self.link = link

    def get_guid(self):
        return self.guid

    def get_titl(self):
        return self.titl

    def get_subj(self):
        return self.subj

    def get_summ(self):
        return self.summ

    def get_link(self):
        return self.link