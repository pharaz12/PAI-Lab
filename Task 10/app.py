from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route for sentiment analysis (just as a placeholder)
@app.route('/sentiment', methods=['POST'])
def sentiment():
    sentence = request.form['sentence']
    # Add sentiment analysis logic here if needed
    return jsonify({'result': f'Sentiment analysis for: {sentence}'})

# Starting the Flask app
if __name__ == "__main__":
    app.run(debug=True)
