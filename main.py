"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def subquadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _subquadratic_multiply(x,y).decimal_val


# Using equations 7 and 8 in the slides we see that (xl+xr) * (yl+yr) = (xl*yl) + (xl*yr) + (xr*yl) + (xr*yr) and (xl*yr) + (xr*yl) = (xl+xr) * (yl+yr) - (xl*yl) - (xr*yr)
# this means (xl+xr) * (yl+yr) = (xl*yl) + (xl+xr) * (yl+yr) - (xl*yl) - (xr*yr) + (xr*yr), this way so we only use 3 multiplications instead of 4 like we did in recitation 3
def _subquadratic_multiply(x, y):
    #base cases, if either x or y <= 1, just return their product
    if ((x.decimal_val <= 1) or (y.decimal_val  <= 1)):
        return BinaryNumber(x.decimal_val*y.decimal_val)
    #recursive case
    else: 
        #obtain xvec and yvec, the binary_vec values of x and y
        xvec = x.binary_vec
        yvec = y.binary_vec
        #pad xvec and yec so they are the same length and update the variables
        xvec = pad(xvec, yvec)[0]
        yvec = pad(xvec, yvec)[1]
        #split xvec and yvec into two halves
        x_left = split_number(xvec)[0]
        x_right = split_number(xvec)[1]
        y_left = split_number(yvec)[0]
        y_right = split_number(yvec)[1]
        '''
        I will now find the three products in the given formula
        I then plug these values into the formula.
        the formula has three terms the first term needs to be shifted 2^n and the second term needs to be shifted 2^n/2
        '''
        first_product = _subquadratic_multiply(x_left, y_left)
        second_product = _subquadratic_multiply(x_right, y_right)
        third_product = _subquadratic_multiply(BinaryNumber(x_left.decimal_val + x_right.decimal_val), BinaryNumber(y_left.decimal_val + y_right.decimal_val))
        second_term = BinaryNumber(third_product.decimal_val - first_product.decimal_val - second_product.decimal_val)

        return BinaryNumber(bit_shift(first_product, len(xvec)).decimal_val + bit_shift(second_term, len(xvec)//2).decimal_val + second_product.decimal_val)
    


def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000

print(time_multiply(BinaryNumber(2),BinaryNumber(1),subquadratic_multiply))
print(time_multiply(BinaryNumber(2),BinaryNumber(10),subquadratic_multiply))
print(time_multiply(BinaryNumber(2),BinaryNumber(100),subquadratic_multiply))
print(time_multiply(BinaryNumber(2),BinaryNumber(1000),subquadratic_multiply))
print(time_multiply(BinaryNumber(2),BinaryNumber(10000),subquadratic_multiply))
print(time_multiply(BinaryNumber(2),BinaryNumber(100000),subquadratic_multiply))






    

