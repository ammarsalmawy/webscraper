import requests
from bs4 import BeautifulSoup
import json
import boto3

# initialize the s3 client
s3 = boto3.client('s3')

# define the bucket name we created and path whre to save the file
bucket_name = "project1-webscraper"
s3_key = "scraped_data/headlines_data.json"  
# define the lambda handler; the entry point to the lambda function 
def lambda_handler(event, context):
    # URL of the page to scrape 
    url = "https://www.sportingnews.com/ca/soccer/news"
    
    # requests to send HTTP requests to the target website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Use BeautifulSoup to parse HTML and extract data
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all headline elements with the specified attributes, these attributes can be found by inspecting the html page of the target website
        headlines = soup.find_all('h3', {'data-testid': 'text--article-headline'})
        
        # Create a list to all headlines
        data = {"headlines": []}
        
        # Loop through each headline element and add its text to the list
        for headline in headlines:
            data["headlines"].append(headline.get_text(strip=True))
        
        # Convert data to JSON format 
        json_data = json.dumps(data)
        
        # upload JSON data to the S3 bucket
        s3.put_object(Bucket=bucket_name, Key=s3_key, Body=json_data, ContentType='application/json')
        # log the status when connection is successful
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "scraped data saved to S3 bucket", "bucket": bucket_name, "key": s3_key})
        }
    # log when the HTTP request fails
    else:
        return {
            "statusCode": response.status_code,
            "body": json.dumps({"message": "failed to retrieve the page"})
        }
