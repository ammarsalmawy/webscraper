# Web Scraper Lambda Function\
This project sets up an AWS Lambda function that scrapes the headlines from www.sportingnews.com and uploads the extracted data to an S3 bucket. This function is automated using a CloudWatch Events trigger to run at regular intervals.\

1. Install Dependencies\
   ```bash
      pip install boto3 -t .
      pip install requests -t .
      pip install beautifulsoup4 -t .

2. Package the Function\
   zip all the files including the python code and the libraries into one zip file\
3. deploy to AWS Lambda\
   upload the zip file to lambda function\
4. set up a CloudWatch events trigger\
   to automate your lambda function set up a CloudWatch rule specify as you time such as "suchedule" for how often and when the function should be triggred\
5. Configure IAM Policies\
   . basic Lambda execution role\
   . S3 Full Access Policy\

Note: Update the Bucket Name: Modify the bucket_name variable in the Lambda function code to match your S3 bucket.\
