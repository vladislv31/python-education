with open('even.txt', 'w') as f:
    for n in range(1, 101):
        if n % 2 == 0:
            f.write(f"{n}\n")

with open('even.txt', 'r') as f:
    lines = f.readlines()
    print(f"Lines count: {len(lines)}")
