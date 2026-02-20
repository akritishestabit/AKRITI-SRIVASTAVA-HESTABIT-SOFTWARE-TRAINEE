"use client";

import { usePathname } from "next/navigation";
import { FiSearch, FiSettings, FiBell, FiUser } from "react-icons/fi";

const routeMap = {
  "/": "Dashboard",
  "/tables": "Tables",
  "/billing": "Billing",
  "/rtl": "RTL",
  "/profile": "Profile",
  "/sign-in": "Sign In",
  "/sign-up": "Sign Up",
};

export default function Navbar() {
  const pathname = usePathname();
  const currentPage = routeMap[pathname] || "Dashboard";

  return (
    <header className="h-16 bg-white flex items-center px-6">
      <div className="flex flex-col">
        <span className="text-xs text-gray-400">
          Pages /{" "}
          <span className="text-gray-900 font-medium">{currentPage}</span>
        </span>
        <span className="text-sm font-semibold text-gray-900">
          {currentPage}
        </span>
      </div>

      <div className="ml-auto flex items-center gap-4">
        <div className="relative">
          <FiSearch className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 text-sm" />
          <input
            type="text"
            placeholder="Type here..."
            className="pl-9 pr-3 py-1.5 w-44 text-sm rounded-md border border-gray-200
                       outline-none focus:ring-1 focus:ring-teal-400"
          />
        </div>

        <button className="flex items-center gap-1.5 text-sm font-medium text-gray-700 hover:text-teal-600">
          <FiUser />
          Sign In
        </button>

        <button className="p-2 rounded-full hover:bg-gray-100">
          <FiSettings className="text-gray-600" />
        </button>

        <button className="p-2 rounded-full hover:bg-gray-100">
          <FiBell className="text-gray-600" />
        </button>
      </div>
    </header>
  );
}


