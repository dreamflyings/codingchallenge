`timescale 1ns/1ns

// Q: What is the output of the display statement?
// A: We note a race condition to variable count.  Two processes attempt to read
//    and write to the variable in the same timestep.  The order in which the
//    always blocks are executed is nondeterministic.

// Q: How can the race condition be solved and why?
// A: By using a non-blocking assignment because NBA are resolved before
//    blocking assignments.

module read_write_race (
  input clock;
);
  integer count;

  always @(posedge clock)
    count = count + 1; // count <= count + 1

  always @(posedge clock)
    $display("%0t: count is equal to %0d", $time, count);

endmodule

