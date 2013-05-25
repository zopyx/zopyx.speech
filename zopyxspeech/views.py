# -*- coding: utf-8 *-*

from pyramid.view import view_config
import os
import requests

def execute(cmd):
    params = dict(cmd0=cmd, cmd1='aspMainZone_WebUpdateStatus/')
    requests.get('http://192.168.0.128/MainZone/index.put.asp', params=params)

COMMANDS = {
    u'verstärker ein': 'PutVolumeMute/off',
    u'verstärker aus': 'PutVolumeMute/on',
    u'sr2': 'PutZone_InputFunction/FAVORITE1',
    u'swr2': 'PutZone_InputFunction/FAVORITE2',
    u'swr3': 'PutZone_InputFunction/FAVORITE3',
    u'lautstärke 2' : 'PutMasterVolumeSet/-55.0',
    u'lautstärke 3' : 'PutMasterVolumeSet/-50.0',
    u'lautstärke 4' : 'PutMasterVolumeSet/-45.0',
    u'lautstärke 5' : 'PutMasterVolumeSet/-40.0',
    u'lautstärke 6' : 'PutMasterVolumeSet/-35.0',
    u'lautstärke 7' : 'PutMasterVolumeSet/-30.0',
}

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def home(request):
    query = request.params.get('query', '').lower()
    cmd = COMMANDS.get(query)
    print repr(query), cmd
    if cmd:
        execute(cmd)
    return {'project': 'zopyx.speech'}

