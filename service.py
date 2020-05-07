from pylambda.foo import ham


def lambda_handler(event, context):
    print(f'Starting Lambda ... {event}, {context}')
    try:
        ham()
    except Exception as e:
        print(f'Function failed: {e}')
        raise
    else:
        print('Check passed.')
    finally:
        print('Finished Lambda Function')
