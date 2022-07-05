def generate_line(symbol, n, offset_count = 0):
    offset = ' ' * offset_count
    content = (symbol + ' ') * n
    return f"{offset}{content}"

def show_line(symbol, n, offset = 0):
    print(generate_line(symbol, n, offset))

def draw_rhombus(n, symbol="*"):
    for i in range(n):
        show_line(symbol, (i + 1), (n - i - 1))

    for i in range(n - 2, -1, -1):
        show_line(symbol, (i + 1), (n - i - 1))

draw_rhombus(int(input()))

# draw_rhombus(3)
# draw_rhombus(4)
# draw_rhombus(5)

# print(generate_line('*', 5))