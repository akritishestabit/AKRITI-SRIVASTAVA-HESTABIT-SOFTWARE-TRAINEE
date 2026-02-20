"use client";

import PaymentCardItem from "./PaymentCardItem";

export default function PaymentMethodSection() {
  return (
    <div className="bg-white rounded-2xl shadow-md p-4">
      
     
      <div className="flex items-center justify-between">
        <h3 className="text-lg font-semibold text-gray-800">
          Payment Method
        </h3>

        <button className="bg-gray-900 text-white text-xs font-semibold px-4 py-2 rounded-lg hover:bg-gray-800 transition">
          ADD A NEW CARD
        </button>
      </div>

      
      <div className="space-y-4">
        <PaymentCardItem
          brand="VISA"
          number="**** **** **** 7852"
        />
        <PaymentCardItem
          brand="MC"
          number="**** **** **** 5248"
        />
      </div>
    </div>
  );
}
