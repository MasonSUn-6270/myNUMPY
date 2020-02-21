import matplotlib.pyplot as plt


cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
dog = ["happy", "happy", "happy", "very happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]

fig, ax = plt.subplots()
ax.plot(activity, dog, 'o-',label="dog",)
ax.plot(activity, cat, 'o-', label="cat")
ax.legend()
plt.savefig('cohere相关性')