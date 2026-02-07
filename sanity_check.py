from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class TestModel(BaseModel):
    x: int

print(TestModel(x=1))
