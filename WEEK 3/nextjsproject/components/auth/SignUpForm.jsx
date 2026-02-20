"use client";

import { FaFacebookF, FaApple, FaGoogle } from "react-icons/fa";
//import AuthInput from "./AuthInput";
//import AuthButton from "./AuthButton";
//import RememberMeToggle from "./RememberMeToggle";
import Link from "next/link";

export default function SignUpForm() {
  return (
    <div className="w-full max-w-md bg-white rounded-2xl shadow-xl px-10 py-10">
      
      {/* TITLE */}
      <h2 className="text-center text-lg font-semibold text-gray-800">
        Register with
      </h2>

      {/* SOCIAL BUTTONS */}
      <div className="flex justify-center gap-4 mt-6">
        <SocialIcon icon={<FaFacebookF />} />
        <SocialIcon icon={<FaApple />} />
        <SocialIcon icon={<FaGoogle />} />
      </div>

      {/* OR TEXT */}
      <div className="text-center text-gray-400 text-sm mt-6">or</div>

      {/* FORM FIELDS */}
      {/* <div className="mt-6 space-y-4">
        <AuthInput label="Name" placeholder="Your full name" />
        <AuthInput label="Email" placeholder="Your email address" />
        <AuthInput label="Password" placeholder="Your password" type="password" />
      </div> */}

      {/* REMEMBER ME */}
      {/* <div className="mt-4">
        <RememberMeToggle />
      </div> */}

      {/* BUTTON */}
      {/* <div className="mt-6">
        <AuthButton text="SIGN UP" />
      </div> */}

      {/* SIGN IN LINK */}
      <p className="text-center text-sm text-gray-400 mt-6">
        Already have an account?{" "}
        <Link href="/auth/signin" className="text-teal-500 font-medium">
          Sign in
        </Link>
      </p>
    </div>
  );
}

function SocialIcon({ icon }) {
  return (
    <div className="w-14 h-14 flex items-center justify-center rounded-xl border border-gray-200 text-gray-600 hover:bg-gray-100 transition cursor-pointer">
      {icon}
    </div>
  );
}
