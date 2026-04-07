import boto3
import json

# Connect to Bedrock
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Send a message to Claude
response = client.invoke_model(
    modelId="us.anthropic.claude-sonnet-4-6",
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 200,
        "messages": [
            {
                "role": "user",
                "content": "Say hello and tell me one fun fact about Cape Town!"
            }
        ]
    })
)

# Print the response
result = json.loads(response["body"].read())
print(result["content"][0]["text"])