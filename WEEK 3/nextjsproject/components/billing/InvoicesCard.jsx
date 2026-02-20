"use client";

import { FiDownload } from "react-icons/fi";

const invoices = [
  { id: 1, date: "March, 01, 2020", amount: "$180" },
  { id: 2, date: "February, 10, 2021", amount: "$250" },
  { id: 3, date: "April, 05, 2020", amount: "$560" },
  { id: 4, date: "June, 25, 2019", amount: "$120" },
  { id: 5, date: "July, 15, 2021", amount: "$300" },
  { id: 6, date: "August, 10, 2021", amount: "$450" },
];

export default function InvoicesCard() {
  return (
    <div className="bg-white rounded-2xl shadow-md p-8 h-[450px] flex flex-col ">
      
      
      <div className="flex justify-between items-center mb-6">
        <h3 className="text-lg font-semibold text-gray-800">
          Invoices
        </h3>
        <button className="text-xs font-semibold text-teal-500 hover:underline">
          VIEW ALL
        </button>
      </div>

      
      <div className="flex-1 space-y-6 overflow-hidden">
        {invoices.map((item) => (
          <div
            key={item.id}
            className="flex justify-between items-center text-sm"
          >
            <div>
              <p className="text-gray-800 font-medium">
                {item.date}
              </p>
              <p className="text-gray-400 text-xs">
                #{item.id}
              </p>
            </div>

            <div className="flex items-center gap-3">
              <span className="text-gray-800 font-semibold">
                {item.amount}
              </span>
              <FiDownload className="text-gray-400 cursor-pointer hover:text-gray-600" />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
