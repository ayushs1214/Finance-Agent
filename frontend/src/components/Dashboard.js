import React, { useEffect, useState } from 'react';
import { TransactionForm } from './TransactionForm';
import { TransactionList } from './TransactionList';
import { SpendingChart } from './SpendingChart';
import { api } from '../services/api';

export const Dashboard = () => {
    const [transactions, setTransactions] = useState([]);
    const [spendingSummary, setSpendingSummary] = useState([]);
    const [analysis, setAnalysis] = useState('');

    const loadData = async () => {
        const [txns, summary, analysisData] = await Promise.all([
            api.getTransactions(),
            api.getSpendingSummary(),
            api.getAnalysis(),
        ]);
        setTransactions(txns);
        setSpendingSummary(summary);
        setAnalysis(analysisData.analysis);
    };

    useEffect(() => {
        loadData();
    }, []);

    const handleNewTransaction = async (transaction) => {
        await api.createTransaction(transaction);
        loadData();
    };

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Finance Manager</h1>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                    <h2 className="text-xl font-semibold mb-2">Add Transaction</h2>
                    <TransactionForm onSubmit={handleNewTransaction} />
                </div>
                <div>
                    <h2 className="text-xl font-semibold mb-2">Spending Summary</h2>
                    <SpendingChart data={spendingSummary} />
                </div>
            </div>
            <div className="mt-8">
                <h2 className="text-xl font-semibold mb-2">Recent Transactions</h2>
                <TransactionList transactions={transactions} />
            </div>
            {analysis && (
                <div className="mt-8">
                    <h2 className="text-xl font-semibold mb-2">Financial Analysis</h2>
                    <div className="bg-gray-100 p-4 rounded">
                        <pre>{analysis}</pre>
                    </div>
                </div>
            )}
        </div>
    );
}; 