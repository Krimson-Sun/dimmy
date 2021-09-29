class InvalidNumber(Exception):
    pass


num = input()
try:
    num = ''.join(num.split())
    if num[:2] == '+7' or num[0] == '8':
        if num[0] == '8':
            num = num[1:]
        else:
            num = num[2:]
    else:
        raise InvalidNumber
    if '(' in num:
        if '((' not in num:
            if ')' in num:
                if '))' not in num:
                    num = ''.join(''.join(num.split('(')).split(')'))
                else:
                    raise InvalidNumber
            else:
                raise InvalidNumber
        else:
            raise InvalidNumber

    elif ')' in num:
        raise InvalidNumber
    if '-' in num:
        if '--' in num or num[-1] == '-':
            raise InvalidNumber
        else:
            num = ''.join(num.split('-'))
    n = num
    num = ''.join(filter(str.isdigit, list(num)))
    if num != n:
        raise InvalidNumber
    if len(num) == 10:
        print('+7' + num)
    else:
        raise InvalidNumber
except InvalidNumber:
    print('error')
