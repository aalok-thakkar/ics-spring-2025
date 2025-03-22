(* Lecture 16, Mar 25 *)

(* A tail recursive function is one where the recursive call is the last operation performed. For example: *)

let rec gcd (a: int) (b: int) : int =
  match b with
  | 0 -> a
  | _ -> gcd b (a mod b)
;;

(* And then we have a for loop, which is a special kind of tail recursive function: *)

let factorial (n: int) : int =
  (* references *)
  let a = ref 1 in
  for i = 1 to n do
    (* assignments and deref. *)
    a := !a * i
  done;
  !a
;;

(* With references, dereferencing, and assignments *)

(* We prove correctness of a for loop using a loop invariant, a property of the state of the program that:

1. Holds before the loop starts.
2. Remains true after every iteration of the loop.
3. When the loop ends, it helps prove that the program produces the correct result. *)


let factorial (n: int) : int =
  let a = ref 1 in
  (* Loop Invariant: At the start of each iteration !a = factorial(i - 1) *)
  for i = 1 to n do
    a := !a * i;
  done;
  !a
;;

(* How would you do GCD? *)

let rec gcd (a: int) (b: int) : int =
  if b = 0 then a
  else gcd b (a mod b)
;;

(* While loop *)

let rec while_loop (condition: bool) (body: unit) =
  if condition then (
    body;
    while_loop condition body
  )
;;