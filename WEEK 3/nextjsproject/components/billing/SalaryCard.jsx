"use client";

import { FiCreditCard } from "react-icons/fi";

export default function SalaryCard() {
  return (
    <div className="bg-white rounded-2xl shadow-md p-6 h-[200px] flex flex-col justify-between">
      
      
      <div className="w-12 h-12 bg-teal-400 rounded-xl flex items-center justify-center text-white">
        <FiCreditCard size={20} />
      </div>

      
      <div>
        <h3 className="text-lg font-semibold text-gray-800">
          Salary
        </h3>
        <p className="text-sm text-gray-400">
          Belong Interactive
        </p>
      </div>

      
      <div className="text-xl font-bold text-gray-800">
        +$2000
      </div>
    </div>
  );
}
