import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("mushra.csv")
data = data.replace(["reference", "C1", "C2", "C3"],
                    ["resynth", "baseline", "lstm", "unet"])

print(data)

rqst = data[["rating_stimulus",
             "rating_score"]].groupby("rating_stimulus").describe()
print(rqst)

sns.set_theme(style="ticks")
f, ax = plt.subplots(figsize=(7, 6))
sns.boxplot(x="rating_score",
            y="rating_stimulus",
            data=data,
            whis=[0, 100],
            width=.6,
            palette="vlag")

sns.stripplot(x="rating_score",
              y="rating_stimulus",
              data=data,
              size=4,
              color=".3",
              linewidth=0)

# Tweak the visual presentation
ax.xaxis.grid(True)
ax.set(ylabel="")
sns.despine(trim=True, left=True)
plt.show()