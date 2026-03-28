from src.llm.base import BaseLLM
from ollama import chat

class OllamaLLM(BaseLLM):
    """Ollama LLM implementation.
    It is going to use gpt-oss-20b model for OCR parsing.
    """
    def __init__(self, model: str = "gpt-oss:20b"):
        self.model = model

    def ocr(self,text: str) -> str:
        response = chat(
            model=self.model,
            messages = [
                {"role": "system", "content": f"""
                
                You are a highly intelligent assistant that extracts texts as structured data in JSON only format.

                Required fields:
                - 利⽤⽇ (transaction_date)
                - 利⽤合計⾦額 (amount)
                - 登録番号 (register_number)

                Rules:
                - Output JSON only
                - No explanation
                - No extra text
                - amount must be integer (no currency symbol)
                - amount should be in the range of 600 to 5000
                - amount must be divisible by 10 (last digit must be 0). Taxi fares in Japan never end in 1-9.
                - date format must be YYYY-MM-DD
                - reguster_number must be the length of 14 and start with T (T + 13 digits)

                Output MUST be valid JSON only.

                Return the result in JSON in the following format:
                    {{
                        "transaction_date": "YYYY-MM-DD",
                        "amount": "10000",
                        "register_number": "T1234567890123"
                    }}
                """},
                {"role": "user", "content": f"""
                Receipt text:
                {text}
                """}
                ],
                format="json"
            )

        # print(f"\nresponse: {response}\n")

        result = response["message"]["content"]

        # print(f"\nresponse[m][c]: {result}\n")

        
        return response["message"]["content"]