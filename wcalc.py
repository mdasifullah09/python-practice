def calc():
    print('Weekly loan calculator\n')
    l=int(input('Enter the amount of loan:'))
    r=float(input('Enter the interest rate(%):'))
    y=int(input('Enter the number of years:'))
    i=(r/5200)
    wp=i*l/((1-((1+i)**-(52*y))))
    print('Your weekly payment will be: $',round(wp,2))
calc()
