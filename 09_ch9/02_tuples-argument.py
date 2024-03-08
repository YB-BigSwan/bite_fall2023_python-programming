def main():
    p = ("Hawks", "Jennifer", 10)
    print_player(p)

def print_player(tup):
    t1, t2, t3 = tup
    print(f"{t2} ({t1}), {t3} goals")

main()