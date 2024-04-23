import cmath

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def draw_mandelbrot(xmin,xmax,ymin,ymax,width,height,max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1,r2,[[mandelbrot(complex(r, i),max_iter) for r in r1] for i in r2])

def generate_ascii(mandelbrot_set):
    ascii_set = ''
    for row in mandelbrot_set[2]:
        for value in row:
            if value == max_iter:
                ascii_set += '*'
            else:
                ascii_set += ' '
        ascii_set += '\n'
    return ascii_set

import numpy as np

xmin,xmax,ymin,ymax = -2.0,1.0,-1.5,1.5
width,height,max_iter = 80,40,255

mandelbrot_set = draw_mandelbrot(xmin,xmax,ymin,ymax,width,height,max_iter)
ascii_set = generate_ascii(mandelbrot_set)

assert isinstance(ascii_set, str), "The output should be a string."
assert all(row.count('*') < len(row) for row in ascii_set.splitlines()), "The set is not correct."

print(ascii_set)