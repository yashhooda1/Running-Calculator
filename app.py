from flask import Flask, render_template, request
import math

app = Flask(__name__)

def pace_calculator(time_in_minutes, distance_in_miles):
    return time_in_minutes / distance_in_miles

def distance_calculator(average_pace, time_in_minutes):
    return time_in_minutes / average_pace

def time_calculator(average_pace, total_distance):
    return total_distance * average_pace

def predict_race_time(running_time, running_distance, predicted_race_distance):
    return float(running_time) * pow(float(predicted_race_distance)/float(running_distance), 1.06)

def calculate_training_paces(predicted_race_time):
    return {
        "Easy Run Pace": round(1.50 * predicted_race_time, 2),
        "Tempo Run Pace": round(1.25 * predicted_race_time, 2),
        "VO2 Max Run Pace": round(1.35 * predicted_race_time, 2),
        "Speed Run Pace": round(1.10 * predicted_race_time, 2),
        "Long Run Pace": round(1.55 * predicted_race_time, 2)
    }

def calculate_vo2_max(running_time, running_distance, gender, body_weight):
    predicted_race_time = float(running_time) * pow(float(1.5)/float(running_distance), 1.06)
    gender_factor = 1 if gender == "M" else 0
    v02_max = 88.02 + (3.716 * gender_factor) - (0.0753 * body_weight) - (2.767 * predicted_race_time)
    return round(v02_max, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        calculation_type = request.form["calculation_type"]
        if calculation_type == "pace":
            time = float(request.form["time"])
            distance = float(request.form["distance"])
            result = f"Your average pace is {pace_calculator(time, distance):.2f} minutes per mile."
        elif calculation_type == "distance":
            pace = float(request.form["pace"])
            time = float(request.form["time"])
            result = f"Your total distance is {distance_calculator(pace, time):.2f} miles."
        elif calculation_type == "time":
            pace = float(request.form["pace"])
            distance = float(request.form["distance"])
            result = f"Your total time is {time_calculator(pace, distance):.2f} minutes."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
    
with open("templates/index.html", "w") as f:
    f.write(html_template)