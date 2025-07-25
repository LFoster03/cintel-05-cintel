# --------------------------------------------
# Imports - PyShiny EXPRESS VERSION
# --------------------------------------------
from shiny import reactive, render
from shiny.express import ui
import random
from datetime import datetime
from collections import deque
import pandas as pd
import plotly.express as px
from shinywidgets import render_plotly
from scipy import stats
from faicons import icon_svg

# --------------------------------------------
# Constants
# --------------------------------------------
UPDATE_INTERVAL_SECS: int = 5
DEQUE_SIZE: int = 5

# --------------------------------------------
# Reactive value wrapper (deque)
# --------------------------------------------
reactive_value_wrapper = reactive.value(deque(maxlen=DEQUE_SIZE))

# --------------------------------------------
# Reactive calc for wind speed + timestamp
# --------------------------------------------
@reactive.calc()
def reactive_calc_combined():
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)

    # Simulate wind speed (5 to 40 km/h)
    wind_speed = round(random.uniform(5, 40), 1)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save new reading as dictionary
    new_entry = {"wind_speed": wind_speed, "timestamp": timestamp}

    # Append to deque
    reactive_value_wrapper.get().append(new_entry)

    # Snapshot for DataFrame & latest
    deque_snapshot = reactive_value_wrapper.get()
    df = pd.DataFrame(deque_snapshot)

    return deque_snapshot, df, new_entry

# ------------------------------------------------
# UI Page Options
# ------------------------------------------------
ui.page_opts(title="Penguin Colony Wind Monitor 🌬️🐧", fillable=True)

# ------------------------------------------------
# Sidebar
# ------------------------------------------------
with ui.sidebar(open="open"):
    ui.h2("Penguin Wind Explorer 🌬️", class_="text-center")
    ui.p("Monitoring live wind speeds in penguin habitats.", class_="text-center")
    ui.hr()
    ui.h6("Links:")
    ui.a("GitHub Source", href="https://github.com/LFoster03/cintel-05-cintel/tree/main", target="_blank")
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")

# ------------------------------------------------
# Main Layout: Value Box + Cards
# ------------------------------------------------
with ui.layout_columns():
    # Current wind speed value box
    with ui.value_box(
        showcase=icon_svg("wind"),
        theme="bg-gradient-blue-purple",
    ):
        "Current Wind Speed 🌬️"

        @render.text
        def display_wind():
            _, _, latest_entry = reactive_calc_combined()
            return f"{latest_entry['wind_speed']} km/h"

        "Blustery conditions 🐧"

    # Current timestamp card
    with ui.card(full_screen=True):
        ui.card_header("Current Date and Time 🕒")

        @render.text
        def display_time():
            _, _, latest_entry = reactive_calc_combined()
            return latest_entry['timestamp']

# ------------------------------------------------
# Data Table of Recent Readings
# ------------------------------------------------
with ui.card(full_screen=True):
    ui.card_header("Most Recent Wind Speed Readings 📊")

    @render.data_frame
    def display_df():
        _, df, _ = reactive_calc_combined()
        return render.DataGrid(df, width="100%")

# ------------------------------------------------
# Chart with Trend + Regression Line
# ------------------------------------------------
with ui.card():
    ui.card_header("Wind Speed Trend with Regression Line 📈")

    @render_plotly
    def display_plot():
        _, df, _ = reactive_calc_combined()

        if not df.empty:
            # Convert timestamp column to datetime
            df["timestamp"] = pd.to_datetime(df["timestamp"])

            # Scatter plot using timestamps
            fig = px.scatter(
                df,
                x="timestamp",
                y="wind_speed",
                title="Wind Speeds in Penguin Colony 🌬️",
                labels={"wind_speed": "Wind Speed (km/h)", "timestamp": "Time"},
                color_discrete_sequence=["blue"]
            )

            # Regression using integer sequence
            sequence = range(len(df))
            slope, intercept, _, _, _ = stats.linregress(sequence, df["wind_speed"])
            df["best_fit_line"] = [slope * x + intercept for x in sequence]

            # Add regression line aligned with timestamps
            fig.add_scatter(
                x=df["timestamp"],
                y=df["best_fit_line"],
                mode="lines",
                name="Trend Line"
            )

            # Fix axis formatting (HH:MM:SS)
            fig.update_xaxes(
                tickformat="%H:%M:%S"
            )

            fig.update_layout(
                xaxis_title="Time",
                yaxis_title="Wind Speed (km/h)",
                title_font=dict(size=20),
            )

            return fig

# ------------------------------------------------
# Histogram of Wind Speeds
# ------------------------------------------------
with ui.card():
    ui.card_header("Wind Speed Distribution Histogram 📊")

    @render_plotly
    def display_histogram():
        _, df, _ = reactive_calc_combined()

        if not df.empty:
            fig = px.histogram(
                df,
                x="wind_speed",
                nbins=5,
                title="Distribution of Last Wind Speed Readings 🌬️",
                labels={"wind_speed": "Wind Speed (km/h)"},
                color_discrete_sequence=["green"]
            )

            fig.update_layout(
                bargap=0.2,
                xaxis_title="Wind Speed (km/h)",
                yaxis_title="Frequency",
                title_font=dict(size=18),
            )

            return fig
