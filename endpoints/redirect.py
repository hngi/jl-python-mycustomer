from flask import redirect, request


def get():
    return redirect(str(request.url_root)+"ui")
