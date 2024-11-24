from services.llm_interface import query_llm
import logging


def query_llm_pipeline(context: str, question: str) -> str:
    """
    Pipeline to query the LLM using a retriever for fetching context.

    Args:
        question (str): The user's question.
        context_retriever: A retriever object for fetching relevant context.

    Returns:
        str: The response generated by the LLM.
    """
    try:
        logging.info("Executing LLM query pipeline.")

        # Use the updated query method from services
        response = query_llm(context, question)
        logging.info("Pipeline received response from LLM.")
        return response
    except Exception as e:
        logging.error(f"Error in LLM query pipeline: {e}", exc_info=True)
        raise
