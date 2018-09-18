- Explain dfferences between `always`, `always_comb`, `always_ff`, and
  `always_latch`
  - `always @*`: Used to infer sensitivity lists for combinational logic
    blocks.  Does not infer complete sensitivity list when block contains
    functions. TL;DR don't use.
  - `always_comb`: Similar to above, it is used to infer sensitity list for the
    block.  It also is sensitive to changes within functions. The block is
    automatically executed once at time 0. The block cannot have blocking timing,
    event controls, or fork-join statements.
    *Gotcha*:
    ~~~~
    always_comb begin
    b = a;
    c = a; // c = a
    end
    always_comb begin
    c = b; // c = previous value of a
    b = a; // changing b does not retrigger the always_comb during the timestep
    end
    ~~~~
  - `always_ff`: Used to model sequential logic.  There can be only a single
    event control (i.e. `@(posedge clock)`) and no blocking controls.  Tools
    can implement lint behavior.
  - `always_latch`:  Used to model latches.  Identical rules to `always_comb`.

##### Reference
https://www.verilogpro.com/systemverilog-always_comb-always_ff/
