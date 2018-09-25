class cam_scoreboard;
  int mem[];
  int size;

  function new(int size);
    this.mem = new[size];
    this.size = size;
  endfunction

  function void write(int addr, int data);
    if (addr < 0 || addr >= size)
      $fatal(1, "illegal address on write");
    mem[addr] = data;
  endfunction

  function int search(int data);
    int q[$] = mem.find_index with (item == data);
    foreach (q[i])
      if (mem[q[i]] == data)
        return q[i];
    return -1;
  endfunction

endclass

module tb;
  initial begin
    cam_scoreboard scbd = new(10);

    for (int i=0; i<10; i++) begin
      scbd.write(i, 10+i);
      if (scbd.search(10+i) != i)
        $fatal(1, "scoreboard error");
    end
    $finish;
  end

endmodule

