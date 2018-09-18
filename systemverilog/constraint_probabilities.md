### Constraint Probabilities

- Bidirectional constraints

    - All constraints are active at the same time

    - SystemVerilog constraints are bidirectional.  The solver looks at both sides of the equation at the same time.

- List solutions for the following bidirectional constraints:

~~~systemverilog
rand bit [15:0] b, c, d;
constraint c_bidir {
  b < d;
  c == b;
  d < 30;
  c > 25;
}

// Ans:
// b < d
// c < d
// b == c
// d < 30
// c > 25
// b > 25
// 
// b > 25
// 25 < b
// b < d
// 25 < b < d < 30
// 25 < c < d < 30
// 
// b in { 26, 27, 28, 29 }
// c in { 26, 27, 28, 29 }
// d in { 26, 27, 28, 29 }
// 
// b   c   d
// 26, 26, 27
// 26, 26, 28
// 26, 26, 29
// 27, 27, 28
// 27, 27, 29
// 28, 28, 29
~~~

- Conditional constraints

    - Expression only active some of the time, use -> and if-else

    - List solution probabilities for the unconstrained case:

~~~systemverilog
class unconstrained;
  rand bit x; // 0 or 1
  rand bit [1:0] y; // 0, 1, 2, or 3
endclass

// Ans: each constraint has the same probability: 1/8
~~~

- Conditional constraints (cont'd)

    - List solution probabilities for the implication case

~~~systemverilog
class implication;
  rand bit x; // 0 or 1
  rand bit [1:0] y; // 0, 1, 2, or 3
  constraint c { (x==0) -> y == 0; }
endclass

// Ans:
//
// Solver recognizes there are eight combinations of x and y, but solutions
// where x==0 have been merged together.
//
// x y p
// 0 0 1/2
// 0 1 0
// 0 2 0
// 0 3 0
// 1 0 1/8
// 1 1 1/8
// 1 2 1/8
// 1 3 1/8
~~~

- Conditional constraints (cont'd)

    - Bidirectional and implication constraints

~~~systemverilog
class bidir_impli;
  rand bit x; // 0 or 1
  rand bit [1:0] y; // 0, 1, 2, or 3
  constraint c { y > 0; (x==0) -> y==0; }
endclass

// Ans:
// x y
// 0 0 illegal
// 0 1 -
// 0 2 -
// 0 3 -
// 1 0 illegal
// 1 1 1/3
// 1 2 1/3
// 1 3 1/3
~~~

