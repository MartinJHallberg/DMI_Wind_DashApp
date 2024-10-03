from dmi_data import get_dmi_forecast_data
from dotenv import load_dotenv
import os

api_key = os.getenv("DMI_KEY_FORECAST")

df = get_dmi_forecast_data(
    api_key,
    12.3,
    56.13,
    "wind",
    "wind-speed",
    "wind-dir",
    "gust-wind-speed-10m"
    )

df.to_csv("data/wind_forecast.csv", index=False)

df = get_dmi_forecast_data(
    api_key,
    12.3,
    56.13,
    "waves",
    "significant-wave-height",
    "dominant-wave-period",
    "mean-wave-period",
    "mean-wave-dir",
    "significant-windwave-height",
    "mean-windwave-period",
    "mean-windwave-dir",
    "significant-totalswell-height",
    "mean-totalswell-period",
    "mean-totalswell-dir"
    )

df.to_csv("data/wave_forecast.csv", index=False)