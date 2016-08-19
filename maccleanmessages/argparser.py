
import argparse
import sys

from datetime import datetime


class CleanMessagesArgParse(object):

    """
    A wrapper for the 'argparse' module

    Parses and checks arguments needed to clean message app data
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Inputs to Clean Messages Data')
        self._args = None

    @property
    def args(self):
        if self._args is None:
            self.arg_parse()
        return self._args

    @args.setter
    def args(self, newArgs):
        assert type(newArgs) == dict
        self._args = newArgs

    def arg_parse(self):
        self.add_arguments()
        self.args = vars(self.parser.parse_args())
        self.arg_check()
        return self

    def add_arguments(self):
        self.parser.add_argument('-r', '--remove', help='WARNING this removes files (instead of moving them to Trash)', required=False, action='store_true', default=False)
        self.parser.add_argument('-n', '--names', help='Save messages from people with these names (*not* case sensitive)', nargs='+', required=False)
        self.parser.add_argument('-s', '--startdate', help='Save messages BEFORE the start date ("yyyy-mm-dd" format)', required=False, type=self.date_check)
        self.parser.add_argument('-e', '--enddate', help='Save messages AFTER the end date ("yyyy-mm-dd" format)', required=False, type=self.date_check)

    @staticmethod
    def date_check(dateStr):
        try:
            dte = datetime.strptime(dateStr, '%Y-%m-%d')
        except ValueError:
            raise argparse.ArgumentTypeError('{0} is not a valid date'.format(dateStr))
        return dte

    def arg_check(self):
        if self._args['names'] is None:
            self.parse_response('Do you really want to clean *all* messages (y/[n])? ')
        if self._args['remove']:
            self.parse_response('Do you really want to *permanently* delete messages (y/[n])? ')

    @staticmethod
    def parse_response(message):
        response = raw_input(message)
        if response.lower() not in ('y', 'yes'):
            sys.exit()
