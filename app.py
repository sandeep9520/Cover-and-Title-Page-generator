from flask import Flask, render_template_string, request

app = Flask(__name__)

# Combined HTML Template (Form + Output Page)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assignment Title Page Generator</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f6f9; margin: 0; padding: 20px; }
        .container { max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h2 { text-align: center; color: #333; margin-bottom: 20px; }
        .form-group { margin-bottom: 15px; }
        label { font-weight: bold; display: block; margin-bottom: 5px; }
        input, select { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { width: 100%; background: #007bff; color: white; padding: 12px; border: none; border-radius: 4px; font-size: 16px; cursor: pointer; margin-top: 10px; }
        button:hover { background: #0056b3; }
        
        /* Styles for Generated Cover Page */
        .cover-page { background: #fff; padding: 40px; border-radius: 4px; min-height: 800px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box; }
        
        /* Style 1: Classic Border */
        .style-classic { border: 10px double #333; }
        
        /* Style 2: Modern Minimalist */
        .style-modern { border-left: 12px solid #007bff; border-right: 2px solid #007bff; }
        
        /* Style 3: Fancy Frame */
        .style-fancy { border: 2px solid #28a745; outline: 6px solid #28a745; outline-offset: -15px; }

        .text-center { text-align: center; }
        .header-section { margin-bottom: 30px; }
        .header-section h1 { text-transform: uppercase; margin: 5px 0; font-size: 26px; }
        .header-section h3 { margin: 5px 0; color: #555; font-size: 18px; }
        .topic-section { margin: 40px 0; padding: 15px; background: #f9f9f9; border-radius: 5px; }
        .topic-section h2 { margin: 5px 0; color: #000; }
        .details-grid { display: flex; justify-content: space-between; margin-top: 40px; text-align: left; }
        .details-box { width: 45%; }
        .details-box p { margin: 6px 0; line-height: 1.4; }
        
        .no-print { margin-bottom: 20px; }
        @media print {
            .no-print { display: none; }
            body { background: none; padding: 0; }
            .container { box-shadow: none; max-width: 100%; width: 100%; padding: 0; }
        }
    </style>
</head>
<body>

<div class="container">
    {% if not generated %}
    <h2>Assignment Cover Page Generator</h2>
    <form method="POST">
        <div class="form-group">
            <label>University Name:</label>
            <input type="text" name="university" required placeholder="e.g. Harvard University">
        </div>
        <div class="form-group">
            <label>College Name:</label>
            <input type="text" name="college" required placeholder="e.g. Faculty of Arts & Sciences">
        </div>
        <div class="form-group">
            <label>Assignment Topic:</label>
            <input type="text" name="topic" required placeholder="e.g. Artificial Intelligence in Healthcare">
        </div>
        <div class="form-group">
            <label>Subject Name:</label>
            <input type="text" name="subject" required placeholder="e.g. Computer Science">
        </div>
        <div class="form-group">
            <label>Student Name:</label>
            <input type="text" name="student_name" required>
        </div>
        <div class="form-group">
            <label>Class / Roll No:</label>
            <input type="text" name="student_class" required placeholder="e.g. B.Tech CS - Sem 4">
        </div>
        <div class="form-group">
            <label>Father's Name:</label>
            <input type="text" name="father_name" required>
        </div>
        <div class="form-group">
            <label>Mobile Number:</label>
            <input type="tel" name="mobile" required>
        </div>
        <div class="form-group">
            <label>Submitted By (Name):</label>
            <input type="text" name="submitted_by" required placeholder="Your Full Name">
        </div>
        <div class="form-group">
            <label>Submitted To (Teacher/Professor Name):</label>
            <input type="text" name="submitted_to" required placeholder="Prof. John Doe">
        </div>
        <div class="form-group">
            <label>Page Style Layout:</label>
            <select name="style">
                <option value="style-classic">Classic Border</option>
                <option value="style-modern">Modern Blue Border</option>
                <option value="style-fancy">Fancy Green Frame</option>
            </select>
        </div>
        <button type="submit">Generate Cover Page</button>
    </form>

    {% else %}
    <div class="no-print">
        <button onclick="window.print()">Print / Save as PDF</button>
        <a href="/" style="display:block; text-align:center; margin-top:10px; color:#007bff; text-decoration:none;">← Create Another Page</a>
    </div>

    <div class="cover-page {{ data.style }}">
        <div class="header-section text-center">
            <h1>{{ data.university }}</h1>
            <h3>{{ data.college }}</h3>
        </div>

        <div class="topic-section text-center">
            <p style="text-transform: uppercase; letter-spacing: 1px; margin-bottom:0;">Assignment On</p>
            <h2>{{ data.topic }}</h2>
            <p><strong>Subject:</strong> {{ data.subject }}</p>
        </div>

        <div class="details-grid">
            <div class="details-box">
                <h4 style="border-bottom: 2px solid #333; padding-bottom: 5px; margin-bottom: 10px;">SUBMITTED BY:</h4>
                <p><strong>Name:</strong> {{ data.submitted_by }}</p>
                <p><strong>Student Name:</strong> {{ data.student_name }}</p>
                <p><strong>Class:</strong> {{ data.student_class }}</p>
                <p><strong>Father's Name:</strong> {{ data.father_name }}</p>
                <p><strong>Mobile:</strong> {{ data.mobile }}</p>
            </div>
            
            <div class="details-box">
                <h4 style="border-bottom: 2px solid #333; padding-bottom: 5px; margin-bottom: 10px;">SUBMITTED TO:</h4>
                <p><strong>Professor/Teacher:</strong> {{ data.submitted_to }}</p>
                <p><strong>Department:</strong> {{ data.college }}</p>
            </div>
        </div>
    </div>
    {% endif %}
</div>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_data = {
            'university': request.form.get('university'),
            'college': request.form.get('college'),
            'student_name': request.form.get('student_name'),
            'student_class': request.form.get('student_class'),
            'subject': request.form.get('subject'),
            'topic': request.form.get('topic'),
            'father_name': request.form.get('father_name'),
            'mobile': request.form.get('mobile'),
            'style': request.form.get('style'),
            'submitted_by': request.form.get('submitted_by'),
            'submitted_to': request.form.get('submitted_to')
        }
        return render_template_string(HTML_TEMPLATE, generated=True, data=form_data)
    
    return render_template_string(HTML_TEMPLATE, generated=False)

if __name__ == '__main__':
    app.run(debug=True)

