#! /usr/bin/env python
#! coding=utf-8

# Imports: Standard Libraries
import time

# Imports: Related 3rd Parties
import bs4

# Imports: Local Application
import db
import sc2


# Constants: WeChat MSG Templates
_WECHAT_TEXT_MSG_TMPL = '''
    <xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    <FuncFlag>0</FuncFlag>
    </xml>
    '''
_WECHAT_MULTIMEDIA_MSG_TMPL = '''
    <xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[news]]></MsgType>
    <ArticleCount>1</ArticleCount>
    <Articles>
    <item>
    <Title><![CDATA[%s]]></Title>
    <Description><![CDATA[%s]]></Description>
    <PicUrl><![CDATA[%s]]></PicUrl>
    <Url><![CDATA[%s]]></Url>
    </item>
    </Articles>
    </xml>
    '''

# Constants: Content Templates
_CONTENT_NOT_SUPPORTED = \
    'Not supported.'
_CONTENT_NOT_IMPLEMENTED = \
    'Not implemented.'
_CONTENT_UNRECOGNIZED_INPUT = \
    'Input not recognized. Enter "help" for usage instruction.'
_CONTENT_WRONG_CMD_FORMAT = \
    'Command format is wrong. Enter "Help" for usage instruction.'
_CONTENT_NO_MATCH_FOUND = \
    'No match %s found.'
_CONTENT_HELP = \
    'Enter "help" to show this usage instruction.\n'                \
    'Enter "list terran/protoss/zerg" to show unit of that race.\n' \
    'Enter "query <unit_name>" to show info about the unit.'
_CONTENT_SUBSCRIBE = \
    'Welcome to MonkeyChat for StarCraft 2!\n' + _CONTENT_HELP
_CONTENT_UNSUBSCRIBE = \
    'Goodbye!'

# Constants: Supported Commands
_SUPPORTED_CMDS = ['help', 'random', 'list', 'query']


# Functions
def answer_incoming_wechat_msg(wechat_msg):
    """
    """
    msg = bs4.BeautifulSoup(wechat_msg, 'xml')
    msg_type = msg.find('MsgType').text

    if msg_type == 'event':
        return _answer_msg_of_type_event(msg)
    elif msg_type == 'text':
        return _answer_msg_of_type_text(msg)
    else:
        return _return_text_msg(msg, _CONTENT_NOT_IMPLEMENTED)


def _answer_msg_of_type_event(msg):
    """
    """
    event = msg.find('Event').text

    if event == 'subscribe':
        return _return_text_msg(msg, _CONTENT_SUBSCRIBE)
    elif event == 'unsubscribe':
        return _return_text_msg(msg, _CONTENT_UNSUBSCRIBE)
    else:
        return _return_text_msg(msg, _CONTENT_NOT_SUPPORTED)


def _answer_msg_of_type_text(msg):
    """
    """
    content_list = msg.find('Content').text.strip().lower().split()

    if len(content_list) == 0 or content_list[0] not in _SUPPORTED_CMDS:
        return _return_text_msg(msg, _CONTENT_UNRECOGNIZED_INPUT)
    elif content_list[0] == 'help':
        return _return_text_msg(msg, _CONTENT_HELP)
    elif content_list[0] == 'list':
        return _handle_command_list(msg, content_list)
    elif content_list[0] == 'query':
        return _handle_command_query(msg, content_list)


def _handle_command_list(msg, content_list):
    """
    """
    if len(content_list) != 2:
        return _return_text_msg(msg, _CONTENT_WRONG_CMD_FORMAT)
    else:
        race = content_list[1]
        if race not in sc2.RACES:
            return _return_text_msg(msg, _CONTENT_NO_MATCH_FOUND % 'race')
        else:
            if race == 'terran':
                selected_units = sc2.TERRAN_UNITS
            elif race == 'protoss':
                selected_units = sc2.PROTOSS_UNITS
            else:
                selected_units = sc2.ZERG_UNITS

            content = ''
            for unit in selected_units:
                content = content + unit + '\n'
            content = content.strip()
            return _return_text_msg(msg, content)


def _handle_command_query(msg, content_list):
    """
    """
    if len(content_list) != 2:
        return _return_text_msg(msg, _CONTENT_WRONG_CMD_FORMAT)
    else:
        lowercase_name = content_list[1]
        doc = db.get_doc_from_db(lowercase_name)
        if doc is None:
            return _return_text_msg(msg, _CONTENT_NO_MATCH_FOUND % 'entry')
        else:
            info = db.extract_card_info_from_doc(doc)
            return _return_multimedia_msg(msg, info, lowercase_name)


def _return_text_msg(msg, content):
    """
    """
    to_user_name = msg.find('FromUserName').text
    from_user_name = msg.find('ToUserName').text
    create_time = str(int(time.time()))
    return _WECHAT_TEXT_MSG_TMPL % \
        (to_user_name, from_user_name, create_time, content)


def _return_multimedia_msg(msg, info, lowercase_name):
    """
    """
    to_user_name = msg.find('FromUserName').text
    from_user_name = msg.find('ToUserName').text
    create_time = str(int(time.time()))
    title = info['title']
    desc = info['desc']
    pic_url = info['pic_url']
    spec_url = info['spec_url']
    return _WECHAT_MULTIMEDIA_MSG_TMPL % \
        (to_user_name, from_user_name, create_time, title,
         desc, pic_url, spec_url)
