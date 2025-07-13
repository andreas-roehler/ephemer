def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"Y-axis, y={y}"
        case (x, 0):
            return f"X-axis, x={x}"
        case (x, y):
            return f"X={x}, Y={y}"
        case _:
            return "Not a point"

print(describe_point((0, 0)))        # Output: Origin
print(describe_point((0, 5)))        # Output: Y-axis, y=5
print(describe_point((3, 0)))        # Output: X-axis, x=3
print(describe_point((2, 3)))        # Output: X=2, Y=3
print(describe_point("not a point")) # Output: Not a point

# def describe_point(point): match point: case (0, 0): return
# "Origin" case (0, y): return f"Y-axis, y={y}" case (x, 0): return
# f"X-axis, x={x}" case (x, y): return f"X={x}, Y={y}" case _: return
# "Not a point"

# Output: Origin
# Output: Y-axis, y=5
# Output: X-axis, x=3
# Output: X=2, Y=3
# Output: Not a point 
