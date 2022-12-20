"""DOES NOT WORK, DID NOT CONSIDER OUTPUT"""

def inputs() -> list[int]:
    always_false: bool = False
    return_list: list[int] = list()
    while always_false == False:
        try:
            initial_total_cost = int(input("What is the Fixed cost? "))
            return_list.append(initial_total_cost)
        except ValueError:
            print("Respond with a number.")
        try:
            avg_var_cost = int(input("What is the average variable cost? "))
            return_list.append(avg_var_cost)
        except ValueError:
            print("Respond with a number.")
        try:
            worker_num = int(input("How many workers? "))
            return_list.append(worker_num)
        except ValueError:
            print("Respond with a number.")
        return(return_list)

def main() -> None:
    input_list: list[int] = inputs()
    fixed_cost: int = input_list[0]
    avc: int = input_list[1]
    worker_count: int = input_list[2]
    final_list: list[int] = list()
    i = 0
    while i <= worker_count:
        if i != 0:
            final_list.append(fixed_cost/i)
            i += 1
            fixed_cost += avc
        else:
            i += 1
            fixed_cost += avc
    print(final_list)


if __name__ == "__main__":
    main()