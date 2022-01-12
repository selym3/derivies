import exp as e

def is_finished(measurement, target, epsilon):
    return abs(measurement-target)<=epsilon

def find_root(f, x0, digits, show_work):
    df = f.deriv()
    epsilon = 10**(-digits)

    print(f'{x0=}')
    while not is_finished(f.eval([x0]).value, 0, epsilon):
        fx = f.eval([x0]).value
        dx = df.eval([x0]).value
        x1 = x0 - fx/dx
        if show_work:
            print(f"x1 = {x0} - (f({x0})/f'({x0})) = {x0} - ({fx}/{dx}) = {x1}")
        x0 = x1
    
    return x0

if __name__ == "__main__":
    f = e.sub(e.pow(e.x(), e.const(2)), e.const(30))
    print(f)
    root = find_root(f, x0=3, digits=8, show_work=True)
    print("final root:", root) 