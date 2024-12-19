import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import os

user_name = "Lavindu"

load_dotenv()

brt = boto3.client(
    "bedrock-runtime",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

model_id = "amazon.nova-lite-v1:0"
context_message = f"""
    You are a personal assistant for the user. Keep responses short and formal.
    Now greet the user with the name {user_name}.
"""

conversation = [
    {
        "role": "user",
        "content": [{"text": context_message}],
    }
]

def initialize_lm():
    return call_lm()

def process(input_text):
    if type(input_text) != str or len(input_text) == 0:
        return "Invalid input. Please try again."

    conversation.append({"role": "user", "content": [{"text": input_text}]})
    return call_lm()

def call_lm():
    try:
        # Send the message to the model, using a basic inference configuration.
        response = brt.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
        )

        # Extract and print the response text.
        response_text = response["output"]["message"]["content"][0]["text"]
        conversation.append({"role": "assistant", "content": [{"text": response_text}]})
        return response_text

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
        exit(1)
