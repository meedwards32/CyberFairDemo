from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

# Route to serve the main page
@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML file

# Route to handle search queries and store them in a text file
@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['query']  # Get the search query from the form
    timestamp = datetime.datetime.now()   # Add a timestamp to each query

    # Store the query in a text file with the timestamp
    with open('search_queries.txt', 'a') as file:
        file.write(f"{timestamp}: {search_query}\n")

    # Return a response or redirect to a new page
    return f"Search query '{search_query}' was saved successfully!"

if __name__ == '__main__':
    app.run(debug=True)
