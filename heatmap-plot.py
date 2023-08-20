import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

datafile = sys.argv[1]
smt = int(sys.argv[2])
plotfile = sys.argv[3]

df = pd.read_csv(datafile, header=None).set_index([0, 1]).unstack()
n = df.shape[0]
ticks = np.arange(n)

if smt:
    idx = [x for i in range(n//2) for x in (i, i+n//2)]
    df = df.iloc[idx, idx]
    labels = [l for i in range(n//2) for l in (f'{i+1}a', f'{i+1}b')]
else:
    labels = df.index + 1

fig, ax = plt.subplots(figsize=(8, 8), dpi=200)
hm = ax.matshow(df)
hm.get_cmap().set_bad(color='gray')

ax.set_xticks(ticks, labels=labels, rotation=90)
ax.set_yticks(ticks, labels=labels)
ax.set_title('Core to core latency')
ax.set_xlabel('core #')
ax.xaxis.set_label_position('top')
ax.set_ylabel('core #')
ax.tick_params(bottom=False)

cb = ax.figure.colorbar(hm, ax=ax, fraction=0.046, pad=0.04)
cb.ax.set_ylabel('ns', rotation=-90, va="bottom")

fig.tight_layout()
fig.savefig(plotfile, transparent=False, facecolor='white')
