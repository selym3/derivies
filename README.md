# derivies

## todo

* solver for certain terms? (e.g. y' when doing implicit)
* algebraic simplifier -> optimize creation of expression tree when deriv/exp is created (e.g. `a * 0`, `a * 1`, `a ^ 1`)
* exp -> latex string function
* imports are kinda messed up in `graph/`

### graph/

* fix line rasterization (it's bad)
* figure out where stuff is getting flipped for squares (`get_segments(...)`) (position order? screen conversions?)
* use interpolation on marching square sides
* multithreading? + share corner data
* upgrade to quadtree subdivision
* implement some interval arithmetic

### parse/

* add unary operators and real negation
* add a type system for functions (const vs function)?
* add better errors
* add graphing function

### exp/

* `constpow` exists in `expr/ops.py` because of circular import with `exp.py`
* make sure exponentials are wokring
* ability to subclass const for irrational terms like `pi` and `e`
* const term might be better as subclass of number? or with useful operators
* operator overloading between expression for convenience
