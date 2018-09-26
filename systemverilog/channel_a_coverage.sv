// not following UVM guidelines ...

/*
data_w | mask_w data_width/8
8        1
16       2
32       4
64       8
128      16
256      32

size_w |  size values |  number of bytes          | log(2) number of bytes
4      |  0-3         |  1,2,4 8                  | 0,1,2,3
8      |  0-255       |  1,2,4,8,16,32,64,128,256 | 0,1,2,3,4,5,6,7
*/


`define NUM_MASTERS 16
`define SOURCE_W 4
`define SIZE_W 4
`define ADDR_W 8
`define DATA_W 8
`define MASK_W 2

class channel_a_item;
  bit [2:0] a_opcode;
  bit [2:0] a_param;
  bit [`SIZE_W-1:0] a_size;
  bit [`SOURCE_W-1:0] a_source;
  bit [`ADDR_W-1:0] a_address;
  bit [`MASK_W-1:0] a_mask;
  bit [`DATA_W-1:0] a_data;

  function new();
  endfunction
endclass

class channel_a_coverage;
  channel_a_item m_item;

  // there is no "good" way to parameterize a covergroup
  covergroup covgroup(int size_w=`SIZE_W, int data_w=`DATA_W, int addr_w=`ADDR_W);
    option.per_instance = 0;

    opcode : coverpoint m_item.a_opcode {
      bins get = {4};
      bins put_full = {0};
      bins put_partial = {1};
    }

    param : coverpoint m_item.a_param {
      bins reserved = {0};
    }

    size : coverpoint m_item.a_size {
      bins zero = {0};
      bins max = {(2**`SIZE_W)-1};
      bins others[] = default;
    }

    source_cp : coverpoint m_item.a_source {
      bins zero = {0};
      bins max = {(2**`SOURCE_W)-1};
      bins others[] = default;
    }

    // again, no "good" way to parameterize a coverpoint
    address_cp : coverpoint m_item.a_address {
      // power of two range coverage
      bins powers_of_two[] = {
        8'b00000001, // [1]       <-- lowest probability to generate
        8'b0000001?, // [3:2]
        8'b000001??, // [7:4]
        8'b00001???, // [15:8]
        8'b0001????,
        8'b001?????,
        8'b01??????,
        8'b1???????  // [255,128] <-- highest probability to generate
      };
      // alignment coverage, address % N == 0 // FIXME: does non-power-of-two N matter?
      bins align_4_byte  = {8'b??????00};
      bins align_8_byte  = {8'b?????000};
      bins align_16_byte = {8'b????0000};
      // [..]
    }

    mask_cp : coverpoint m_item.a_mask {
      bins zero = {0};
      bins max = {(2**`MASK_W)-1};
      bins others[] = default;
    }

    data_cp : coverpoint m_item.a_data {
      // FIXME: syntax
      bins toggle_0_to_1[] = {
        8'b????_???0 => 8'b????_???1,
        8'b????_??0? => 8'b????_??1?,
        8'b????_?0?? => 8'b????_?1??,
        8'b????_0??? => 8'b????_1???,
        8'b???0_???? => 8'b???1_????,
        8'b??0?_???? => 8'b??1?_????,
        8'b?0??_???? => 8'b?1??_????,
        8'b0???_???? => 8'b1???_????
      };

      // FIXME: syntax
      bins toggle_1_to_0[] = {
        8'b????_???1 => 8'b????_???0
        8'b????_??1? => 8'b????_??0?
        8'b????_?1?? => 8'b????_?0??
        8'b????_1??? => 8'b????_0???
        8'b???1_???? => 8'b???0_????
        8'b??1?_???? => 8'b??0?_????
        8'b?1??_???? => 8'b?0??_????
        8'b1???_???? => 8'b0???_????
      };
    }

  endgroup

  function new();
    covgroup = new;
  endfunction

  function void write(channel_a_item item);
    m_item = item;
    channel_a_cov.sample();
  endfunction
endclass

module tb;
  initial begin
  channel_a_coverage coverage = new;
  channel_a_item  item = new;
  coverage.write(item);
endmodule
