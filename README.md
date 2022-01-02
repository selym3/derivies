# derivies

## todo

* plot implicit equations
* solver for certain terms? (e.g. y' when doing implicit)
* algebraic simplifier -> optimize creation of expression tree when deriv/exp is created (e.g. `a * 0`, `a * 1`, `a ^ 1`)

### parse/

* add a type system for functions (const vs function)?
* add better errors
* add graphing function

### exp/

* implement better exponentials

* const term might be better as subclass of number? or with useful operators
* ability to subclass const for irration terms like `pi` and `e`
* operator overloading between expression for convenience
