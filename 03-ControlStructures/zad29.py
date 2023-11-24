jacket_time = 40
underwear_time = 70
shoes_time = 20

washing_product = "shoes"
rinse = True
spin = False

if washing_product == "jacket":
    total_time = jacket_time
elif washing_product == "underwear":
    total_time = underwear_time
elif washing_product == "shoes":
    total_time = shoes_time
else:
    total_time = 0 

if rinse:
    total_time += 15

if spin:
    total_time += 9

print(f"Całkowity czas prania: {total_time} minut")
