for x in range(19):
    a = 5*19**4+5*19**3+x*19**2+3*19+6
    b = x*19**4+2*19**3+7*19**2+2*19+4
    f = a+b
    if f % 5 ==0:
        print(x, f/5)


#192567
