from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import os
from dotenv import load_dotenv
from finance_manager import FinanceManager

load_dotenv()

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize FinanceManager
finance_manager = FinanceManager(api_key=os.getenv('GEMINI_API_KEY'))

class TransactionCreate(BaseModel):
    amount: float
    category: str
    transaction_type: str
    description: str

class TransactionResponse(BaseModel):
    amount: float
    category: str
    transaction_type: str
    description: str
    date: datetime

@app.post("/transactions/", response_model=TransactionResponse)
async def create_transaction(transaction: TransactionCreate):
    try:
        finance_manager.record_transaction(
            amount=transaction.amount,
            category=transaction.category,
            transaction_type=transaction.transaction_type,
            description=transaction.description
        )
        return finance_manager.transactions[-1]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/transactions/", response_model=List[TransactionResponse])
async def get_transactions():
    return finance_manager.transactions

@app.get("/spending-summary/")
async def get_spending_summary():
    summary = finance_manager.get_spending_summary()
    return summary.to_dict(orient='records')

@app.get("/analyze/")
async def analyze_finances():
    return {"analysis": finance_manager.analyze_finances()} 