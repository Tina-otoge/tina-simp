from browser import document

def convert_external_link_to_new_tab():
    import urllib.parse
    for el in document.select('a'):
        if urllib.parse.urlparse(el.attrs['href']).netloc:
            el.attrs['target'] = '_blank'

def convert_anchors_to_absolute():
    """
    When using <base> anchors are bound to the base href instead of current page
    This cirumvents it by replacing every relative anchor links with absolute
    links so they are not picked up by <base> anymore
    """
    URL = document.location.href.split('#')[0]
    for el in document.select('a'):
        if (href := el.attrs['href']).startswith('#'):
            el.attrs['data-anchor'] = href
            el.href = URL + href

def smooth_anchor_scroll():
    def do_scroll(event):
        document.select(event.target.attrs['data-anchor'])[0].scrollIntoView(
            {'behavior': 'smooth'}
        )
        event.preventDefault()

    for el in document.select('[data-anchor]'):
        el.bind('click', do_scroll)

if __name__.startswith('__main__'):
    convert_external_link_to_new_tab()
    convert_anchors_to_absolute()
    smooth_anchor_scroll()
