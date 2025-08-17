from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import glob
from pypdf import PdfReader
from langchain_community.embeddings import GPT4AllEmbeddings

CHROMA_DB_PATH = './'

class ChromaEmbeddings:
    def __init__(self):
        # load_dotenv()
        self.collection_name = 'Test_DB'
        self.directory = CHROMA_DB_PATH
        # self.embeddings = OpenAIEmbeddings(model = "text-embedding-3-small")
        self.gpt4all_embd = GPT4AllEmbeddings()
        self.chroma_db = Chroma(persist_directory=self.directory, embedding_function=self.gpt4all_embd, collection_name=self.collection_name)

    def generate_embeddings(self, chunk_size:int, chunk_overlap:int):
        is_collection_empty: bool = self.chroma_db._collection.count() == 0 
        if is_collection_empty:
            texts = self.__getRecordsToIngest(chunk_size, chunk_overlap)
            self.__save_embeddings(texts)

    def __save_embeddings(self, texts: list):
        if not texts:
            print('No texts to save.')
            return

        print(f'Saving {len(texts)} embeddings to Chroma DB...')
        try:
            self.chroma_db = Chroma.from_texts(
                texts, self.gpt4all_embd, collection_name=self.collection_name, persist_directory=self.directory
            )
            print('Embeddings saved successfully.')
        except Exception as e:
            print(f'Error saving embeddings: {e}')
            raise      

    def __getRecordsToIngest(self, chunk_size:int, chunk_overlap:int):
        allTexts = self.__getPdfFileText()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        texts = []
        for text in allTexts:
            texts.extend(text_splitter.split_text(text))
        return texts
    
    def __getPdfFileText(self):
        pdf_texts = []
        for pdf_file in glob.glob('**/*.pdf', recursive=True):
            reader = PdfReader(pdf_file)
            text = ""
            for page in reader.pages:
                t = page.extract_text()
                text += t
            pdf_texts.append(text)
        return pdf_texts

    def search_debug(self, query:str, len:int):
        docs_and_scores = self.chroma_db.similarity_search_with_score(query, k=len)
        print('------------------------------------------Search results ------------------------------------------')
        for index, [doc, score] in enumerate(docs_and_scores):
            print('Index:' + str(index) + ' Score:'+ str(score))
        return [doc for doc, _ in docs_and_scores]
    
    def search(self, query:str, len:int = 1):
        return self.chroma_db.similarity_search(query, k=len)


if __name__ == "__main__":
    chroma = ChromaEmbeddings()
    chroma.generate_embeddings(1024, 128)
    print(chroma.search("Search Text"))


