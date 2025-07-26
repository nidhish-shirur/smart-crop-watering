from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage
saved_crop_details = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save-crop', methods=['POST'])
def save_crop():
    crop = request.form['crop']
    stage = request.form['stage']
    soil = request.form['soil']

    saved_crop_details['crop'] = crop
    saved_crop_details['stage'] = stage
    saved_crop_details['soil'] = soil

    return redirect(url_for('input_conditions'))

@app.route('/input-conditions', methods=['GET', 'POST'])
def input_conditions():
    if request.method == 'POST':
        temperature = float(request.form['temperature'])
        moisture = float(request.form['moisture'])

        # Basic logic for watering recommendation
        if moisture < 40 or temperature > 35:
            decision = "Yes, you should water the plant 💧"
        else:
            decision = "No, watering is not needed now ✅"

        return render_template(
            'prediction_summary.html',
            crop=saved_crop_details['crop'],
            stage=saved_crop_details['stage'],
            soil=saved_crop_details['soil'],
            temperature=temperature,
            moisture=moisture,
            recommendation=decision
        )

    return render_template('input_conditions.html')

if __name__ == '__main__':
    app.run(debug=True)
