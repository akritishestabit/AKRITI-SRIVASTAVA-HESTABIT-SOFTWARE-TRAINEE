"use client";

import { FiTrash2, FiEdit } from "react-icons/fi";

export default function BillingInfoCard({
  name,
  company,
  email,
  vat
}) {
  return (
    <div className="bg-gray-50 rounded-2xl p-6 flex justify-between items-start shadow-sm">

    
      <div>
        <h3 className="font-semibold text-gray-800">{name}</h3>

        <p className="text-sm text-gray-500 mt-2">
          Company Name: <span className="font-medium text-gray-700">{company}</span>
        </p>

        <p className="text-sm text-gray-500">
          Email Address: <span className="font-medium text-gray-700">{email}</span>
        </p>

        <p className="text-sm text-gray-500">
          VAT Number: <span className="font-medium text-gray-700">{vat}</span>
        </p>
      </div>

     
      <div className="flex gap-5 text-sm font-medium">
        <button className="flex items-center gap-2 text-red-500 hover:opacity-80 transition">
          <FiTrash2 />
          DELETE
        </button>

        <button className="flex items-center gap-2 text-gray-600 hover:opacity-80 transition">
          <FiEdit />
          EDIT
        </button>
      </div>
    </div>
  );
}
