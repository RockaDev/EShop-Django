

def retry_on_exception(view):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return view(*args, **kwargs)
            except:
                pass
    return wrapper