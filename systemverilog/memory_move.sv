package tb_pkg;

  class memory_model#(int DEPTH=1024);
    typedef bit [$clog2(DEPTH)-1:0] addr_t;

    bit [7:0] mem[DEPTH];

    function new();
      for (int i=0; i<DEPTH; i++)
        mem[i] = i;
    endfunction

    function void move(addr_t from, addr_t to, int size);
      for (int i=size-1; i>=0; i--)
        mem[(to+i)%DEPTH] = mem[(from+i)%DEPTH];
    endfunction

    function void print();
      for (int i=0; i<DEPTH; i++)
        $display("mem[%0d]=%0d", i, mem[i]);
    endfunction
  endclass

endpackage

import tb_pkg::*;

module tb_top;
  initial begin
    memory_model#(8) mem = new;
    mem.print();
    mem.move(6, 0, 4);
    mem.print();
  end

endmodule

