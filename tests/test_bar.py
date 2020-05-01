from pylambda.bar import spam

def test_spam():
    assert spam() == 'Importing from local passed'
