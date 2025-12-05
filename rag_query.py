import boto3

client = boto3.client("bedrock-agent-runtime")

KNOWLEDGE_BASE_ID = "your-kb-id"
MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

def ask_question(question):
    response = client.retrieve_and_generate(
        knowledgeBaseId=KNOWLEDGE_BASE_ID,
        modelId=MODEL_ID,
        retrievalQuery={"text": question},
        generationConfiguration={"maxTokens": 500}
    )
    print("=== Generated Answer ===")
    print(response["output"]["text"])

if __name__ == "__main__":
    ask_question("List the financial risks mentioned in the documents.")
