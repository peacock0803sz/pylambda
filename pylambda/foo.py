from pylambda.bar import spam


def ham():
    print(spam(), 'success')


if __name__ == 'main':
    ham()
