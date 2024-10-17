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
        /* Header styling */
        .header {
            position: absolute;
            top: 0;
            right: 0;
            padding: 15px;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .header a {
            color: #5f6368;
            text-decoration: none;
            font-size: 14px;
        }
        .header a:hover {
            text-decoration: underline;
        }
        .apps-icon {
            width: 30px;
            height: 30px;
            margine-left: 20px;
            background-image: url('https://thumb.ac-illust.com/3e/3edabcf91aa2e119568b5e39476cc95b_t.jpeg');
            background-size: cover;
            cursor: pointer;
        }
        .profile-pic {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background-image: url('https://caps.sa.ucsb.edu/sites/default/files/default_images/generic-user-icon.jpg');
            background-size: cover;
            cursor: pointer;
        }
        /* Logo styling */
        .logo {
            margin-bottom: 30px;
        }
        .logo img {
            width: 272px;
            height: 92px;
        }
        /* Search bar styling */
        .search-box {
            width: 450%;
            max-width: 1200px;
            margin-left: -250px;
            display: flex;
            align-items: center;
            padding: 15px;
            border: 1px solid #dfe1e5;
            border-radius: 24px;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        }
        .search-box input[type="text"] {
            flex: 1;
            font-size: 18px;
            border: none;
            outline: none;
            height: 30px;
        }
        /* Search button styling */
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
            font-size: 14px;
        }
        .search-buttons input:hover {
            background-color: #e8e8e8;
        }
    </style>
</head>
<body>

    <!-- Header section -->
    <div class="header">
        <a href="#">Gmail</a>
        <a href="#">Images</a>
        <div class="apps-icon"></div>
        <div class="profile-pic"></div>
    </div>

    <!-- Logo -->
    <div class="logo">
        <img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" alt="Google Logo">
    </div>

    <!-- Search box -->
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









#Sam comment 