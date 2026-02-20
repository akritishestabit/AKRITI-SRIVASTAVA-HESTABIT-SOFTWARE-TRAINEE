"use client";

import Link from "next/link";
import { FaFacebookF, FaApple, FaGoogle } from "react-icons/fa";
import AuthNavbar from "@/components/auth/AuthNavbar";
import AuthFooter from "@/components/auth/AuthFooter";

export default function SignUpPage() {
  return (
    <div className="min-h-screen bg-gray-100 relative">

      {/* HERO SECTION (FULL WIDTH TOP) */}
      <div
        className="absolute top-0 left-0 w-full h-[420px]
                   bg-gradient-to-br from-teal-400 via-teal-500 to-teal-600
                   rounded-b-[30px] overflow-hidden"
      >
        {/* Wave Overlay */}
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

        {/* Welcome Text */}
        <div className="relative z-10 flex flex-col items-center justify-center h-full text-white text-center">
          <h1 className="text-3xl font-bold mb-3">Welcome!</h1>
          <p className="text-sm opacity-90 max-w-md">
            Use these awesome forms to login or create new account in your project for free.
          </p>
        </div>
      </div>

      {/* NAVBAR (OVER HERO) */}
      <div className="relative z-30 pt-6">
        <AuthNavbar />
      </div>

      {/* SIGNUP CARD */}
      <div className="relative z-20 flex justify-center -mt-[-195px]">
        <div className="bg-white w-[420px] rounded-2xl shadow-xl p-8">

          <h2 className="text-center text-gray-700 font-semibold mb-6">
            Register with
          </h2>

          <div className="flex justify-center gap-4 mb-6">
            <div className="w-12 h-12 border border-gray-200 rounded-xl flex items-center justify-center hover:bg-gray-100 cursor-pointer transition">
              <FaFacebookF className="text-gray-700" />
            </div>
            <div className="w-12 h-12 border border-gray-200 rounded-xl flex items-center justify-center hover:bg-gray-100 cursor-pointer transition">
              <FaApple className="text-gray-700" />
            </div>
            <div className="w-12 h-12 border border-gray-200 rounded-xl flex items-center justify-center hover:bg-gray-100 cursor-pointer transition">
              <FaGoogle className="text-gray-700" />
            </div>
          </div>

          <p className="text-center text-gray-400 text-sm mb-6">or</p>

          <div className="space-y-4">
            <div>
              <label className="block text-sm text-gray-600 mb-1">
                Name
              </label>
              <input
                type="text"
                placeholder="Your full name"
                className="w-full rounded-xl border border-gray-200 px-4 py-3 text-sm
                           focus:outline-none focus:ring-2 focus:ring-teal-400"
              />
            </div>

            <div>
              <label className="block text-sm text-gray-600 mb-1">
                Email
              </label>
              <input
                type="email"
                placeholder="Your email address"
                className="w-full rounded-xl border border-gray-200 px-4 py-3 text-sm
                           focus:outline-none focus:ring-2 focus:ring-teal-400"
              />
            </div>

            <div>
              <label className="block text-sm text-gray-600 mb-1">
                Password
              </label>
              <input
                type="password"
                placeholder="Your password"
                className="w-full rounded-xl border border-gray-200 px-4 py-3 text-sm
                           focus:outline-none focus:ring-2 focus:ring-teal-400"
              />
            </div>
          </div>

          <div className="flex items-center mt-5">
            <input type="checkbox" className="accent-teal-500" />
            <span className="ml-2 text-sm text-gray-600">
              Remember me
            </span>
          </div>

          <button
            className="w-full mt-6 bg-teal-400 hover:bg-teal-500
                       text-white py-3 rounded-xl font-semibold transition"
          >
            SIGN UP
          </button>

          <p className="text-center text-sm text-gray-500 mt-6">
            Already have an account?{" "}
            <Link
              href="/auth/signin"
              className="text-teal-500 font-medium hover:underline"
            >
              Sign in
            </Link>
          </p>
        </div>
      </div >

      <AuthFooter />
    </div>
  );
}

