# file: lambda_function.py
import os, json, logging, urllib.request, urllib.error

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
APP_TOKEN = os.environ.get("APP_TOKEN")
MODEL = os.environ.get("MODEL")

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def call_openai(prompt: str) -> str:
    url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": MODEL,      
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 1,
        "top_p": 1.0
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Bearer {OPENAI_API_KEY}")

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return body["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="ignore")
        logger.error(f"openai_http_error status={e.code} body={err_body}")
        raise
    except Exception as e:
        logger.exception("openai_call_error")
        raise

def lambda_handler(event, context):
    # normalize headers
    headers = event.get("headers") or {}
    headers_lc = { (k.lower() if isinstance(k,str) else k): v for k,v in headers.items() }
    token = headers_lc.get("x-app-token")

    if APP_TOKEN and token != APP_TOKEN:
        return {"statusCode": 401, "body": "Unauthorized"}

    try:
        body = event.get("body") or "{}"
        if isinstance(body, str):
            body = json.loads(body)
        prompt = body.get("prompt", "Say hello!")
        answer = call_openai(prompt)
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"answer": answer})
        }
    except Exception as e:
        # see CloudWatch
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}