from flask import Flask, request, render_template, send_file, flash, redirect
import os
import tempfile
from werkzeug.utils import secure_filename
from ml_functions import audio_to_text, transcript_to_meeting_minutes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            flash('No file was uploaded')
            return redirect(request.url)
        file = request.files['file']

        filename = secure_filename(file.filename)

        with tempfile.TemporaryDirectory() as tempdir:
            input_path = os.path.join(tempdir, filename)
            file.save(input_path)

            try:
                transcript = audio_to_text(input_path)
                transcript = transcript['text']
                meeting_minutes = transcript_to_meeting_minutes(transcript)

                with open("meeting_minutes.txt", "w") as f:
                    f.write(meeting_minutes)

                return send_file("meeting_minutes.txt", as_attachment=True)
            except Exception as e:
                flash('Error')
                return redirect(request.url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
