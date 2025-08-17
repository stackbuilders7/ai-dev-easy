from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  # Changed import

class LLM_Interface:
    llm: ChatOpenAI  # Changed type hint

    def __init__(self):
        load_dotenv()

        # Initialize OpenAI LLM using ChatOpenAI for chat models
        self.llm = ChatOpenAI(
            model="gpt-4.1-mini",
            temperature=0.7,
            max_tokens=100
        )

    def ask_llm(self, question: str) -> str:
        print(f"Sending prompt: {question}")

        # Get response
        response = self.llm.invoke(question)
        print(f"Response: {response}")

        return response

    def ask_llm_with_context(self, question: str, context: str) -> str:
        final_question = f"Answer user question using provided context as knowledge. \n Question: {question}\n\nContext:\n{context}"
        print(f"Sending prompt: {final_question}")

        # Get response
        response = self.llm.invoke(final_question)
        print(f"Response: {response.content}")

        return response.content

if __name__ == "__main__":
    llm_interface = LLM_Interface()
    print(llm_interface.ask_llm("What is the capital of France?"))
    print(llm_interface.ask_llm_with_context("What is the capital?", "France is a country in Europe."))
