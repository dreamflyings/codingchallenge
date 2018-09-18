// SV Interview Question 3a
// https://www.edaplayground.com/s/4/960
//
// Answers:
// 1) 5 us; sub_run_b completes, then join occurs.
// 2) sub_run_a, sub_run_c; disable fork terminates all descendants of the
//    calling process, as well as their descendants.
// 3) encapsulate sub_run_b,sub_run_c and disable fork into its own fork
//    join block, make sure to use begin/end

// Task A. This task runs for 50us
task sub_run_a();
  while ($time < 50us) begin
    #1us;
    $display("sub_run_a(): ping at time %d", $time);
  end
endtask : sub_run_a

// Task B. This task runs for 5us
task sub_run_b();
  #5us;
  $display("sub_run_b() finished");
endtask : sub_run_b

// Task C. This task runs for 10us
task sub_run_c();
  #10us;
  $display("sub_run_c() finished");
endtask : sub_run_c

// You have the following task that forks off the tasks above.
// 1) assuming we start at time 0, how much time elapses before we reach "disable fork"
// 2) when we execute the "disable fork", which tasks get killed?
task run();

  fork
    sub_run_a();
  join_none

  fork // create separate process
  begin
    fork
      sub_run_b();
      sub_run_c();
    join_any

    $display("time before disable fork: %d", $time);

    disable fork; // now, this does not kill sub_run_a
  end
  join

  #10us;
endtask : run

module top;
  initial begin
    run();
  end
endmodule 

// 3) how do you prevent sub_run_a() task from getting killed in this scenario?

