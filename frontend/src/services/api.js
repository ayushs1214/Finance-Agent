const API_BASE_URL = 'http://localhost:8000';

export const api = {
    async createTransaction(transaction) {
        const response = await fetch(`${API_BASE_URL}/transactions/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(transaction),
        });
        return response.json();
    },

    async getTransactions() {
        const response = await fetch(`${API_BASE_URL}/transactions/`);
        return response.json();
    },

    async getSpendingSummary() {
        const response = await fetch(`${API_BASE_URL}/spending-summary/`);
        return response.json();
    },

    async getAnalysis() {
        const response = await fetch(`${API_BASE_URL}/analyze/`);
        return response.json();
    },
}; 