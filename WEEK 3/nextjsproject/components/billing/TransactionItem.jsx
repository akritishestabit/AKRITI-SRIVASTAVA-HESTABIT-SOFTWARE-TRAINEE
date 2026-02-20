"use client";

import { FiArrowUp, FiArrowDown, FiClock } from "react-icons/fi";

export default function TransactionItem({
  title,
  date,
  amount,
  type = "income", 
}) {
  const isIncome = type === "income";
  const isExpense = type === "expense";
  const isPending = type === "pending";

  return (
    <div className="flex justify-between items-center">

      
      <div className="flex items-center gap-4">

       
        <div
          className={`w-10 h-10 flex items-center justify-center rounded-full
            ${
              isIncome
                ? "bg-green-100 text-green-600"
                : isExpense
                ? "bg-red-100 text-red-600"
                : "bg-gray-100 text-gray-500"
            }`}
        >
          {isIncome && <FiArrowUp />}
          {isExpense && <FiArrowDown />}
          {isPending && <FiClock />}
        </div>

        
        <div>
          <p className="font-medium text-gray-800">{title}</p>
          <p className="text-xs text-gray-500">{date}</p>
        </div>
      </div>

      
      <div>
        {isPending ? (
          <p className="text-sm font-medium text-gray-500">Pending</p>
        ) : (
          <p
            className={`text-sm font-semibold ${
              isIncome ? "text-green-600" : "text-red-600"
            }`}
          >
            {amount}
          </p>
        )}
      </div>
    </div>
  );
}
