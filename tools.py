def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
        return i


def file_text(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            yield i, l.strip()


def get_ua():
    from fake_useragent import UserAgent
    ua = UserAgent()
    return ua.random


def get_date():
    import datetime
    i = datetime.datetime.now()
    return [str(item) for item in [i.year, i.month, i.day, i.hour]]


def _async_raise(tid, exctype):
    import ctypes
    import inspect
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)
