prices = { "AAPL" : 180, "TSLA": 250, "GOOG": 150}
total =0
while True:
    stock = input("Stock (or end ): ").upper()
    if stock == "END":
        break
    qty = int(input("Qty:"))
    total += prices.get(stock, 0) * qty
    print("Total Investment:" , total)
    with open ("portfolio.txt", "w") as f:
        f.write(f"Total Investment = { total }")
