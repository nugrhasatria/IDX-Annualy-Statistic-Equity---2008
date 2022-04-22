import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

# 2008 Chart for:

                        # Trading Value, Trading Volume, Trading Frequency
                # Nilai Perdagangan Saham, Volume Perdagangan Saham, Trading Frequency
                                            # 2008

# Daily Averages of:
    # Periode Selama Satu Tahun
pr_08 = np.array(['Q1', 'Q2', 'Q3', 'Q4'])
    # Volume Perdagangan
vol_08 = np.array([3.439, 3.547, 2.707, 3.471])
    # Nilai Perdagangan
val_08 = np.array([5.569, 5.717, 3.823, 2.562])
    # Frekuensi Perdagangan
freq_08 = np.array([58.390, 61.150, 54.487, 49.190])

    # index 1
plt.subplot(3, 1, 1)
plt.plot(pr_08, vol_08, color='blue', marker='o')
plt.title("Rata-rata Perdagangan Saham Harian Tahun 2008")
    # Add Grid
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
    # index 2
plt.subplot(3, 1, 2)
plt.plot(pr_08, val_08, color='orange', marker='o')
    # Add Grid
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
    # index 3
plt.subplot(3, 1, 3)
plt.plot(pr_08, freq_08, color='crimson', marker='o')
plt.xlabel('Periode')
    # Add Grid
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
    # Checkout Chart
plt.show()


                        # Indeks Harga Saham Gabungan (dinormalisasi)
                                        # Tahun 2008

# Data for IHSG
    # Y-Axis - Nilai IHSG (dinormalisasi)
td08 = [1.000000, 0.959951, 0.748672, 0.553739]
# Periode
    # X-Axis - Periode Selama Satu Tahun
y08 = ['Q1', 'Q2', 'Q3', 'Q4']
    #
# Merge Datasets into Dataframe
a_df = {'td08': td08, 'y08': y08}
alpha = pd.DataFrame(a_df)

    # Axis for IHSG
fig, ax1 = plt.subplots(figsize = (10,6))
color = 'crimson'
ax1.set_title('Perkembangan Indeks Harga Saham Gabungan (IHSG) \n Tahun 2008 ', fontsize = 15, pad = 15)
ax1.set_xlabel('Periode / Kuartal', fontsize = 13)
ax1.set_ylabel('Indeks', fontsize = 13)
ax2 = sns.lineplot(x = 'y08', y = 'td08', data = alpha, marker='o', color = color)
ax1.tick_params(axis = 'y')
    # Add Grid
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)

    # Checkout Cart
plt.show()