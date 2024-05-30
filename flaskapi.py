from flask import Flask, jsonify

app = Flask(__name__)

# Import your scraping functions here
from supplimentary_functions import scrape_analytics_insight, scrape_wired_news, scrape_venturebeat_news, scrape_mit_news, scrape_extremetech_news, scrape_huggingface_papers

def combine_data_simple(*data_list):
    combined_data = {'Article Title': [], 'Link': [], 'Image': []}

    for data in data_list:
        if data:
            for entry in data:
                combined_data['Article Title'].append(entry['Article Title'])
                combined_data['Link'].append(entry['Link'])
                combined_data['Image'].append(entry['Image'])

    return combined_data

# Define API route for /latestnews
@app.route('/latestnews')
def read_latestnews():
    # data_analytics_vidhya = scrape_analytics_insight()
    data_wired = scrape_wired_news()
    # data_venturebeat = scrape_venturebeat_news()
    data_mitnews = scrape_mit_news()
    data_extremetech = scrape_extremetech_news()
    data_huggingface = scrape_huggingface_papers()

    response_data = {
        # "data_with_description": data_mitnews,
        "data_without_description": data_wired,
        "hugging_face_paper": data_huggingface
    }

    return jsonify(response_data)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
