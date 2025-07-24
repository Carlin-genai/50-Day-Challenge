@app.route('/')
def index():
    formats = []
    meaning = None
    selected_fonts = []
    
    name = request.args.get('name', 'Carlin Venishiya')  # Default if not provided
    parts = name.split()
    
    if len(parts) >= 2:
        first = parts[0]
        last = parts[-1]
    else:
        first = parts[0]
        last = ""

    formats = [
        f"{first} {last}",
        f"{last}, {first}",
        f"{first[0]}. {last}",
        f"{last.upper()}, {first.title()}"
    ]

    selected_fonts = random.sample(fonts, min(len(fonts), len(formats)))

    base_name = first.capitalize()
    meaning = name_meanings.get(base_name, "Meaning not found in our database.")

    return render_template('index.html', name=name, formats=zip(formats, selected_fonts), meaning=meaning)
