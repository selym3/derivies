# derivies

## todo

* plot implicit equations

### parser/

* expression parser
* finish implementing scanner
* add proper checks for equal sign (gt and lt too)

### exp/

* solve for y'
* find roots with newton's method
* optimize creation of expression tree when deriv/exp is created (e.g. `a * 0`, `a * 1`, `a ^ 1`)
* operator overloading between expression for convenience
* add subclass of exp that handles chain rule (requires fixing cyclical imports?)
