module nested_data_structs;
  
  // associative array of dynamic arrays
  initial begin
    int x[string][];
    x["hello"] = new[2];
    x["hello"][1] = 2;
  end

  // dynamic array _of_ associative arrays
  initial begin
    int x[][string];
    x = new[2];
    x[0]["hello"] = 1234;
    x[1]["world"] = 5678;
    //x[9]["hello"] = 9; // out of bounds, detected at run time
  end
  
  // fixed array _of_ associative arrays
  initial begin
    int x[2][string];
    x[0]["hello"] = 1234;
    x[1]["world"] = 5678;
    //x[9]["hello"] = 9; // out of bounds, detected at compile time    
  end
  
  // dynamic array _of_ smart queues
  initial begin
    int x[][$];
    x = new[2];
    x[0].push_back(2);
    x[1].push_back(3);    
  end
  
  // 2D dynamic array
  initial begin
    int num_rows = 2;
    int num_cols = 3;
    int m[][];
    m = new[num_rows];    
    foreach (m[i])
      m[i] = new[num_cols];
    //m[1][3] = 9; // out of bounds, detected at run time
    m[num_rows-1][num_cols-1] = 9;
  end

  // 3D dynamic array
  initial begin
    int num_rows = 2;
    int num_cols = 3;
    int num_deep = 4;
    int m[][][];
    m = new[num_rows];    
    foreach (m[i]) begin
      m[i] = new[num_cols];
      foreach (m[i,j])
        m[i][j] = new[num_deep];
    end
       
    m[num_rows-1][num_cols-1][num_deep-1] = 9;      
  end
  
  // pass dynamic array by reference and value
  function automatic void dyn_arr_by_ref(ref int z[]);
     z[0] = 9;
    $display(z[0]);
  endfunction

  function void dyn_arr_by_val(int z[]);
    z[0] = 8;
    $display(z[0]);
  endfunction

  initial begin
    int a[] = new[1];
    int b[] = new[1];
    
    dyn_arr_by_ref(a); // 9
    $display(a[0]); // 9
    
    dyn_arr_by_val(b); // 8
    $display(b[0]); // 0  
  end
 
endmodule
