from twttr import shorten

def test_shorten_upper():
    assert shorten('TWITTER') == 'TWTTR'

def test_shorten_lower():
    assert shorten('twitter') == 'twttr'

def test_shorten_number():
    assert shorten('twitter3') == 'twttr3'

def test_shorten_punctuations():
    assert shorten('twitter.') == 'twttr.'