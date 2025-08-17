import os
from dotenv import load_dotenv
from langchain_openai import OpenAI

def check_environment():
    load_dotenv()
    
    # Check if OpenAI API key is loaded
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    print("Environment variables loaded successfully")
    print(f"OPENAI_API_KEY: {api_key[:10]}..." if api_key else "OPENAI_API_KEY: Not found")

def test_openai_llm():
    try:
        # Initialize OpenAI LLM
        llm = OpenAI(
            model="gpt-4o-mini",
            temperature=0.7,
            max_tokens=100
        )
        
        # Test query
        prompt = "What is the capital of France?"
        print(f"Sending prompt: {prompt}")
        
        # Get response
        response = llm.invoke(prompt)
        print(f"Response: {response}")
        
        return True
    
    except Exception as e:
        print(f"Error testing OpenAI LLM: {e}")
        return False

def main():
    print("Starting OpenAI LLM test with LangChain...")
    
    try:
        check_environment()
        
        # Test OpenAI LLM
        success = test_openai_llm()
        
        if success:
            print("OpenAI LLM test completed successfully!")
        else:
            print("OpenAI LLM test failed!")
            
    except Exception as e:
        print(f"Test failed with error: {e}")

if __name__ == "__main__":
    main()
