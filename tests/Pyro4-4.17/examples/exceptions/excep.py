import pickle


class MyError(Exception):
    pass

class UnserializableError(Exception):
    def __reduce__(self):
        raise pickle.PicklingError("make this nonpickleable")


class TestClass(object):
    def div(self, arg1, arg2):
        return arg1/arg2
    def error(self):
        raise ValueError('a valueerror! Great!')
    def error2(self):
        return ValueError('a valueerror! Great!')
    def othererr(self):
        raise MyError('my error!')
    def othererr2(self):
        return MyError('my error!')
    def complexerror(self):
        x=Foo()
        x.crash()
    def unserializable(self):
        raise UnserializableError("this error can't be serialized")


class Foo(object):
    def crash(self):
        self.crash2('going down...')
    def crash2(self, arg):
        # this statement will crash on purpose:
        x=arg//2
