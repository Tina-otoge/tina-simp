from browser import document, timer
from browser.html import DIV, IMG

from scripts import utils

START_TIME = 10 * 1000
TRANSITION_TIME = 1 * 1000
BGA_COUNT = 13
BGA_PATH_FMT = 'assets/img/bga/lincle_generic_{}.jpg'
BGA_PARENT = DIV(id='bga')
BGA_CURRENT = IMG()
BGA_NEXT = IMG()
BGA_PARENT <= BGA_NEXT + BGA_CURRENT

current = 1

def set_bga(element, index):
    element['src'] = BGA_PATH_FMT.format(index)

def rotate_bga():
    global current
    set_bga(BGA_CURRENT, current)
    BGA_CURRENT.classList.remove('fade')
    current = get_next()
    set_bga(BGA_NEXT, current)

def get_next():
    result = current + 1
    if result > BGA_COUNT:
        result = 1
    return result

@utils.repeat(5)
def loop_bga():
    BGA_CURRENT.classList.add('fade')
    timer.set_timeout(rotate_bga, TRANSITION_TIME)

if __name__.startswith('__main__'):
    document.select('body')[0].prepend(BGA_PARENT)
    rotate_bga()
    timer.set_timeout(loop_bga, START_TIME)
