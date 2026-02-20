"use client";

import TransactionItem from "./TransactionItem";

export default function TransactionsSection() {
  return (
    <div className="bg-white rounded-2xl p-6 shadow-md h-full">

     
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-lg font-semibold text-gray-800">
          Your Transactions
        </h2>
        <p className="text-xs text-gray-500">
          23 - 30 March 2020
        </p>
      </div>

    
      <div>
        <p className="text-xs text-gray-400 mb-4">NEWEST</p>

        <div className="space-y-6">
          <TransactionItem
            title="Netflix"
            date="27 March 2020, at 12:30 PM"
            amount="- $2500"
            type="expense"
          />

          <TransactionItem
            title="Apple"
            date="27 March 2020, at 12:30 PM"
            amount="+ $2500"
            type="income"
          />
        </div>
      </div>

      
      <div className="mt-8">
        <p className="text-xs text-gray-400 mb-4">YESTERDAY</p>

        <div className="space-y-6">
          <TransactionItem
            title="Stripe"
            date="26 March 2020, at 13:45 PM"
            amount="+ $800"
            type="income"
          />

          <TransactionItem
            title="HubSpot"
            date="26 March 2020, at 12:30 PM"
            amount="+ $1700"
            type="income"
          />

          <TransactionItem
            title="Webflow"
            date="26 March 2020, at 05:00 AM"
            type="pending"
          />

          <TransactionItem
            title="Microsoft"
            date="25 March 2020, at 16:30 PM"
            amount="- $987"
            type="expense"
          />
        </div>
      </div>
    </div>
  );
}
