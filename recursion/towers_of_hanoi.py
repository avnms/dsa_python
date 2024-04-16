def hanoi(num_disks, from_rod, to_rod, aux_rod):
    # Base case
    if num_disks >= 1:
        hanoi(num_disks - 1, from_rod, aux_rod, to_rod)
        print(f"Moving disk {num_disks} from rod {from_rod} to rod {to_rod}")
        hanoi(num_disks - 1, aux_rod, to_rod, from_rod)


if __name__ == "__main__":
    num_disks = 4
    source_rod = "A"
    target_rod = "C"
    auxiliar_rod = "B"

    hanoi(num_disks, source_rod, target_rod, auxiliar_rod)
