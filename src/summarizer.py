from langchain_openai import ChatOpenAI
from langchain_community.llms import OpenAI
# or if that fails:
# from langchain_core.chains import create_retrieval_chain

def summarize_query(db, query):
    retriever = db.as_retriever(search_kwargs={"k":5})
    llm = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.2)
    chain = create_retrieval_chain(llm=llm, retriever=retriever)
    result = chain.invoke({"input": query})
    return result["output"] if "output" in result else result
