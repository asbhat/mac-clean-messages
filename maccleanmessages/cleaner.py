
import os
import re


class Cleaner(object):

    """
    Removes files and directories based on filter criteria


    TODO:
    - Make sure malicious rootPaths aren't set (e.g., '/' or '~')
    - Build out date criteria functionality
    """

    def __init__(self, rootPath, removeFlag, walkTD=False, criteria=None, critPosOrNeg=False, exclFolders=None):
        self.rootPath = rootPath
        self.removeFlag = removeFlag
        self.walkTD = walkTD
        self.criteria = self.list_to_regex_str(criteria)
        self.critPosOrNeg = critPosOrNeg
        self.exclFolders = self.list_to_regex_str(exclFolders)

    def clean_root(self):
        print 'running clean_root...'
        print 'self.criteria =', self.criteria
        for root, dirs, files in os.walk(self.rootPath, topdown=self.walkTD):
            dirs[:] = self.filter_to_be_removed(dirs, self.exclFolders, False)
            files[:] = self.filter_to_be_removed(files, self.criteria, self.critPosOrNeg)
            print root, 'dirs =', dirs, 'files =', files
            for f in files:
                self.remove_files(root, f, self.removeFlag)
            for d in dirs:
                # won't remove a directory unless it's empty
                try:
                    self.remove_directories(root, d, self.removeFlag)
                except OSError:
                    continue

        return self

    @staticmethod
    def list_to_regex_str(lst):
        return '({0})'.format(')|('.join(lst)) if type(lst) == list else lst

    @staticmethod
    def filter_to_be_removed(lst, criteria, critPosOrNeg):
        print 'filtering files...'
        if criteria is None:
            return lst
        elif critPosOrNeg:
            return [i for i in lst if re.search(criteria, i, re.I)]
        else:
            return [i for i in lst if not re.search(criteria, i, re.I)]

    @staticmethod
    def remove_files(path, f, removeFlag):
        filepath = os.path.join(path, f)
        if removeFlag:
            os.remove(filepath)
        else:
            os.rename(filepath, '{0}/.Trash/{1}'.format(os.path.expanduser('~'), f))

    @staticmethod
    def remove_directories(path, d, removeFlag):
        dirpath = os.path.join(path, d)
        if removeFlag:
            os.rmdir(dirpath)
        elif os.listdir(dirpath) == []:
            os.rename(dirpath, '{0}/.Trash/{1}'.format(os.path.expanduser('~'), d))
