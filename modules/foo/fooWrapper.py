from ctypes import cdll
lib = cdll.LoadLibrary('/Users/edwincloud/Documents/Make School/projects/python/tweet-generator/modules/foo/libfoo.so')

class Foo(object):
    def __init__(self):
        self.obj = lib.Foo_new()

    def bar(self):
        lib.Foo_bar(self.obj)