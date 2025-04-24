from langchain.chat_models import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate

def draft_answer(context):
    llm = ChatAnthropic(model_name="claude-3-haiku-20240307", temperature=0)
    prompt = ChatPromptTemplate.from_template("""
        You are a research summarizer. Based on the following context, draft a concise and informative answer.

        Context:
        {context}

        Answer:
    """)
    chain = prompt | llm
    return chain.invoke({"context": context}).content
