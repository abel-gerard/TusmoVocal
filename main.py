import tusmo

accept = False
while not accept:
    mode = input("daily, suite ou solo ? ")
    if mode in ("daily", "suite", "solo"):
        tusmo.tusmo(mode)
        accept = True
        