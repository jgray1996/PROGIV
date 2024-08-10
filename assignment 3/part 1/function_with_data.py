def run_function(data, *funcs):
    return [[func(x) for x in data] for func in funcs]

sequence = [1,2,3,4,5,6]

double = lambda x: x*2
square = lambda x: x**2
invert = lambda x: x*-1

functions = [double, square, invert]

print(run_function(sequence, *functions))