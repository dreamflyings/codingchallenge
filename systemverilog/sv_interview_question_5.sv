// SV Interview Question 5
// https://www.edaplayground.com/x/2a2

// Interview Question
// Fill in the code below

class my_sequencer;
  int id;
endclass : my_sequencer

class my_sequence;
  task start (my_sequencer seqr);
    int delay = $urandom_range(1,10);
    $display("time: %d, starting sequence on sequencer with id:%d", $time, seqr.id);
    #(delay * 1us);
    $display("time: %d, finishing sequence on sequencer with id:%d", $time, seqr.id);
  endtask : start
endclass : my_sequence


module top;
  initial begin
    my_sequencer seqr;
    my_sequencer seqr_q[$];
    static int num_of_seqr = $urandom_range(3,5);

    for (int i = 0; i < num_of_seqr; i++) begin
      seqr = new;
      seqr.id = i;
      seqr_q.push_back(seqr);
    end

    // write SV code to start a new instance of my_sequence on each of the sequencers in seqr_q
    // conditions:
    // 1) all sequences must start simultaneously (at time 0)
    // 2) code must wait until all sequences are finished before reaching "end" of initial block

    begin : solution
      semaphore sem = new(0);

      foreach (seqr_q[i]) begin
        fork
          automatic my_sequencer _seqr = seqr_q[i];
        begin
          my_sequence seq = new;
          seq.start(_seqr);
          sem.put(1); // does this need to be automatic?
        end
        join_none
      end

      sem.get(num_of_seqr);
    end : solution

   $display("time: %d, end reached", $time);
  end

endmodule

