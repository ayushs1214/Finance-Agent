import os
from dotenv import load_dotenv
from finance_manager import FinanceManager
import pandas as pd

# Load environment variables from .env file
load_dotenv()

def test_environment():
    try:
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        return True
    except Exception as e:
        print(f"Environment test failed: {str(e)}")
        return False

def test_agent_initialization():
    try:
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        manager = FinanceManager(api_key)
        # Check for required attributes and agent types
        if not hasattr(manager, 'agents'):
            raise ValueError("Manager does not have 'agents' attribute")
        required_agents = ['user_proxy', 'financial_advisor', 'data_analyst']
        for agent in required_agents:
            if agent not in manager.agents:
                raise ValueError(f"Missing required agent: {agent}")
        return True
    except Exception as e:
        print(f"Agent initialization test failed: {str(e)}")
        return False

def test_transaction_recording():
    try:
        api_key = os.getenv('GEMINI_API_KEY')
        manager = FinanceManager(api_key)
        # Test multiple transactions
        test_transactions = [
            (100.0, "Income", "income", "Test income"),
            (-50.0, "Food", "expense", "Test expense"),
        ]
        for amount, category, tx_type, desc in test_transactions:
            manager.record_transaction(amount, category, tx_type, desc)
        
        # Verify transactions were recorded correctly
        if len(manager.transactions) != 2:
            raise ValueError("Failed to record all transactions")
        return True
    except Exception as e:
        print(f"Transaction recording test failed: {str(e)}")
        return False

def test_spending_analysis():
    try:
        api_key = os.getenv('GEMINI_API_KEY')
        manager = FinanceManager(api_key)
        # Add test transactions
        manager.record_transaction(100.0, "Income", "income", "Test")
        
        # Test spending summary
        summary = manager.get_spending_summary()
        if not isinstance(summary, pd.DataFrame):
            raise ValueError("Spending summary should return a DataFrame")
            
        # Test visualization
        manager.visualize_spending()
        if not os.path.exists('spending_analysis.png'):
            raise ValueError("Spending visualization failed to create image")
            
        return True
    except Exception as e:
        print(f"Spending analysis test failed: {str(e)}")
        return False

def main():
    print("Starting system tests...\n")
    
    tests = [
        ("Environment test", test_environment),
        ("Agent initialization test", test_agent_initialization),
        ("Transaction recording test", test_transaction_recording),
        ("Spending analysis test", test_spending_analysis),
    ]
    
    all_passed = True
    for test_name, test_func in tests:
        if test_func():
            print(f"✅ {test_name} passed")
        else:
            print(f"❌ {test_name} failed")
            all_passed = False
        
    if all_passed:
        print("\n🎉 All tests completed successfully!")
    else:
        print("\n⚠️ Some tests failed!")

if __name__ == "__main__":
    main() 