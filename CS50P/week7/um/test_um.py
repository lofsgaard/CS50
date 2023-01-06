from um import count

def test_count():
    assert count('um') == 1
    assert count('UM') == 1
    assert count('this is um, a test to find um in a sentence') == 2
    assert count('this sentence does not include anything, except ummpires') == 0