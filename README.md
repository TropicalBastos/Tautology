# Tautology
Create expressions and test whether they are logical tautologies


Usage:

And(var,var) = an and operator object

Or(var,var) = an or operator object

Not(var) = a not operator object

These objects construct an expression for example:

e = And(Or("x","y"),Or("y","x"))

And if we print it with print(e) we get:

"(x or y) and (y or x)"

And the method isTauto() tests whether the given object's expression string is evaluated to a tautology eg:

e.isTauto()

which returns False
