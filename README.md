# derivies

## todo

* plot implicit equations

### parser/

* add parsing for gt and lt
* add proper checks for repeated equal sign (gt and lt too)
* add support for identifiers (and maybe function calls)
* add support for exponents
* replace parser with shunting yard?

### exp/

* implement better exponentials

* less messy evaluation functions (visitor pattern)
* add subclass of exp that handles chain rule (requires fixing cyclical imports?)

* const term might be better as subclass of number?
* operator overloading between expression for convenience

* solve for y'
* optimize creation of expression tree when deriv/exp is created (e.g. `a * 0`, `a * 1`, `a ^ 1`)
