# -*- coding: utf-8 -*-

import os
import pathspec
import argparse
import json
from ftplib import FTP
import ftplib

from . import json_cleaner

__VERSION__ = "0.1.0"

__DEFAULT_CONF__ = """{
    "protocol": "ftp",
    "host": "localhost", // string - The hostname or IP address of the FTP server. Default: 'localhost'
    "port": 21, // integer - The port of the FTP server. Default: 21
    "user": "anonymous", // string - Username for authentication. Default: 'anonymous'
    "pass": "anonymous@", // string - Password for authentication. Default: 'anonymous@'
    "encoding": "big5",
    "remote": ".",
    "local": ".",
    "useGitIgnore": true,
    "gitIgnoreEncoding": "utf-8",
    "useFtpIgnore": true,
    "ftpIgnoreEncoding": "utf-8"
}
"""

class Config(dict):
    def __init__(self, file = None):
        if file is None:
            pass
        elif not os.path.exists(file):
            raise FileNotFoundError('Can\'t find config file "' + file + '"')
        else:
            with open(file, 'r', encoding='UTF-8') as fh:
                self.loadText(fh.read())

    def loadText(self, text):
        confText = json_cleaner.remove_comments(text)
        confDist = json.loads(confText)
        self.checkAndLoadDist(confDist)

    def checkAndLoadDist(self, confDist):
        # protocol
        if type(confDist['protocol']) is not str:
            raise Exception("config parameter \"protocol\" is error, plz check config file")
        elif confDist['protocol'] == '':
            self.protocol = 'ftp'
        elif confDist['protocol'] != 'ftp':
            raise Exception("unsupport portocol :" + confDist['protocol'])
        else:
            self.protocol = confDist['protocol']
        # host
        if type(confDist['host']) is not str:
            raise Exception("config parameter \"host\" is error, plz check config file")
        elif confDist['host'] == '':
            self.host = 'localhost'
        else:
            self.host = confDist['host']
        # port
        if type(confDist['port']) is not int:
            raise Exception("config parameter \"port\" is error, plz check config file")
        else:
            self.port = confDist['port']
        # user
        if type(confDist['user']) is not str:
            raise Exception("config parameter \"user\" is error, plz check config file")
        elif confDist['user'] == '':
            self.user = 'anonymous'
        else:
            self.user = confDist['user']
        # pass
        if type(confDist['pass']) is not str:
            raise Exception("config parameter \"pass\" is error, plz check config file")
        elif confDist['pass'] == '':
            self.passwd = 'anonymous@'
        else:
            self.passwd = confDist['pass']
        # encoding
        if type(confDist['encoding']) is not str:
            raise Exception("config parameter \"encoding\" is error, plz check config file")
        elif confDist['encoding'] == '':
            self.encoding = 'utf8'
        else:
            self.encoding = confDist['encoding']
        # remote
        if type(confDist['remote']) is not str:
            raise Exception("config parameter \"remote\" is error, plz check config file")
        elif confDist['remote'] == '':
            self.remote = '.'
        else:
            self.remote = confDist['remote']
        # local
        if type(confDist['local']) is not str:
            raise Exception("config parameter \"local\" is error, plz check config file")
        elif confDist['local'] == '':
            self.local = '.'
        else:
            self.local = confDist['local']
        # useGitIgnore
        if type(confDist['useGitIgnore']) is not bool:
            raise Exception("config parameter \"useGitIgnore\" is error, plz check config file")
        else:
            self.useGitIgnore = confDist['useGitIgnore']
        # gitIgnoreEncoding
        if type(confDist['gitIgnoreEncoding']) is not str:
            raise Exception("config parameter \"gitIgnoreEncoding\" is error, plz check config file")
        elif confDist['gitIgnoreEncoding'] == '':
            self.gitIgnoreEncoding = 'utf-8'
        else:
            self.gitIgnoreEncoding = confDist['gitIgnoreEncoding']
        # useFtpIgnore
        if type(confDist['useFtpIgnore']) is not bool:
            raise Exception("config parameter \"useFtpIgnore\" is error, plz check config file")
        else:
            self.useFtpIgnore = confDist['useFtpIgnore']
        # ftpIgnoreEncoding
        if type(confDist['ftpIgnoreEncoding']) is not str:
            raise Exception("config parameter \"ftpIgnoreEncoding\" is error, plz check config file")
        elif confDist['ftpIgnoreEncoding'] == '':
            self.ftpIgnoreEncoding = 'utf-8'
        else:
            self.ftpIgnoreEncoding = confDist['ftpIgnoreEncoding']
