

def christmas_tree(height: int, hollow: bool):
    assert height % 2 == 0 and height >= 4

    width = 0

    limit = height - 1
    count = 0

    while limit > 0:
        if count % 2 == 0:
            count += 1
            continue
        else:
            width = count
            count += 1
            limit -= 1
            continue


    if not hollow:
        turn = 1
        tick = 0

        for i in range(height - 1):
            string = []

            stop = int(((width -1) / 2) - tick)

            for _ in range(stop):
                string.append("-")
            
            for _ in range(turn):
                string.append("X")
            
            for _ in range(stop):
                string.append("-")

            temp = ""
            out = temp.join(string)
            print(out)

            turn += 2
            tick += 1

    if hollow:
        turn = 1
        tick = 0

        for i in range(height - 1):
            string = []

            stop = int(((width -1) / 2) - tick)

            if turn == 1:
                for _ in range(stop):
                    string.append("-")
                string.append("X")
                for _ in range(stop):
                    string.append("-")
            
            elif turn == width:
                for _ in range(width):
                    string.append("X")

            else:
                for _ in range(stop):
                    string.append("-")
                
                string.append("X")

                for _ in range(turn - 2):
                    string.append("-")

                string.append("X")
                
                for _ in range(stop):
                    string.append("-")

            temp = ""
            out = temp.join(string)
            print(out)

            turn += 2
            tick += 1
    
    base_stop = int(((width - 1) / 2))
    string_base = []
    for _ in range(base_stop):
        string_base.append("-")
    string_base.append("X")
    for _ in range(base_stop):
        string_base.append("-")
    base = ""
    base_out = base.join(string_base)
    print(base_out)


christmas_tree(6, False)

christmas_tree(6, True)


    
