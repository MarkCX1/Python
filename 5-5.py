pound = 20
kilogram = 1
KILOGRAM_TO_POUND = 2.2
POUND_TO_KILOGRAM = 0.45
print(format("Kilograms", "15s"), format("Pounds", "8s"), format("|", "5s"), format("Pounds", "12s"), "Kilograms")
while kilogram < 200:
    pounds = kilogram * KILOGRAM_TO_POUND
    kilograms = pound * POUND_TO_KILOGRAM
    print(kilogram, format(pounds, "18.1f"), format(" ", "3s"),
          format("|", "2s"), format(pound, "6.0f"), format(kilograms, "16.2f"))
    kilogram += 2
    pound += 5