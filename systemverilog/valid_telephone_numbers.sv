/*

Valid combinations
0
1
[2-9]11
1 areacode 453 5794
011-countrycode-


areacode
[2-9]xx









*/


class telephone_number;
  rand int num_digits; // parent constraint

  rand int digits[]; // child constraint

  constraint digits_c {
    num_digits inside {1, 3, 7, 10, 11};
    digits.size() == num_digits;
  }

  constraint trunk_prefix_c {
    (num_digits != 11) -> digits[0] != 1;
  }

  constraint operator_c {
    if (num_digits == 1) {
      digits[0] == 0;
    }
    else if(num_digits == 11) {
      digits[0] == 1;
    }
    else {
      digits[0] != 0;
    }
  }

  constraint special_number_c {
    if (num_digits == 3) {
      digits[0] != 0;
      digits[1] == 1;
      digits[2] == 1;
    }

    if (num_digits > 3) {
      digits[1] != 1;
      digits[2] != 1;
    }
  }

  function new();
  endfunction

  function string to_string();
    bit [0:11+1][7:0] s;
    foreach (digits[i]) begin
      string t;
      t.itoa(digits[i]);
      s[i] = t;
      s[i+1] = "\0";
    end
    return string'(s);
  endfunction

endclass

module tb;
  initial begin
    telephone_number num;
    telephone_number nums[];

    num = new;
    if (!num.randomize() with { num_digits == 1; })
      $fatal(1, "error randomizing object with num_digits == 1");
    $display(num.to_string);

    num = new;
    if (!num.randomize() with { num_digits == 3; })
      $fatal(1, "error randomizing object with num_digits == 3");
    $display(num.to_string);

    num = new;
    if (!num.randomize() with { num_digits == 7; })
      $fatal(1, "error randomizing object with num_digits == 7");
    $display(num.to_string);

    num = new;
    if (!num.randomize() with { num_digits == 10; })
      $fatal(1, "error randomizing object with num_digits == 10");
    $display(num.to_string);

    num = new;
    if (!num.randomize() with { num_digits == 11; })
      $fatal(1, "error randomizing object with num_digits == 11");
    $display(num.to_string);DD    

    nums = new[10];
    foreach (nums[i]) begin
      nums[i] = new;
      if (!nums[i].randomize())
        $fatal(1, "error randomizing object");
      $display(nums[i].to_string());
    end

    $finish;
  end

endmodule

