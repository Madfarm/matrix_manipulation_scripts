import cmath


def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter


def generate_ascii_art(width, height, x_min, x_max, y_min, y_max, max_iter):
    ascii_art = ''
    for py in range(height):
        line = ''
        for px in range(width):
            x = x_min + (x_max - x_min) * px / width
            y = y_min + (y_max - y_min) * py / height
            c = complex(x, y)
            m = mandelbrot(c, max_iter)
            line += '*' if m < max_iter else ' '
        ascii_art += line + '\n'
    return ascii_art


width = 80
height = 24
x_min = -2.0
x_max = 1.0
y_min = -1.0
y_max = 1.0
max_iter = 1000


ascii_art = generate_ascii_art(width, height, x_min, x_max, y_min, y_max, max_iter)


assert isinstance(ascii_art, str), "Output is not a string"
assert ascii_art.count('\n') == height, "Incorrect number of rows"
assert all(len(row) == width for row in ascii_art.split('\n')[:-1]), "Incorrect number of columns"


print(ascii_art)