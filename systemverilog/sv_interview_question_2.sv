// SV Interview Question 2
// https://www.edaplayground.com/s/4/870

class widget;
  int id;
  bit to_remove;
endclass : widget

module top;
  widget q[$];

  initial begin
    widget w;
    int num = $urandom_range(20,40);
    for (int i = 0; i < num; i++) begin
      w = new;
      w.id = i;
      w.to_remove = $urandom_range(0,1);
      q.push_back(w);
      $display("widget id:%02d, to_remove:%b", q[$].id, q[$].to_remove);
    end

    // write SV code to remove entries in q[$] that have to_remove==1
    for (int i=q.size-1; i>=0; i--) // important: reverse loop
        if (q[i].to_remove)
          q.delete(i);

    // write SV code to check that no entry in q[$] has to_remove==1
    foreach (q[i]) assert(!q[i].to_remove) else $error("mismatch detected");
  end

endmodule

