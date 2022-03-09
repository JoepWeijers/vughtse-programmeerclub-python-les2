for nummer in range(1, 100):
    if nummer % 15 == 0:
        print("programmeerclub")
        continue
    
    if nummer % 3 == 0:
        print("programmeer")
        continue
    
    if nummer % 5 == 0:
        print("club")
        continue

    print(nummer)
	