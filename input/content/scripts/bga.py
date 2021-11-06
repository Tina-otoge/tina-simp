from browser import document, timer
from browser.html import DIV, IMG

from scripts import utils

TIME_PER_LOOP = 5000
TRANSITION_TIME = 1000
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
    set_bga(BGA_CURRENT, current)
    BGA_CURRENT.classList.remove('fade')

@utils.repeat(5)
def loop_bga():
    global current
    current += 1
    if current > BGA_COUNT:
        current = 1
    set_bga(BGA_NEXT, current)
    BGA_CURRENT.classList.add('fade')
    timer.set_timeout(rotate_bga, TRANSITION_TIME)

if __name__.startswith('__main__'):
    document.select('body')[0].prepend(BGA_PARENT)
    loop_bga()
