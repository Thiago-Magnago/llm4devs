from langchain_text_splitters import RecursiveCharacterTextSplitter
#from langchain_text_splitters import CharacterTextSplitter
import re

def transform(source):
    # Remove espaços em branco do início e do final da string
    source = source.strip()
    # Substitui múltiplas quebras de linha consecutivas por uma única quebra de linha
    source = re.sub(r'\n+', '\n', source)

    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=1000,
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_text(source)