// SV Interview Question 4
// https://www.edaplayground.com/s/4/963
//
// Answers:
//
// 1) class_a, class_b; normal operation
// 2) class_b, class_b; b is downcast to a, print() is virtual function
// 3) class_b, class_b; see comments below
// 4) remove virtual from extended class
//    4.1) class_a, class_b; normal operation
//    4.2) class_b, class_b; base class still virtual
//    4.3) class_b, class_b; base class still virtual
// 5) remove virtual from both classes
//    5.1) class_a, class_b; normal operation
//    5.1) class_a, class_b; base class not virtual
//    5.1) class_a, class_b; base class not virtual
//          b = new;
//          a = b; // downcast ok
//          a2 = a; // a2=a=b
//          $cast(b2, a); // upcast b2 = a
//          a2.print();
//          b2.print();

class class_a;
  virtual function void print();
    $display("class_a");
  endfunction : print
endclass : class_a

class class_b extends class_a;
  virtual function void print(); 
    $display("class_b");
  endfunction : print
endclass : class_b

module top;
  initial begin

    // 1) what gets displayed for each print(), explain why
    $display("1");
    begin
      class_a a;
      class_b b;

      a = new;
      b = new;
      a.print(); // class_a
      b.print(); // class_b
    end

    // 2) what gets displayed for each print(), explain why
    $display("2");
    begin
      class_a a;
      class_b b;

      b = new;
      a = b; // b is downcast to a
      a.print(); // class_b
      b.print(); // class_b
    end

    // 3) what gets displayed for each print(), explain why
    $display("3");
    begin
      class_a a;
      class_a a2;
      class_b b;
      class_b b2;

      b = new;
      a = b; // b is downcast to a
      a2 = a; // a2 shares handle with a
      $cast(b2, a); // upcast, does not fail
      a2.print(); // class_b
      b2.print(); // class_b
    end

  end
endmodule

// 4) If we remove virtual from the extended class, how does that change things?
// 5) If we remove virtual from both classes, how does that change things?
