"use client";

import Link from "next/link";
import { useState } from "react";

export default function SignInForm() {
  const [rememberMe, setRememberMe] = useState(true);

  const handleSubmit = (e) => {
    e.preventDefault();

    
    console.log("Form submitted");
  };

  return (
    <div className="w-full max-w-md">
      
      
      <h2 className="text-2xl font-bold text-teal-500">
        Welcome Back
      </h2>

      <p className="mt-2 text-sm text-gray-400">
        Enter your email and password to sign in
      </p>

      
      <form onSubmit={handleSubmit} className="mt-8 space-y-5">
        
        
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Email
          </label>
          <input
            type="email"
            placeholder="Your email address"
            className="w-full rounded-xl border border-gray-200 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-teal-400"
            required
          />
        </div>

       
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Password
          </label>
          <input
            type="password"
            placeholder="Your password"
            className="w-full rounded-xl border border-gray-200 px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-teal-400"
            required
          />
        </div>

        
        <div className="flex items-center gap-3">
          <button
            type="button"
            onClick={() => setRememberMe(!rememberMe)}
            className={`w-10 h-5 rounded-full flex items-center px-1 transition ${
              rememberMe ? "bg-teal-400" : "bg-gray-300"
            }`}
          >
            <span
              className={`w-4 h-4 bg-white rounded-full transition transform ${
                rememberMe ? "translate-x-5" : ""
              }`}
            />
          </button>

          <span className="text-sm text-gray-600">
            Remember me
          </span>
        </div>

        
        <button
          type="submit"
          className="w-full bg-teal-400 hover:bg-teal-500 text-white font-semibold py-3 rounded-xl transition"
        >
          SIGN IN
        </button>
      </form>

     
      <p className="mt-6 text-sm text-gray-400">
        Don&apos;t have an account?{" "}
        <Link
          href="/auth/signup"
          className="text-teal-500 font-medium hover:underline"
        >
          Sign up
        </Link>
      </p>
    </div>
  );
}
