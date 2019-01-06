import math
def conversion():
    print('Imperial to Metric conversion')
    t=int(input('Enter the number of tons :'))
    s=int(input('Enter the number of stone :'))
    p=int(input('Enter he number o5f pound :'))
    o=int(input('Enter the number of ounces :'))
    total_o=35274*t+224*s+16*p+o
    k=total_o/35.274
    g=k/1000
    m_t=int(t*1000)
    
    print('The matric weight is',m_t,'matric tons',k,'kilos',g,'grams')
conversion()
