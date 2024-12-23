import React from 'react';
import { Dashboard } from './components/Dashboard';
import './App.css';

function App() {
    return (
        <div className="min-h-screen bg-gray-50">
            <nav className="bg-white shadow-sm">
                <div className="container mx-auto px-4 py-3">
                    <h1 className="text-xl font-bold text-gray-800">
                        Financial Management System
                    </h1>
                </div>
            </nav>
            <main className="container mx-auto px-4 py-8">
                <Dashboard />
            </main>
            <footer className="bg-white shadow-sm mt-8">
                <div className="container mx-auto px-4 py-3 text-center text-gray-600">
                    © 2024 Financial Management System
                </div>
            </footer>
        </div>
    );
}

export default App; 