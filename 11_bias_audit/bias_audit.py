
import pandas as pd
import matplotlib.pyplot as plt

# Replace this section with your own dataset loading
# Example:
# df = pd.read_excel("data/raw/bd3 BALANCEADA.xlsx")

# y = df["CALIFICACIÓN"]

class_distribution = y.value_counts().sort_index()

bias_table = class_distribution.reset_index()
bias_table.columns = ["Class","Samples"]

bias_table.to_csv(
    "bias_audit_splits.csv",
    index=False
)

plt.figure(figsize=(7,5))

plt.bar(
    bias_table["Class"].astype(str),
    bias_table["Samples"]
)

plt.title("Class Distribution")

plt.xlabel("Credit Rating Class")

plt.ylabel("Samples")

plt.tight_layout()

plt.savefig(
    "class_distribution.png",
    dpi=300
)

print("Bias audit completed.")
