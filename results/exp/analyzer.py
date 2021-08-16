import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# LOAD FILE
data = pd.read_csv("7lms.csv")

# CHANGE LABELS
data = data.replace(["C1", "C2", "C3", "C4"],
                    ["baseline", "lstm", "unet", "diffusion"])
data = data.replace(
    [" bad ", " poor ", " fair ", " good ", " excellent ", " NA "],
    [1, 2, 3, 4, 5, None])

# SPLIT BETWEEN VIOLIN AND FLUTE


def instrument(exp):
    if len(exp) == 4:
        return "violin"
    elif len(exp) == 5:
        return "flute"
    else:
        return None


# SPLIT BETWEEN TEST AND MIDI


def file_used(exp):
    if int(exp[-1]) < 5:
        return "test"
    elif int(exp[-1]) >= 5:
        return "MIDI"
    else:
        return None


data["instrument"] = data["trial_id"].map(instrument)
data["type"] = data["trial_id"].map(file_used)

# PRINT SCORES
rqst = data[["stimuli", "stimuli_rating", "type",
             "instrument"]].groupby(["stimuli", "type",
                                     "instrument"]).describe()
print(rqst)

# NUMBER OF PARTICIPANTS

print("Number of participants = ", data.trial_id.value_counts().lms1)

# BOXPLOTS
sns.set_theme(style="whitegrid")

f, ax = plt.subplots(figsize=(7, 6))
sns.catplot(x="stimuli",
            y="stimuli_rating",
            hue="instrument",
            col="type",
            kind="box",
            data=data,
            width=.5).set(xlabel='Models', ylabel='Score')

# Tweak the visual presentation
#ax.xaxis.grid(True)
#ax.set(ylabel="")
sns.despine(trim=True, left=True)
plt.show()
