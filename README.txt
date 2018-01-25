This is one of the tools used in the Nonlinear Arithmetic
verification project: https://www.cs.washington.edu/node/14419

Run visualizer.py to launch an applet showing a SAT-solver in
action. Included are two traces of a SAT-solver proving that 
a certain type of grid problem is UNSAT.

Set "rectangular = True" to view visualize_4by8_rectangle_. 
This trace shows the execution of a modified SAT-
solver where the variable branching order has been fixed.

Set "rectangular = False" to view visualize_unmod_5to8. 
This trace shows the execution of an unmodified SAT-
solver. The problem is to show that a given "critical strip"
of a multiplier is unsatisfiable.

Each "step" shows a clause that has been learned by the solver. 
The green variables correspond to true literals and the magenta
variables correspond to false literals in the learned clause.

To learn more about where these SAT instances came from,
see: https://arxiv.org/pdf/1705.04302.pdf