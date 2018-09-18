package tb_pkg;
  typedef bit [31:0] addr_t;
  typedef bit [31:0] data_t;

  class MemoryModel;
    bit [7:0] sparse_mem[bit [7:0]];

    function bit [7:0] read_byte(addr_t addr);
      return (!sparse_mem.exists(addr)) ? $urandom_range(0, 255) : sparse_mem[addr];
    endfunction

    function void write_byte(addr_t addr, bit [7:0] data);
      sparse_mem[addr] = data;
    endfunction

    function data_t read(addr_t addr);
      data_t data;
      assert(addr[2:0] == 0) else $fatal(-1, "unaligned read address");
      for (int b=0; b<4; b++) data[7+8*b -: 8] = read_byte(addr | b);
      return data;
    endfunction

    function void write(addr_t addr, data_t data);
      assert(addr[2:0] == 0) else $fatal(-1, "unaligned write address");
      for (int b=0; b<4; b++) write_byte(addr | b, data[7+8*b -: 8]);
    endfunction

    function void move(addr_t src_addr, addr_t dest_addr);
      data_t tmp_data;
      assert(dest_addr[2:0] == 0) else $fatal(-1, "unaligned source address");
      assert(src_addr[2:0] == 0) else $fatal(-1, "unaligned destination address");
      tmp_data = read(src_addr);
      write(dest_addr, tmp_data);
    endfunction

  endclass
endpackage

import tb_pkg::*;

module tb_top;
  initial begin
    MemoryModel mem_model = new;
    addr_t addr = 32'h0000_0080;
    data_t data = $urandom;
    mem_model.write(addr, data);
    assert(mem_model.read(addr) == data) else $error("mismatch detected");
    mem_model.move(addr, addr + 8);
    assert(mem_model.read(addr + 8) == data) else $error("mismatch detected");
  end

endmodule
