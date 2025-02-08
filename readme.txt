Weird News Website
Project Overview
This project is a news website that fetches and displays weird and unusual news articles from around the world. The website is built using Flask (Python) as the backend and HTML/CSS for the frontend. It retrieves news data from an API (NewsAPI) and presents it in a structured and visually appealing way.

How It Works
Fetching News

The application requests news articles from NewsAPI using a specific query (q=weird) to get unusual and bizarre news.
It filters the results to display only articles that contain both an image and a summary, ensuring a clean and engaging layout.
Displaying the News

The articles are displayed as cards, each containing:
A headline
A summary
An image (if available)
A "Read More" button linking to the full article
Handling Missing Data

If an article has no image, it is replaced with another article that does have an image.
If there are not enough valid articles, the website will notify users that no news is available.
Requirements to Run the Project
1. Prerequisites
Before running the project, ensure you have the following installed:

Python 3.x
pip (Python package manager)
A valid API key from NewsAPI
2. Installation Steps
Clone the Repository
First, clone the project from GitHub:

bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
Set Up a Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
Activate it:

Windows:
bash
Copy
Edit
venv\Scripts\activate
Mac/Linux:
bash
Copy
Edit
source venv/bin/activate
Install Dependencies
Run the following command to install the required Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
Set Up the API Key
Get a free API key from NewsAPI.
Open app.py and replace YOUR_API_KEY with your actual API key:
python
Copy
Edit
API_KEY = "YOUR_API_KEY"
3. Running the Application
Once everything is set up, start the Flask server with:

bash
Copy
Edit
python app.py
Now, open your browser and visit:

cpp
Copy
Edit
http://127.0.0.1:5000
4. Deploying the Project (Optional)
To make your website available online, you can deploy it using:

Heroku
Render
Vercel (For frontend-only hosting)
Conclusion
This project provides an interactive and user-friendly way to browse unusual news stories. It ensures a clean UI by filtering out incomplete articles, making it engaging and readable. The site is easy to set up, requiring just Python, Flask, and an API key.

🚀 Now you’re ready to explore the weirdest news from around the world!