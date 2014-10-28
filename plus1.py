number = 99999
add = int('1'*len(str(number)))
print(number + add)


def wages():
    hour_wage = 7.79
    hours_wrk = eval(input("Please tell me how many hours you have worked this week:" ))

    if hours_wrk > 40:
        hour_wage = 7.79 * 3


    result = hour_wage * hours_wrk


    print(result)

wages()
