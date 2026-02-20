"use client";

import { FiTrash2 } from "react-icons/fi";

export default function PaymentCardItem({ brand, number }) {
  return (
    <div className="bg-white rounded-2xl shadow-sm p-4 flex items-center justify-between">
      
     
      <div className="flex items-center gap-4">
        
        
        <div className="w-10 h-10 bg-gray-100 rounded-xl flex items-center justify-center font-semibold text-gray-700 text-sm">
          {brand}
        </div>

       
        <span className="text-sm font-medium text-gray-700">
          {number}
        </span>
      </div>

      
      <FiTrash2 className="text-gray-400 cursor-pointer hover:text-red-500 transition" />
    </div>
  );
}
