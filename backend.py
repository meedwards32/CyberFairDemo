from flask import Flask, request, redirect
import datetime

app = Flask(__name__)

# Route to serve the main page
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Google-like Homepage</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                font-family: Arial, sans-serif;
                background-color: #fff;
            }
            .logo {
                margin-bottom: 30px;
            }
            .logo img {
                width: 272px;
                height: 92px;
            }
            .search-box {
                width: 100%;
                max-width: 584px;
                display: flex;
                align-items: center;
                padding: 10px 20px;
                border: 1px solid #dfe1e5;
                border-radius: 24px;
                box-shadow: 0px 1px 6px rgba(32, 33, 36, 0.28);
            }
            .search-box input[type="text"] {
                flex: 1;
                font-size: 16px;
                border: none;
                outline: none;
                height: 30px;
            }
            .search-buttons {
                margin-top: 20px;
                display: flex;
                gap: 10px;
            }
            .search-buttons input {
                padding: 10px 20px;
                background-color: #f8f9fa;
                border: 1px solid #f8f9fa;
                border-radius: 4px;
                color: #5f6368;
                cursor: pointer;
            }
            .search-buttons input:hover {
                background-color: #e8e8e8;
            }
        </style>
    </head>
    <body>
        <div class="logo">
            <img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" alt="Google Logo">
        </div>
    
        <form action="/search" method="POST">
            <div class="search-box">
                <input type="text" name="query" placeholder="Search Google or type a URL">
            </div>
            <div class="search-buttons">
                <input type="submit" value="Google Search">
            </div>
        </form>
    </body>
    </html>
    '''

# Route to handle search queries and redirect to Google search
@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['query']  # Get the search query from the form
    timestamp = datetime.datetime.now()   # Add a timestamp to each query

    # Store the query in a text file with the timestamp
    with open('search_queries.txt', 'a') as file:
        file.write(f"{timestamp}: {search_query}\n")

    # Redirect the user to Google search results for the query
    google_search_url = f"https://www.google.com/search?q={search_query}"
    return redirect(google_search_url)

if __name__ == '__main__':
    app.run(debug=True)
