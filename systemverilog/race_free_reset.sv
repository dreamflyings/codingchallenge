`timescale 1ns/1ns

// Guidelines for avoiding race conditions:
//
// - initial and always blocks are exectued one after another, in any order
// - use continuous assignments to drive inout pins only, avoid using them to
//   model internal combinatorial functions, prefer sequential code in large
//   always block to several continuous assignments
// - use initializers to assign initial values, do not assign any value at time 0

module tb_top;
  reg clock; // reference clock only, do not use to drive logic

  reg clock_div_by_1;
  reg clock_div_by_2;

  // this guarantees values will be assigned before end of time 0, they will
  // also cause a negedge 1'bx->1'b0 transition during time 0, this is added
  // to queue
  initial #0 begin
    clock = 1'b0;
    clock_div_by_1 = 1'b0;
    clock_div_by_2 = 1'b0;
  end

  always #5 clock = ~clock;

  always @(clock) begin
    clock_div_by_1 <= clock;
    if (clock == 1'b1)
      clock_div_by_2 <= ~clock_div_by_2;
  end

  // Q: Does this clock and reset generator exhibit a race condition?  If so,
  //    how would it impact simulation?
  //
  // bit clock =0;
  // always #50 clk = ~clk;
  // bit reset = 0;
  // initial begin
  //   #150 reset = 1'b1; // race condition at 150, which block gets executed first?
  //   #200 reset = 1'b0; // .... and again at 350
  // end
  //
  // A: Race condition between clock and reset at 150, 350.  A block sensitive
  //    to the falling edge of clock may execute before or after reset is
  //    assigned.
  //
  // always @(negedge clock_div_by_1)
  //   if (sync_reset)
  //
  // Example:
  // t   clock rising falling reset comments
  // 0   0     n      n       0
  // 50  1     y      n       0
  // 150 0     n      y       1     race condition, if clock gets assigned first, no falling edge transition during this timestep
  // 200 1     y      n       1
  // 250 0     n      y       1
  // 300 1     y      n       1
  // 350 0     n      y       0     race condition: if clock gets assigned first, no falling edge transition during this timestep
  // 400 1     y      n       0

  // Q: Does this reset generator exhibit a race condition?  Is it the best
  //    way to generate synchronous reset? Why?
  //
  // logic sync_reset = 1'b0;
  // initial begin
  //   #150 sync_reset <= 1'b1;
  //   #350 sync_reset <= 1'b0;
  // end
  //
  // A1: No race condition. @150 sync_reset and clock are scheduled at beginning of
  //     timestep, reliably assigned for the NEXT time @(negedge clock_div_by_1) is
  //     triggered
  // A2: When sync_reset will go low is _not_ guaranteed.

  logic sync_reset = 1'b0;

  initial begin
    @(negedge clock_div_by_1); // clock_div_by_1 has guaranteed x->0 transition at time 0
    sync_reset <= 1'b1; // reliably assigned one delta-cycle after clock edge
    @(negedge clock_div_by_1); // t=10
    @(negedge clock_div_by_1); // t=20
    sync_reset <= 1'b0;
  end

  initial begin
    $dumpfile("dump.vcd");
    $dumpvars;
    $display("%0t: START", $time);
    #100;
    $display("%0t: END", $time);
    $finish;
  end

endmodule
