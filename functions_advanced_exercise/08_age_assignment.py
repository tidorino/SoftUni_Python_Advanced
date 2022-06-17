def age_assignment(*args, **kwargs):
    text = [word for word in args]
    result = {}
    for key, value in kwargs.items():
        for el in text:
            if key in el:
                result[el] = value
    sorted_names = [f'{key} is {value} years old.' for key, value in sorted(result.items(),key=lambda x: x[0])]
    return '\n'.join(sorted_names)

    # result = {}
    # for name in args:
    #     first_letter = name[0]
    #     age = kwargs[first_letter]
    #     result[name] = age
    # sorted_result = [f'{key} is {value} years old.' for key,value in sorted(result.items(), key=lambda x: x[0])]
    # return '\n'.join(sorted_result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
