// Q: Explain the operation of clocking block and discuss its impact on timing.
// A: The operation of a clocking block is counter intutitive. The key to understanding is the clocking block event and understanding that signals are sampled into the clocking block.
//
// Notes:
//
// Remember that the testbench clocking block operates in the reactive region.  If the TB drives cb.request at 100ns in the same timestep as @(cb), then request changed in design at 100ns (+ output delay, if applicable).
//
// Example, assume: positive clock edges / clocking events at 10, 20, 30
//
// initial begin
//   #2 cb.request  <= 3; // @ 2ns, request changes @10ns
//   #10 cb.request <= 2; // @ 12ns, request changes @20ns
//   #18 cb.request <= 2; // @ 30ns , request changes @30ns
// end
//
// References:
//
// https://www.verilab.com/files/SNUG_Austin_2012_paper51_presentation.pdf
// https://stackoverflow.com/questions/27758903/how-to-initialize-clocking-block-signals-at-resetmodule tb_top;
// https://www.doulos.com/downloads/events/DVCon_08_abstractBFM_final.pdf
// https://verificationacademy.com/forums/systemverilog/why-there-delay-one-clock-cycle-while-using-clocking-block

`timescale 1ns/1ns

module tb_top;
  logic clock;
  logic reset;
  logic request;
  logic grant;

  clocking cb @(posedge clock);
    output request_x = request;
    input grant_x = grant;
  endclocking

  // DUT
  reg [2:0] shift_reg;

  always @(posedge clock)
    if (reset)
      shift_reg <= 3'b0;
    else
      shift_reg <= {shift_reg[1:0], request};

  assign grant = shift_reg[2]; // request signal delayed by 8 cycles

  // Stimulus
  initial begin
    cb.request_x <= 1'b0;

    @(negedge reset); // 15ns

    @(cb); // 25ns
    cb.request_x <= 1'b1; // seen on waveform at 25ns

    // grant is driven by dut at 55ns, sampled by clocking block and available at 65ns

    while (!cb.grant_x) @(cb);
    cb.request_x <= 1'b0; // 65ns

    repeat (5) @(cb);

    $finish; // stopped at 115ns
  end

  // Clock and reset generation
  initial begin
    $dumpfile("dump.vcd");
    $dumpvars;
    clock = 0; // x->0
    reset = 1; // x->1
    repeat (4)
      #5 clock = !clock;
    reset = 0;
    forever
      #5 clock = !clock;
  end

endmodule

