import os 
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

DISTRICTS = ["Cheras", "Setapak", "Bangsar", "Kepong", "KLCC"]
N_DAYS = 7   # simulate one week of data
OUTPUT_PATH = os.path.join("data", "raw", "environment_kl.csv")

def generate_synthetic_environment_data(districts, n_days):
    """
    Generate synthetic environmental dataset for Kuala Lumpur districts.
    """

    start_date = datetime.today() - timedelta(days=n_days)
    dates = [start_date + timedelta(days=i) for i in range(n_days)]

    records = []
    for d in districts:
        for date in dates:
            pm2_5 = np.random.randint(15, 100)   # µg/m³
            pm10 = pm2_5 + np.random.randint(10, 50)
            no2 = np.random.randint(10, 60)
            o3 = np.random.randint(10, 80)

            # AQI (simplified mock formula)
            aqi = max(pm2_5, pm10 // 2, no2, o3)

            temp = round(np.random.uniform(26, 35), 1)   # °C
            humidity = np.random.randint(55, 90)         # %
            rainfall = round(np.random.uniform(0, 30), 1)  # mm
            wind_speed = round(np.random.uniform(0.5, 5.0), 1)  # m/s

            records.append({
                "date": date.strftime("%Y-%m-%d"),
                "district": d,
                "pm2_5": pm2_5,
                "pm10": pm10,
                "no2": no2,
                "o3": o3,
                "aqi": aqi,
                "temperature": temp,
                "humidity": humidity,
                "rainfall": rainfall,
                "wind_speed": wind_speed
            })

    return pd.DataFrame(records)

def main():
    df = generate_synthetic_environment_data(DISTRICTS, N_DAYS)

    # Ensure folder exists
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    # Save to CSV
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"✅ Synthetic dataset saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
