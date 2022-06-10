from custom_exeptions import MustContainAtSymbolError, NameTooShortError, InvalidDomainError


def is_valid(domain_data):
    if '.org' in domain_data or '.com' in domain_data or '.bg' in domain_data or '.net' in domain_data:
        print('Email is valid')
        return True
    else:
        return False


data = input()

while data != 'End':
    email = data

    email_parts = email.split('@')
    if len(email_parts) != 2:
        raise MustContainAtSymbolError('Email must contain @')

    name, domain = email_parts
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if not is_valid(domain):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    data = input()


