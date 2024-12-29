import json
import random
from fpdf import FPDF

# Mocking CrewAI functionality
class RAG:
    @staticmethod
    def store_data(data):
        print("Simulating RAG: Data stored successfully.")

class Agent:
    def __init__(self, name):
        self.name = name

    def analyze(self, data):
        return [random.choice(["Positive", "Negative", "Neutral"]) for _ in data]

# Step 1: Mock data for X users
def collect_data():
    print("Collecting data...")
    users = [
        {"name": "User1", "followers": 1200, "tweets": ["I love coding!", "Python is amazing!"]},
        {"name": "User2", "followers": 800, "tweets": ["This is a bad day.", "Feeling sad."]},
        {"name": "User3", "followers": 1500, "tweets": ["AI is the future.", "Exploring new tech."]},
        {"name": "User4", "followers": 500, "tweets": ["I hate bugs in code.", "Debugging is hard!"]},
        {"name": "User5", "followers": 1000, "tweets": ["Learning new skills.", "Coding every day."]},
    ]
    # Save to JSON
    with open("users_data.json", "w") as f:
        json.dump(users, f, indent=4)
    print("Data collected and saved as users_data.json")
    return users

# Step 2: Perform sentiment analysis using mocked CrewAI
def analyze_sentiment(users):
    print("Analyzing sentiment...")
    sentiment_agent = Agent("SentimentAnalyzer")
    results = []
    for user in users:
        sentiments = sentiment_agent.analyze(user["tweets"])
        results.append({
            "name": user["name"],
            "followers": user["followers"],
            "tweets": user["tweets"],
            "sentiments": sentiments
        })
    print("Sentiment analysis completed.")
    return results

# Step 3: Generate a PDF report
def generate_pdf_report(results):
    print("Generating PDF report...")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Sentiment Analysis Report", ln=True, align='C')

    for user in results:
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"User: {user['name']}", ln=True)
        pdf.cell(200, 10, txt=f"Followers: {user['followers']}", ln=True)
        for i, tweet in enumerate(user["tweets"]):
            pdf.multi_cell(0, 10, txt=f"Tweet: {tweet}")
            pdf.cell(200, 10, txt=f"Sentiment: {user['sentiments'][i]}", ln=True)

    pdf.output("sentiment_report.pdf")
    print("PDF report generated as sentiment_report.pdf")

# Main script
if __name__ == "__main__":
    # Step 1: Collect data
    users = collect_data()

    # Step 2: Analyze sentiment
    results = analyze_sentiment(users)

    # Step 3: Generate PDF report
    generate_pdf_report(results)

    print("Task completed!")
