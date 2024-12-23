from dataclasses import dataclass
from typing import List, Optional
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import google.generativeai as genai
from finance_agents import user_proxy, financial_advisor, data_analyst

@dataclass
class Transaction:
    amount: float
    category: str
    transaction_type: str
    description: str
    date: datetime
    
class FinanceManager:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.transactions: List[Transaction] = []
        self.agents = {
            'user_proxy': user_proxy,
            'financial_advisor': financial_advisor,
            'data_analyst': data_analyst
        }
        
    def record_transaction(self, amount: float, category: str, 
                         transaction_type: str, description: str):
        transaction = Transaction(
            amount=amount,
            category=category,
            transaction_type=transaction_type,
            description=description,
            date=datetime.now()
        )
        self.transactions.append(transaction)
        
    def get_spending_summary(self) -> pd.DataFrame:
        # Convert transactions to DataFrame
        df = pd.DataFrame([vars(t) for t in self.transactions])
        return df.groupby('category').agg({
            'amount': 'sum',
            'transaction_type': 'count'
        }).reset_index()
    
    def visualize_spending(self):
        df = self.get_spending_summary()
        plt.figure(figsize=(10, 6))
        plt.bar(df['category'], df['amount'])
        plt.title('Spending by Category')
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('spending_analysis.png')
        
    def analyze_finances(self):
        # Create spending summary
        summary = self.get_spending_summary()
        self.visualize_spending()
        
        # Create prompt for analysis
        prompt = f"""
        Please analyze the following financial data and provide insights:
        
        Spending Summary:
        {summary.to_string()}
        
        Please provide:
        1. Analysis of spending patterns
        2. Areas for improvement
        3. Personalized recommendations
        """
        
        # Get analysis from Gemini
        response = self.model.generate_content(prompt)
        return response.text

def main():
    # Initialize the finance management system with your Gemini API key
    finance_system = FinanceManager(api_key="YOUR_GEMINI_API_KEY")
    
    # Record sample transactions
    transactions = [
        (1000.0, "Salary", "income", "Monthly salary"),
        (-50.0, "Groceries", "expense", "Weekly groceries"),
        (-30.0, "Entertainment", "expense", "Movie night"),
        (-100.0, "Utilities", "expense", "Electricity bill"),
        (-20.0, "Transportation", "expense", "Bus fare"),
        (-60.0, "Dining", "expense", "Restaurant dinner")
    ]
    
    for amount, category, tx_type, description in transactions:
        finance_system.record_transaction(amount, category, tx_type, description)
    
    # Analyze the financial data
    analysis = finance_system.analyze_finances()
    print(analysis)

if __name__ == "__main__":
    main() 