from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(text, chunk_size=1500, overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        length_function=len
    )
    return splitter.split_text(text)
