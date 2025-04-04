
(*   if (List.length v1) <> (len2 = List.length v2) then failwith "Matrices must have appropriate dimensions"; *)



(* Pointers reveal how computers actually work under the hood:

   1. Memory as a Giant Array:
      - Physical memory is conceptually one continuous block of bytes
      - Each byte has a unique numeric address
      - Pointers store these addresses

      Visual Representation:
      +--------+--------+--------+--------+
      | 0x0000 | 0x0001 | 0x0002 |  ...   |
      +--------+--------+--------+--------+
      |        |        |        |        |
      +--------+--------+--------+--------+

   2. Variables as Named Memory:
      - Variables are human-readable names for memory addresses
      - The compiler translates names to addresses

      Example:
      let x = 42 in
      The compiler might assign address 0x1234 to 'x'

      This can be achieved by using a pointer. A pointer combines optional type (for null) with reference (for mutability).
*)
type 'a pointer = 'a ref option

let null : 'a pointer = None

let malloc (x : 'a) : 'a pointer = Some (ref x)





(* Create a value and its pointer *)
let value = 42
let ptr = malloc value

(* 
   Memory Layout After Execution:

   Stack (fast, fixed-size)       Heap (flexible, dynamic)
   +-------------------+          +-------------------+
   | value: 42         |          | ref cell          |
   | (address: 0x1000) |          | (address: 0x2000) |
   +-------------------+          +-------------------+
   | ptr: 0x2000       |          | contents: 42      |
   | (address: 0x1008) |          +-------------------+
   +-------------------+

   Key Observations:
   - 'value' is stored on the stack at address 0x1000
   - The reference cell is on the heap at address 0x2000
   - 'ptr' contains the address 0x2000 (points to the heap)
*)



exception SegmentationFault
let deref (ptr : 'a pointer) : 'a =
  match ptr with
  | None -> raise SegmentationFault
  | Some r -> !r
;;

let assign (ptr : 'a pointer) (x : 'a) : unit =
  match ptr with
  | None -> raise SegmentationFault
  | Some r -> r := x
;;











(* 
   WARNING: This is just for educational purposes!
   Real OCaml programs shouldn't rely on actual addresses.
*)

let address (ptr : 'a pointer) : int =
  match ptr with
  | None -> 0
  | Some r -> Obj.magic (Obj.repr r)

let print_memory_layout () =
  let ptr_address = address ptr in
  Printf.printf "Variable 'ptr' points to address: 0x%X\n" ptr_address;
  match ptr with
  | None -> ()
  | Some r -> 
    let value_address = address (Some r) in
    Printf.printf "Reference cell at: 0x%X\n" value_address;
    Printf.printf "Stored value: %d\n" (deref ptr)

(* 
   Example output might look like:
   Variable 'ptr' points to address: 0x2000
   Reference cell at: 0x2000
   Stored value: 42

   (Note: Actual addresses will vary and aren't meaningful in OCaml)

   The pointer system we've built mirrors how CPUs actually work:
   - Every access is ultimately via memory addresses
   - Higher-level languages add safety layers on top
   - Understanding this helps debug complex systems
*)







