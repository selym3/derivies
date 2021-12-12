# derivies

## todo

* plot implicit equations

### parse/

* add a type system for functions (const vs function)?
* add better errors
* add graphing function

### exp/

* implement better exponentials

* less messy evaluation functions (visitor pattern)
* add subclass of exp that handles chain rule (requires fixing cyclical imports?)

* const term might be better as subclass of number?
* operator overloading between expression for convenience

* solve for y'
* optimize creation of expression tree when deriv/exp is created (e.g. `a * 0`, `a * 1`, `a ^ 1`)
