import React from 'react';

export const TransactionList = ({ transactions }) => {
    return (
        <div className="overflow-x-auto">
            <table className="min-w-full table-auto">
                <thead>
                    <tr className="bg-gray-100">
                        <th className="px-4 py-2">Date</th>
                        <th className="px-4 py-2">Amount</th>
                        <th className="px-4 py-2">Category</th>
                        <th className="px-4 py-2">Type</th>
                        <th className="px-4 py-2">Description</th>
                    </tr>
                </thead>
                <tbody>
                    {transactions.map((transaction, index) => (
                        <tr key={index} className={index % 2 === 0 ? 'bg-white' : 'bg-gray-50'}>
                            <td className="px-4 py-2">
                                {new Date(transaction.date).toLocaleDateString()}
                            </td>
                            <td className={`px-4 py-2 ${
                                transaction.transaction_type === 'income' 
                                    ? 'text-green-600' 
                                    : 'text-red-600'
                            }`}>
                                {transaction.transaction_type === 'income' ? '+' : '-'}
                                ${Math.abs(transaction.amount).toFixed(2)}
                            </td>
                            <td className="px-4 py-2">{transaction.category}</td>
                            <td className="px-4 py-2 capitalize">{transaction.transaction_type}</td>
                            <td className="px-4 py-2">{transaction.description}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}; 