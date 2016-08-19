#!/usr/bin/env python

import os

from argparser import CleanMessagesArgParse
from cleaner import Cleaner
from datetime import datetime


def main():
    CleanMessagesDriver().main()


class CleanMessagesDriver(object):

    """
    """

    ATTACHMENTS_PATH = '{0}/Library/Messages/Attachments/'.format(os.path.expanduser('~'))
    CHAT_DB_PATH = '{0}/Library/Messages/'.format(os.path.expanduser('~'))
    CHAT_CRITERIA = 'chat'
    CHAT_EXCL_FOLDER = 'attachments'
    CONTAINER_PATH = '{0}/Library/Containers/com.apple.iChat/Data/Library/Messages/Archive/'.format(os.path.expanduser('~'))

    def __init__(self):
        pass

    def main(self):
        args = CleanMessagesArgParse().args
        rt = datetime.now()

        print('[{t}] Cleaning attachments...'.format(t=datetime.now()))
        attachmentCleaner = Cleaner(CleanMessagesDriver.ATTACHMENTS_PATH, args['remove'])
        attachmentCleaner.clean_root()

        print('[{t}] Cleaning chat databases...'.format(t=datetime.now()))
        chatCleaner = Cleaner(
                CleanMessagesDriver.CHAT_DB_PATH,
                args['remove'],
                walkTD=True,
                criteria=CleanMessagesDriver.CHAT_CRITERIA,
                critPosOrNeg=True,
                exclFolders=CleanMessagesDriver.CHAT_EXCL_FOLDER
            )
        chatCleaner.clean_root()

        print('[{t}] Cleaning container logs...'.format(t=datetime.now()))
        containerCleaner = Cleaner(
                CleanMessagesDriver.CONTAINER_PATH,
                args['remove'],
                criteria=args['names'],
                critPosOrNeg=False
            )
        containerCleaner.clean_root()

        rt = datetime.now() - rt
        print('[{t}] Done in {rt}!'.format(t=datetime.now(), rt=rt))


if __name__ == '__main__':
    main()
