import matplotlib.pyplot as plt

data = [255, 252, 265, 252, 223, 214, 212, 215, 212, 225, 205, 172, 186, 173, 167, 167, 192, 178, 160, 158, 141, 149, 144, 151, 138, 129, 119, 115, 109, 125, 140, 118, 96, 106, 83, 95, 91, 103, 115, 95, 84, 78, 79, 77, 91, 75, 68, 81, 64, 53, 73, 64, 71, 62, 64, 57]

plt.plot(data)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Data Pattern')
plt.grid(True)
plt.show()
