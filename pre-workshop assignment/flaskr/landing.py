import functools
from random import randrange

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('landing', __name__)

@bp.route('/', methods=('GET',))
def index():
    msgs = [
        "Logic will get you from A to B. Imagination will take you everywhere.",
        "There are 10 kinds of people. Those who know binary and those who dont.",
        "There are two ways of constructing a software design. One way is to make it so simple that there are obvioursly no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
        "It's not that I'm so smart, it's just that I stay with problems longer.",
        "It is pitch dark. You are likely to be eaten by a grue."
    ]
    msg = msgs[randrange(len(msgs))]
    return render_template('landing/index.html', msg=msg)
