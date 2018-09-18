`timescale 1ns/1ns

// Q: What is value of strobe at 10ns?
// A: Undefined, can be 0 or 1.

// Q: What will be displayed at 10ns?
// A: Undefined, depends whether the simulation squashes the previously
//    scheduled event.

module events;
  reg strobe;

  always @(strobe)
    $display("%0t: strobe is %b", $time, strobe);

  initial begin
    strobe = 1'b0;

    strobe <= #10 1'b0;
    strobe <= #10 1'b1;
  end

endmodule

