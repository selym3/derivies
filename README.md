# derivies

## todo

* solver for certain terms? (e.g. y' when doing implicit)
* algebraic simplifier -> optimize creation of expression tree when deriv/exp is created (e.g. `a * 0`, `a * 1`, `a ^ 1`)
* exp -> latex string function

### graph/

* fix line rasterization (it's bad)
* figure out where stuff is getting flipped for squares (`get_segments(...)`) (position order? screen conversions?)
* use interpolation on marching square sides
* multithreading? + share corner data
* upgrade to quadtree subdivision
* implement some interval arithmetic

### parse/

* add a type system for functions (const vs function)?
* add better errors
* add graphing function

### exp/

* **implement better exponentials**
* ability to subclass const for irration terms like `pi` and `e`
* const term might be better as subclass of number? or with useful operators
* operator overloading between expression for convenience
