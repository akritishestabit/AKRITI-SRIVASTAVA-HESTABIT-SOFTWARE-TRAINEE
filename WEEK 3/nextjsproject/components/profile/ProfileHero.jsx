"use client";

import Link from "next/link";
import { FiSearch, FiUser, FiSettings, FiBell } from "react-icons/fi";

export default function ProfileHero() {
  return (
    <div className="relative w-full h-[290px] rounded-[30px] overflow-hidden
                    bg-gradient-to-br from-teal-400 via-teal-500 to-teal-600">

      
      <div className="absolute inset-0 opacity-25">
        <svg
          className="w-full h-full"
          viewBox="0 0 800 800"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M0,300 C200,200 400,400 800,250"
            fill="none"
            stroke="white"
            strokeWidth="80"
          />
          <path
            d="M0,450 C250,400 450,600 800,500"
            fill="none"
            stroke="white"
            strokeWidth="60"
          />
        </svg>
      </div>

      
      <div className="relative z-10 flex items-start justify-between px-8 pt-6 text-white">

        
        <div>
          <div className="flex items-center gap-2 text-sm">
            <span className="opacity-70">Pages</span>
            <span className="opacity-50">/</span>
            <span className="font-semibold text-white">
              Profile
            </span>
          </div>

          <h1 className="text-2xl font-bold mt-2">
            Profile
          </h1>
        </div>

        
        <div className="flex items-center gap-6">

          
          <div className="relative">
            <FiSearch className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 text-sm" />
            <input
              type="text"
              placeholder="Type here..."
              className="pl-9 pr-4 py-2 rounded-full text-sm text-gray-700
                         focus:outline-none w-[200px]"
            />
          </div>

          
          <Link
            href="/auth/signin"
            className="flex items-center gap-2 text-sm font-medium hover:opacity-80 transition"
          >
            <FiUser />
            Sign In
          </Link>

          
          <FiSettings className="cursor-pointer hover:opacity-80 transition" />
          <FiBell className="cursor-pointer hover:opacity-80 transition" />

        </div>
      </div>
    </div>
  );
}
