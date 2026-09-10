
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Create Network Dataset
# -----------------------------
np.random.seed(42)

n = 200

data = {
    "Date": pd.date_range("2026-01-01", periods=n, freq="D"),
    "Network_Type": np.random.choice(
        ["4G", "5G", "WiFi"], n
    ),
    "Provider": np.random.choice(
        ["Jio", "Airtel", "Vi"], n
    ),
    "Download_Speed_Mbps": np.random.randint(10, 500, n),
    "Upload_Speed_Mbps": np.random.randint(5, 150, n),
    "Latency_ms": np.random.randint(10, 150, n),
    "Signal_Strength_dBm": np.random.randint(-110, -50, n)
}

df = pd.DataFrame(data)

# -----------------------------
# 2. Connection Quality
# -----------------------------
def connection_quality(row):

    if row["Latency_ms"] < 40 and row["Download_Speed_Mbps"] > 100:
        return "Excellent"

    elif row["Latency_ms"] < 80 and row["Download_Speed_Mbps"] > 50:
        return "Good"

    elif row["Latency_ms"] < 120:
        return "Average"

    else:
        return "Poor"


df["Connection_Quality"] = df.apply(
    connection_quality, axis=1
)

# -----------------------------
# 3. Basic Analysis
# -----------------------------

print("\nNETWORK PERFORMANCE DATA\n")
print(df.head())

print("\nAverage Download Speed:")
print(df["Download_Speed_Mbps"].mean())

print("\nAverage Upload Speed:")
print(df["Upload_Speed_Mbps"].mean())

print("\nAverage Latency:")
print(df["Latency_ms"].mean())

print("\nNetwork Type Performance:")
print(
    df.groupby("Network_Type")["Download_Speed_Mbps"]
    .mean()
)

print("\nProvider Performance:")
print(
    df.groupby("Provider")["Download_Speed_Mbps"]
    .mean()
)

# -----------------------------
# 4. Download Speed by Network
# -----------------------------

network_speed = df.groupby(
    "Network_Type"
)["Download_Speed_Mbps"].mean()

plt.figure(figsize=(8, 5))

network_speed.plot(kind="bar")

plt.title("Average Download Speed by Network Type")
plt.xlabel("Network Type")
plt.ylabel("Download Speed (Mbps)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# -----------------------------
# 5. Provider Performance
# -----------------------------

provider_speed = df.groupby(
    "Provider"
)["Download_Speed_Mbps"].mean()

plt.figure(figsize=(8, 5))

provider_speed.plot(kind="bar")

plt.title("Internet Speed by Provider")
plt.xlabel("Provider")
plt.ylabel("Average Download Speed (Mbps)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# -----------------------------
# 6. Latency Analysis
# -----------------------------

plt.figure(figsize=(9, 5))

plt.plot(
    df["Date"],
    df["Latency_ms"]
)

plt.title("Network Latency Trend")
plt.xlabel("Date")
plt.ylabel("Latency (ms)")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# -----------------------------
# 7. Speed Trend
# -----------------------------

plt.figure(figsize=(9, 5))

plt.plot(
    df["Date"],
    df["Download_Speed_Mbps"],
    label="Download Speed"
)

plt.plot(
    df["Date"],
    df["Upload_Speed_Mbps"],
    label="Upload Speed"
)

plt.title("Internet Speed Trend")
plt.xlabel("Date")
plt.ylabel("Speed (Mbps)")

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# -----------------------------
# 8. Connection Quality
# -----------------------------

quality_count = df[
    "Connection_Quality"
].value_counts()

plt.figure(figsize=(7, 7))

quality_count.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Connection Quality Distribution")
plt.ylabel("")

plt.show()

# -----------------------------
# 9. Save Dataset
# -----------------------------

df.to_csv(
    "internet_network_performance.csv",
    index=False
)

print("\nDataset saved successfully!")
