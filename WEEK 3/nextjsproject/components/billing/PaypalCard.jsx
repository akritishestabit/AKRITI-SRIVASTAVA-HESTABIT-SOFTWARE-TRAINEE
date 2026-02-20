"use client";

import { FaPaypal } from "react-icons/fa";

export default function PaypalCard() {
  return (
    <div className="bg-white rounded-2xl shadow-md p-6 h-[200px] flex flex-col justify-between">
      
      
      <div className="w-12 h-12 bg-teal-400 rounded-xl flex items-center justify-center text-white">
        <FaPaypal size={18} />
      </div>

     
      <div>
        <h3 className="text-lg font-semibold text-gray-800">
          Paypal
        </h3>
        <p className="text-sm text-gray-400">
          Freelance Payment
        </p>
      </div>

      
      <div className="text-xl font-bold text-gray-800">
        $455.00
      </div>
    </div>
  );
}
