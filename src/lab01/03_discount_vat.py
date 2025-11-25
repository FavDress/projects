price = float(input("Цена(₽):"))
discount = float(input("Скидка(%):"))
vat = float(input("НДС(%):"))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

base_r = round(base, 2)
vat_r = round(vat_amount, 2)
total_r = round(total, 2)

print("База после скидки:", base_r, "₽")
print("НДС:              ", vat_r, "₽")
print("Итого к оплате:   ", total_r, "₽")
