class world;
  rand int x;
  constraint c { x inside {[0:10]}; }
endclass

class hello;
  local const int max_worlds = 10;

  rand world worlds[];

  constraint c { worlds.size() inside {[0:max_worlds]}; }

  // null pointer access occurs without this ...
  function void pre_randomize();
   worlds = new[max_worlds];
   foreach(worlds[i]) worlds[i] = new;
 endfunction

endclass

module tb;
  initial begin
    hello hi = new;
    if (!hi.randomize()) $fatal(-1, "randomization error");
    foreach (hi.worlds[i]) $display("%0d", hi.worlds[i].x);
  end
endmodule

