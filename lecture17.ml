(* Lecture 17, Mar 28 *)


(* A tail recursive function is one where the recursive call is the last operation performed. For example: *)

let rec gcd (a: int) (b: int) : int =
  match b with
  | 0 -> a
  | _ -> gcd b (a mod b)
;;

(* Correctness of gcd: 

Case I: a > b
  Inductive Hypothesis: for all m < b, and for all n: 
      let gcd n m = the greatest common divisor of n and m.

  Inductive Step:
  gcd a b = gcd b (a mod b). But by assumption + since (a mod b) < b. Hence, by inductive hypothesis, 
    gcd b (a mod b) is correctly computed. 

    There exists r = gcd a b
    Then: 
      (i) a = p.r
      (ii) b = q.r

      Lemma: 
      r = gcd a b 
        = gcd (p.r) (q.r) 
        = r.(gcd p q) 
        = r. (gcd q (p mod q))

        When they are co-prime, why is:
          gcd a b = gcd b (a mod b)? 

          Let a = qb + r
          Where r < b.
          Then a mod b = r.

          gcd a b = gcd (qb + r) (b) = gcd r b = gcd b r = gcd b (a mod b). 


Case III: a < b??



Proof by Induction on b:
  Base Case: b = 0. Line 8 by definition... 

  Inductive Hypothesis: 
  
  For all n, 
        gcd (b, n) = gcd(n, b mod n)? 


  Consider n = a mod b. Then, for all b,  gcd (b, n) = gcd (n, b mod n). 


  Inductive Step: ...


*)


(* Recall that here you do not know the number of times you need to update the state. 
   For this, we introduced the while loop: *)

let rec while_loop (condition: bool) (body: unit) =
  if condition then (
    body;
    while_loop condition body
  )
;;

(* GCD can be implemented using the while loop as follows: *)

let gcd_while (a: int) (b: int) : int =
  let x = ref a in
  let y = ref b in
  while !y <> 0 do
    let temp = !y in
    y := !x mod !y;
    x := temp
  done;
  !x
;;

(* We can decorate this code with assertions and ghost variables to prove correctness: *)

let gcd_while (a: int) (b: int) : int =
  
  let x = ref a in
  let y = ref b in
  while !y <> 0 do
    (* Loop invariant: gcd(!x, !y) = gcd(a, b) *)
    assert(gcd !x !y = gcd a b);
    
    let temp = !y in
    y := !x mod !y;
    x := temp;
  done;

  (* Loop invariant: *)
  assert(gcd !x !y = gcd a b);

  (* Negation of loop condition: *)
  assert(!y = 0);
  
  (* Post-condition: result is GCD of original inputs, follows from loop invariant and the negation of loop condition *)
  assert(!x = gcd a b);
  
  !x
;;

(* 
  Correctness proof outline:
  1. Initialization: 
     - Before loop, x=a, y=b
     - gcd(a,b) = gcd(a,b) holds trivially
  2. Maintenance:
     - At each iteration, gcd(x,y) = gcd(old_x, old_y)
     - Because gcd(x,y) = gcd(y, x mod y)
  3. Termination:
     - When y=0, gcd(x,0) = x
     - By invariant, x = gcd(a, b)
*)

(* Is Prime? *)

let is_prime (n: int) : bool =
  if n < 2 then false
  else
    let i = ref 2 in
    let has_divisor = ref false in
    while !i * !i <= n && not !has_divisor do
      (* Invariant: 
          all j < i, n mod j <> 0 IMPLIES has_divisor = false
          if there is j < i, n mod j = 0 IMPLIES has_divisor = true *)
      if n mod !i = 0 then has_divisor := true;
      i := !i + 1
    done;
    not !has_divisor
;;

let () = Printf.printf "%b\n" (is_prime 97);;  (* Should print true *)
let () = Printf.printf "%b\n" (is_prime 100);; (* Should print false *)

(* What would be the loop invariants? *)


(* Try to count the number of steps in Collatz Conjecture *)

let rec collatz (n: int) : int =
  if n = 1 then 0
  else if n mod 2 = 0 then 1 + collatz (n / 2)
  else 1 + collatz (3 * n + 1)
;;








let collatz_loop (n: int) : int =
  let num = ref n in
  let steps = ref 0 in
  while !num <> 1 do
    (* Invariant: 
        !steps = number of collatz steps required to get from n to !num *)
    assert(!steps = collatz(n) - collatz(!num)); 

    if !num mod 2 = 0 then
      num := !num / 2
    else
      num := 3 * !num + 1;
    steps := !steps + 1
  done;

  (* From loop condition: !num = 1 *)
  (* From loop invariant: !steps = number of collatz steps required to get from n to !num *)

  (* Therefore, !steps = number of collatz steps required to get from n to 1. *)

  assert(!steps = collatz(n)); 

  !steps
;;






(* Nested Loops *)


let print_grid (n: int) (m: int) =
  for i = 1 to n do
    for j = i to 2*i do
      Printf.printf "(%d,%d) " i j
    done;
    print_newline ()
  done
;;


(* Example usage *)
(* print_grid 3 4;; *)












(* Matrix Multiplication *)

(* This has one mistake *)
let dot_product (v1: int list) (v2: int list) : int =
  let sum = ref 0 in
  let len = List.length v1 in
  for i = 0 to len - 1 do
    sum := !sum + (List.nth v1 i * List.nth v2 i)
  done;
  !sum
;;

(* Get the i-th row of a matrix *)
let get_row (matrix: int list list) (i: int) : int list =
  List.nth matrix i
;;

(* Get the j-th column of a matrix *)
let get_column (matrix: int list list) (j: int) : int list =
  let col = ref [] in
  for i = 0 to (List.length matrix) - 1 do
    col := !col @ [List.nth (List.nth matrix i) j]
  done;
  !col
;;

(* Multiply two matrices *)
let matrix_multiply (a: int list list) (b: int list list) : int list list =
  let n = List.length a in 
  let m = List.length (List.hd b) in
  let result = ref [] in

  for i = 0 to n - 1 do
    let row_result = ref [] in
    for j = 0 to m - 1 do
      let row = get_row a i in
      let column = get_column b j in
      row_result := !row_result @ [dot_product row column];
    done;
    result := !result @ [!row_result];
  done;

  !result
;;

(* Concatenate takes a lot of time. How to do it without concatenate? *)
(* One way is to use While Loops! *)






(* The other is: *)

let test_foo : unit =  
  for i = 5 downto 1 do
    print_int i; print_newline ();
  done;
;;

