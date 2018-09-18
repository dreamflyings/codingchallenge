package tb_pkg;

typedef struct {
  bit [5:0] ingress_port;
  bit [5:0] egress_port;
  bit [3:0] padding;
  bit [16:0] payload;
} packet_t;

class switch_scoreboard;
  int num_ingress_ports;
  int num_egress_ports;

  packet_t packet_queue[][$];

  function new(int num_ingress_ports, int num_egress_ports);
    assert(num_ingress_ports > 0 && num_ingress_ports < 32) else $fatal(-1, "invalid number of ingress ports");
    assert(num_egress_ports > 0 && num_egress_ports < 32) else $fatal(-1, "invalid number of egress ports");

    this.num_ingress_ports = num_ingress_ports;
    this.num_egress_ports = num_egress_ports;
    this.packet_queue = new[num_egress_ports];
  endfunction : new

  function void receive_ingress(packet_t packet);
    packet_queue[packet.dest_port].push_back(packet);
  endfunction

  function void receive_egress(packet_t actual, int egress_port);
    packet_t expected = packet_queue[egress_port].pop_front();
    assert(actual == expected) else $error("mismatch detected");
  endfunction

endclass : switch_scoreboard

endpackage : tb_pkg

import tb_pkg::*;

module tb_top;
  initial begin
    switch_scoreboard scoreboard = new(4, 4);
    packet_t packet = '{ingress_port: 0, egress_port: 1, padding: 0, payload: 16'hABCD};

    scoreboard.receive_ingress(packet);
    scoreboard.receive_egress(packet, 1);
  end

endmodule

