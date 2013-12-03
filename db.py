#! /usr/bin/env python
#! coding=utf-8

# Imports: Standard Libraries
import collections

# Imports: Related 3rd parties
import pymongo

# Imports: Local Application
import wsgi


# Constants: Database Info
_DB_URL_TMPL = 'mongodb://%s:%s@%s:%d/%s'
_DB_USR = '' # db usr
_DB_PWD = '' # db pwd
_DB_HOST = '' # db host
_DB_PORT = 0 # db port
_DB_NAME = '' # db name

# Constants: Collection Info
_COLL_TERRAN = 'terran'
_COLL_PROTOSS = 'protoss'
_COLL_ZERG = 'zerg'


# Classes
class _Ability(object):
    """
    """
    def __init__(self, abil):
        """
        """
        self.pict = wsgi.get_pic_url(abil['_pict'])
        self.name = abil['_name']
        self.desc = abil['_desc']
        self.attr = collections.OrderedDict()

        for key, value in sorted(abil.items()):
            if key in ['_pict', '_name', '_desc']:
                pass
            else:
                value_key, value_value = value.split(':')
                self.attr[value_key] = value_value.strip()


class _Upgrade(object):
    """
    """
    def __init__(self, upgd):
        """
        """
        self.pict = wsgi.get_pic_url(upgd['_pict'])
        self.name = upgd['_name']
        self.desc = upgd['_desc']
        self.attr = collections.OrderedDict()

        for key, value in sorted(upgd.items()):
            if key in ['_pict', '_name', '_desc']:
                pass
            else:
                value_key, value_value = value.split(':')
                self.attr[value_key] = value_value.strip()


class Document(object):
    """
    """
    def __init__(self, doc):
        """
        """
        self.abils = None
        self.upgds = None
        self.attrs = collections.OrderedDict()

        for key, value in sorted(doc.items()):
            if key in ['_id', '_uniq', '_pict']:
                pass
            elif key == '_name':
                self.name = value
            elif key == '_desc':
                self.desc = value
            elif key == '_abil':
                self.abils = self.organize_abilities_data(value)
            elif key == '_upgd':
                self.upgds = self.organize_upgrades_data(value)
            else:
                value_key, value_value = value.split(':')
                self.attrs[value_key] = value_value.strip()

    def organize_abilities_data(self, abils):
        """
        """
        list_of_abils = []
        for key, value in sorted(abils.items()):
            list_of_abils.append(_Ability(value))
        return list_of_abils

    def organize_upgrades_data(self, upgds):
        """
        """
        list_of_upgds = []
        for key, value in sorted(upgds.items()):
            list_of_upgds.append(_Upgrade(value))
        return list_of_upgds


# Functions
def get_doc_from_db(lowercase_name):
    """
    """
    # Connect to db
    url = _DB_URL_TMPL % (_DB_USR, _DB_PWD, _DB_HOST, _DB_PORT, _DB_NAME)
    conn = pymongo.Connection(url)
    db = conn[_DB_NAME]

    # Query each collection within the db
    coll_names = [_COLL_TERRAN, _COLL_PROTOSS, _COLL_ZERG]
    rule = {'_uniq': lowercase_name}

    for coll_name in coll_names:
        coll = db[coll_name]
        doc = coll.find_one(rule)
        if doc is not None:
            return doc
    return None


def organize_doc_data(doc):
    """
    """
    return Document(doc)


def extract_card_info_from_doc(doc):
    """
    """
    info = {}
    info['title'] = doc['_name']
    info['desc'] = doc['_desc']
    info['pic_url'] = wsgi.get_pic_url(doc['_pict'])
    info['spec_url'] = wsgi.get_spec_url(doc['_uniq'])
    return info
