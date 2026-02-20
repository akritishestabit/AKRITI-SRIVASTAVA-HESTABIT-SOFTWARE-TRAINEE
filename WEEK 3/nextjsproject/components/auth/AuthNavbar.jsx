"use client";

import Image from "next/image";
import Link from "next/link";
import { FiUser, FiLogIn } from "react-icons/fi";
import { usePathname } from "next/navigation";

export default function AuthNavbar() {
  const pathname = usePathname();

  const isSignup = pathname === "/auth/signup";
  const isSignin = pathname === "/auth/signin";

  return (
    <header className="w-full flex justify-center mt-6 relative z-30">
      
      {/* MAIN CONTAINER */}
      <div
        className={`w-[92%] max-w-6xl px-8 py-3 flex items-center justify-between rounded-2xl transition
        ${
          isSignup
            ? "bg-transparent shadow-none"
            : "bg-white shadow-md"
        }`}
      >
        
        {/* LEFT - LOGO */}
        <div className="flex items-center gap-2">
          <Image
            src="/logo.svg"
            alt="Purity UI Logo"
            width={28}
            height={28}
          />
          <span
            className={`text-sm font-bold tracking-wide ${
              isSignup ? "text-white" : "text-gray-800"
            }`}
          >
            PURITY UI DASHBOARD
          </span>
        </div>

        {/* NAV LINKS */}
        <nav
          className={`flex items-center gap-8 text-sm font-medium transition ${
            isSignup ? "text-white" : "text-gray-600"
          }`}
        >
          <Link
            href="/dashboard"
            className={`hover:text-teal-400 ${
              pathname === "/dashboard" ? "font-semibold" : ""
            }`}
          >
            Dashboard
          </Link>

          <Link
            href="/profile"
            className={`flex items-center gap-1 hover:text-teal-400 ${
              pathname === "/profile" ? "font-semibold" : ""
            }`}
          >
            <FiUser className="text-sm" />
            Profile
          </Link>

          <Link
            href="/auth/signup"
            className={`hover:text-teal-300 ${
              isSignup ? "font-semibold underline" : ""
            }`}
          >
            Sign Up
          </Link>

          <Link
            href="/auth/signin"
            className={`flex items-center gap-1 hover:text-teal-300 ${
              isSignin ? "font-semibold underline" : ""
            }`}
          >
            <FiLogIn className="text-sm" />
            Sign In
          </Link>
        </nav>

        {/* FREE DOWNLOAD BUTTON */}
        <button
          className={`px-6 py-2 rounded-full text-sm font-medium transition
          ${
            isSignup
              ? "bg-white text-black hover:bg-gray-200"
              : "bg-gray-900 text-white hover:bg-gray-800"
          }`}
        >
          Free Download
        </button>
      </div>
    </header>
  );
}
