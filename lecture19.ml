(* Insertion Sort *)

(* You have l = h :: t. If t is sorted, can you use it to sort l? *)

let rec insert (x: int) (l: int list) : int list = 
  match l with
  | [] -> [x]
  | h :: t -> 
    match (x < h) with
    | true ->  x :: h :: t
    | false -> h :: (insert x t)
;;

let rec insertion_sort (l: int list) : int list = 
  match l with
  | [] -> []
  | h :: t -> insert h (insertion_sort t )
;;

(* 
   insertion_sort [6; 1; 20] 
-> insert 6 insertion_sort [1; 20] 
-> match (6 < 1) with
    | true ->  6 :: 1 :: [20]
    | false -> 1 :: (insert 6 [20])
-> so we get... 1 :: 6 :: [20]
*)
















(* Quick Sort *)


(* Let us make it slightly faster. Instead of recursing on the t, we can partition the tail into two parts: elements smaller than h, and elements equal to larger than h. Then we just sort those. *)



let rec filter (p: 'a -> bool) (l: 'a list) : 'a list = 
  match l with 
  | [] -> []
  | h :: t -> 
    match (p h) with
    | true -> h :: filter t
    | false -> filter t
;;

let rec quick_sort (l: int list) : int list = 
  match l with
  | [] -> []
  | h :: t -> quick_sort (filter (fun x -> x < h) l) @ quick_sort (filter (fun x -> x >= h) l)
;;

(* Can we chose something other than the head? What is the complexity? *)

(* Merge Sort *)

let rec split (l: int list) : (int list * int list) = 
  match l with
  | [] -> ([], [])
  | [x] -> ([x], [])
  | h1 :: h2 :: t -> let s = split t in (h1:: fst s, h2:: snd s)
;;

let rec merge (left: int list) (right : int list) : int list = 
  match left, right with
  | [], r -> r
  | l, [] -> l
  | l::ls, r::rs ->
    match (l <= r) with
    | true -> l :: (merge ls right)
    | false -> r :: (merge left rs)
;;

let rec merge_sort (l: int list): int list =
  match l with
  | [] -> []
  | [x] -> [x]
  | _ ->
      let (left, right) = split l in
      merge (merge_sort left) (merge_sort right)
;;