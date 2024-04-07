from fastapi import FastAPI
from celery import Celery
from requests import get
import json


app = FastAPI()

# Initialize Celery
celery = Celery(
    __name__,
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

def extract_people_names(url):
    # Load JSON data
    res = get(url.strip())
    data = res.json()

    # Extract first_name and last_name from each person
    people_data = data.get('people', [])
    if people_data:
        first_name = people_data[0].get('first_name', '')
        last_name = people_data[0].get('last_name', '')
        name = first_name +last_name
    else:
        name = "N/A"
    return name

# Define Celery task
@celery.task
def scrape():
    with open('link_file/compnay_details_urls.txt', 'r', encoding='utf-8') as file:
        urls = file.readlines()

    company_data = {}
    for url in urls:
        res = get(url.strip())
        data = res.json()
        global var1
        var1 = company_data['organization'] = data.get('name')
        global var2
        var2 = company_data['name'] = extract_people_names(url)
        return f"Scraping data : {company_data}"
    
# Define FastAPI endpoints
@app.post("/scrape")
async def start_scraping():
    # Start Celery task and return job id
    job = scrape.delay()
    return {"job_id": job.id}

@app.get("/scrape_results")
async def get_scrape_results():
    # Assuming you have stored the scraped data in a database
    # Retrieve the complete data from the database
    scraped_results =scrape()
    
    if scraped_results:
        return {"status": "success", "scraped_results": scraped_results}
    else:
        return {"status": "error", "message": "No scraped results found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)