#! /usr/bin/env python
#! coding=utf-8

# Imports: Standard Libraries
import hashlib

# Imports: Related 3rd Parties
import flask

# Imports: Local Application
import chat
import db


# Constants: Server Info
SERVER_TKN = '' # token agreed by ur svr and the WeChat svr
SERVER_URL = '' # ur svr URL

# Constants: Path Info
PATH_DATA_SC2 = '/data/sc2/'
PATH_PICT_SC2 = '/static/pic/sc2/'

# Constants: Error States
ERROR_STATES = {
    'WRONG_SIGNATURE': 'ERROR: SIGNATURE DOES NOT MATCH',
    'UNKNOWN_SERVER': 'ERROR: MESSAGE FROM UNKNOWN SERVER'
}


# Global Variables
application = app = flask.Flask('wsgi')


# Functions: URL Handlers
@app.route('/')
def _handshake_with_wechat_server():
    """
    """
    signature = flask.request.args.get('signature', '')
    timestamp = flask.request.args.get('timestamp', '')
    nonce = flask.request.args.get('nonce', '')
    echostr = flask.request.args.get('echostr', '')

    if echostr and _check_signature(signature, timestamp, nonce):
        return echostr
    else:
        return ERROR_STATES['WRONG_SIGNATURE']


@app.route('/', methods=['POST'])
def _handle_request():
    """
    """
    signature = flask.request.args.get('signature', '')
    timestamp = flask.request.args.get('timestamp', '')
    nonce = flask.request.args.get('nonce', '')

    if _check_signature(signature, timestamp, nonce):
        wechat_msg = flask.request.data
        return chat.answer_incoming_wechat_msg(wechat_msg)
    else:
        return ERROR_STATES['UNKNOWN_SERVER']


@app.route(PATH_DATA_SC2 + '<object_name>')
def _view_object_info(object_name):
    """
    """
    doc = db.get_doc_from_db(object_name)
    if doc is None:
        flask.abort(404)
    else:
        organized_doc = db.organize_doc_data(doc)
        return flask.render_template('info.html', doc=organized_doc)


# Functions: Utilities
def _check_signature(signature, timestamp, nonce):
    """
    """
    if signature and timestamp and nonce:
        temp_arr = []
        temp_arr.append(SERVER_TKN)
        temp_arr.append(timestamp)
        temp_arr.append(nonce)
        temp_arr.sort()
        concatenated_str = ''.join(temp_arr)

        if hashlib.sha1(concatenated_str).hexdigest() == signature:
            return True
        else:
            return False
    else:
        return False


def get_pic_url(pic_file_name):
    """
    """
    return SERVER_URL + PATH_PICT_SC2 + pic_file_name


def get_spec_url(object_name):
    """
    """
    return SERVER_URL + PATH_DATA_SC2 + object_name


# Main
if __name__ == '__main__':
    app.run(debug=False)
