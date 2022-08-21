import pandas as pd
import matplotlib.pyplot as plt

PATH = "/home/soubaboy/Téléchargements/mushra.csv"

df = pd.read_csv(PATH)

print(df)
autofx_feat = df[df['rating_stimulus'] == 'C1']
autofx = df[df['rating_stimulus'] == 'C2']
NC163 = df[df['rating_stimulus'] == 'C3']
C163 = df[df['rating_stimulus'] == 'C4']
C211 = df[df['rating_stimulus'] == 'C5']
random = df[df['rating_stimulus'] == 'C6']
ref = df[df['rating_stimulus'] == 'reference']
ref_score = ref['rating_score']
random_score = random['rating_score']
C163_score = C163['rating_score']
C211_score = C211['rating_score']
NC163_score = NC163['rating_score']
autofx_score = autofx['rating_score']
autofx_feat_score = autofx_feat['rating_score']
x = [ref_score, autofx_feat_score, autofx_score, C211_score, C163_score, NC163_score, random_score]

plt.figure()
plt.boxplot(x, notch=True, labels=['ref', 'AutoFX-F', 'AutoFX', '211C', '163C', '163NC', 'random'], patch_artist=False, )
#plt.violinplot(x)
plt.ylabel("Rating")
plt.show(block=True)