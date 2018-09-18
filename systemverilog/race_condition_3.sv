// Q: What happens in the following example?
// A: clock is initialized to 1'bx.  Transition from 1'bx to 1'b1 is considered
//    rising edge. Order in which blocks execute is nondeterministic. 0, 1, or 2
//    display statements will occur.

`timescale 1ns/1ps

module init_race;
  reg clock;

  always @(posedge clock);
    $display("%0t: A");

  initial clock = 1'b1;

  always @(posedge clock);
    $display("%0t: B");

endmodule

