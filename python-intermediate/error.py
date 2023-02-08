INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)

class invalidPasswordError(ValueError):
    pass

def validate_password(username, password):
    if username==password:
        raise(invalidPasswordError("username and password cannot be the same!"))
    if password in INVALID_PASSWORDS:
        raise(invalidPasswordError("Your password is too common and not safe!"))


def create_account(username, password):
    return (username, password)


def main(username, password):
    try:
        valid = validate_password(username, password)
    except invalidPasswordError as e:
        print(e)
    else:
        account = create_account(username, password)
    finally:
        print("Validated password against username and collection")


if __name__ == '__main__':
    main('jim', 'jam')
    main('admin', 'password')  # Oh no!
    main('guest', 'guest')  # Oh no!
