"use client";

import { FiHelpCircle } from "react-icons/fi";

export default function SidebarHelp() {
  return (
    <div className="mx-4 mb-6 p-6 rounded-xl bg-gradient-to-r from-teal-400 to-teal-500 text-white relative">
      <div className="absolute top-2 left-4 w-8 h-8 rounded-full bg-white flex items-center justify-center shadow">
        <FiHelpCircle className="text-teal-500 text-lg" />
      </div>

      <h4 className="text-sm font-semibold mt-6">Need help?</h4>

      <p className="text-xs mt-1 opacity-90">Please check our docs</p>

      <button className="mt-4 w-full bg-white text-teal-600 text-xs font-semibold py-2 rounded-md">
        DOCUMENTATION
      </button>
    </div>
  );
}
