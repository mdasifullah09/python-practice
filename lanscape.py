""""Program 1 – Landscape Calculator 
A landscaping company needs a program that computes the price of landscaping for a new housing development. Work orders are based on: address, plot length and width in feet, type of grass (“fescue”, “bentgrass” or “campus”), and number of trees. The price is computed as follows:  
•	There is a base labour charge of $1000. 
•	If the surface (length * width) is over 5000 square feet, add $500. 
•	The cost is calculated per square foot. If the grass is “fescue” the cost is $0.05; for “bentgrass” it is $0.02; “campus” is $0.01. 
•	Each tree requested has a $100 charge. 
First, create a flowchart that clearly shows all the paths of execution that will exist within your designed solution to this problem. Write a console application that will input the address, property length and width, type of grass and number of trees, and then output the corresponding price.
Your solution must contain examples demonstrating your understanding of appropriate use of functions and core assignment concepts (decision structures).
EXAMPLES AND TESTING 
In the section below you will be presented with at least one screenshot of a successful execution of a sample solution to the program, which should help demonstrate how your input/output on the program should work. In addition to the sample values used in the screenshot(s), additional testing values are given in a chart along with the output values that they should produce. You can expect your instructor to grade your assignment by using all of these listed input values at the very least, but keep in mind that additional values may also be used as well. In other words, you should thoroughly test your code before submitting! 
 
Sample Output - Make sure your program can output data exactly as shown below. 
Enter House Number: 439 
Enter property depth (feet): 100 
Enter property width (feet): 50 
Enter type of grass (fescue, bentgrass, campus): fescue 
Enter the number of trees: 2 
Total cost for house 439 is: $1450.00 
"""
def landscape_calc():
    h=int(input('Enter house Number: '))
    d=int(input('Enter property depth in(feet)'))
    w=int(input('Enter property width in (feet)'))
    g=input('Enter types of grass(fescue,bentgrass,campus :)')
    t=int(input('Enter the number of trees'))
    b=1000
    add=0
    if d*w>5000:
        add=add+500
    if g=='fescue':
        add1=(d*w)*0.05
    elif g=='bentgrass':
        add1=(d*w)*0.02
    elif g=='campus':
        add1=(d*w)*0.01
    else:
        add1=b+0
    total=add1+add+b+t*100
    print('Total cost for house',h,'is :',total)
landscape_calc()
        
    

