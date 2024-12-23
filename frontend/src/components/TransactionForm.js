import React, { useState } from 'react';

export const TransactionForm = ({ onSubmit }) => {
    const [transaction, setTransaction] = useState({
        amount: '',
        category: '',
        transaction_type: 'expense',
        description: '',
    });

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(transaction);
        setTransaction({
            amount: '',
            category: '',
            transaction_type: 'expense',
            description: '',
        });
    };

    return (
        <form onSubmit={handleSubmit} className="space-y-4">
            <div>
                <label>Amount</label>
                <input
                    type="number"
                    value={transaction.amount}
                    onChange={(e) => setTransaction({
                        ...transaction,
                        amount: e.target.value
                    })}
                    required
                />
            </div>
            <div>
                <label>Category</label>
                <input
                    type="text"
                    value={transaction.category}
                    onChange={(e) => setTransaction({
                        ...transaction,
                        category: e.target.value
                    })}
                    required
                />
            </div>
            <div>
                <label>Type</label>
                <select
                    value={transaction.transaction_type}
                    onChange={(e) => setTransaction({
                        ...transaction,
                        transaction_type: e.target.value
                    })}
                >
                    <option value="expense">Expense</option>
                    <option value="income">Income</option>
                </select>
            </div>
            <div>
                <label>Description</label>
                <input
                    type="text"
                    value={transaction.description}
                    onChange={(e) => setTransaction({
                        ...transaction,
                        description: e.target.value
                    })}
                    required
                />
            </div>
            <button type="submit">Add Transaction</button>
        </form>
    );
}; 