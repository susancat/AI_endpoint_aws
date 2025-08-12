# AWS Lambda AI Endpoint Demo

## Overview
This is an end-to-end serverless AI API demo built with:
- AWS Lambda (Python runtime)
- OpenAI API (`gpt-5-nano`)
- Environment variable authentication
- Colab testing script with `userdata.get()` for secure key storage

Originally created as a personal upskilling project by a former full-stack developer and experienced Product Manager/Owner, now exploring cloud and AI integrations.

## Features
- Serverless AI text generation via AWS Lambda
- Token-based authentication
- Callable from any HTTP client, including Google Colab
- Example Colab script provided

## Files
- `AI_endpoint_function.py` — AWS Lambda function code
- `test_AWS_AI_endpoint_function.ipynb` — Colab script to test the deployed endpoint
- `README.md` — Project documentation

## Deployment Steps
1. Create an AWS Lambda function (Python 3.10+)
2. Set environment variables:
   - `APP_TOKEN`
   - `OPENAI_API_KEY`
   - `MODEL` (optional, for AI model)
3. Deploy `AI_endpoint_function.py`
4. Enable Function URL with authentication disabled
5. Test via Colab using `test_AWS_AI_endpoint_function.ipynb`

## LinkedIn Post Suggestion
> Just wrapped up a hands-on AWS Lambda + OpenAI API mini-project! 🚀
> 
> In this demo, I created a fully serverless AI endpoint with token-based authentication, deployed on AWS Lambda, and tested directly from Google Colab. It's a simple yet powerful setup to integrate AI into any application without maintaining servers.
> 
> Tech stack: AWS Lambda, OpenAI API, Python, Google Colab
> 
> Perfect as a learning exercise for cloud + AI integration, and a nice portfolio addition for product & tech roles.
