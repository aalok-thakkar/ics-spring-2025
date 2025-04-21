(* Quick Sort *)

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


(* How do you force the best case of quicksort? *)

(* Find median in linear time! *)

let rec group5 (xs : 'a list) : 'a list list =
  match xs with
  | [] -> []
  | _ ->
    let g = take 5 xs in
    let rest = drop 5 xs in
    g :: group5 rest

let rec partition3 (pivot : int) (xs : int list) : int list * int list * int list =
  match xs with
  | [] -> ([], [], [])
  | hd :: tl ->
    let (lt, eq, gt) = partition3 pivot tl in
    match compare hd pivot with
    | n when n < 0 -> (hd :: lt, eq, gt)
    | 0 -> (lt, hd :: eq, gt)
    | _ -> (lt, eq, hd :: gt)

let rec select (xs : int list) (k : int) : int =
  match xs with
  | [] -> failwith "Empty list"
  | [x] -> x
  | _ ->
    let groups = group5 xs in
    let medians = 
      let rec get_meds (gs : int list list) : int list =
        match gs with
        | [] -> []
        | g :: rest ->
          let sorted = sort g in
          let mid = length sorted / 2 in
          nth sorted mid :: get_meds rest
      in
      get_meds groups
    in
    let pivot = select medians (length medians / 2) in
    let (lt, eq, gt) = partition3 pivot xs in
    let len_lt = length lt in
    let len_eq = length eq in
    match compare k len_lt with
    | n when n < 0 -> select lt k
    | 0 when k < len_lt + len_eq -> pivot
    | _ -> select gt (k - len_lt - len_eq)

let median (xs : int list) : int =
  let n = length xs in
  match n mod 2 with
  | 1 -> select xs (n / 2)
  | _ ->
    let a = select xs (n / 2 - 1) in
    let b = select xs (n / 2) in
    (a + b) / 2

(* Do I really need this? *)


(* How do I merge two sorted lists? *)

(* [3, 6, 19] and [4, 5, 55] *)

let rec merge (l1 : int list) (l2: int list) : int list = 
  match l1 with
  | [] -> l2
  | h1 :: t1 -> 
    match l2 with
    | [] -> l1
    | h2 :: t2 ->
      match (h1 < h2) with
      | true -> h1 :: h2 :: merge t1 l2
      | false -> h2 :: h1 :: merge l1 t2
;;

let rec split (l : int list) : (int list * int list) = 
  match l with 
  | [] -> ([], [])
  | [x] -> ([x], [])
  | x1 :: x2 :: xs -> let (left, right) = split xs in (x1 :: left, x2 :: right)
;;
 
let rec mergesort (l : int list) : int list = 
  match l with 
  | [] -> []
  | _ -> let (left, right) = split l in merge (merge_sort left) (merge_sort right)
;;


  (* split the list into two *)
  (* mergesort both parts *)
  (* merge them *)