import traceback

class access_modifiers:
    __private = 'private variable'
    _protected = 'protected variable'
    public = 'public variable'

    def __init__(self):
        print(self.__private)
        print(self._protected)
        print(self.public)

access_modifiers1 = access_modifiers()
try:
    print(access_modifiers1.public)
    print(access_modifiers1.__private)
    raise Exception('Unable to access private variable')
    print(access_modifiers1._protected)
    raise Exception('Unable to access protected variable')
except Exception:
    print(Exception)