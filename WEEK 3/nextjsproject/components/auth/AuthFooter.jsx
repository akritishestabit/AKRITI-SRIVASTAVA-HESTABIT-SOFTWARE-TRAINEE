"use client";

import Link from "next/link";

export default function AuthFooter() {
  return (
    <footer className="w-full px-10 mt-25 flex flex-col md:flex-row items-center justify-between text-xs text-gray-400">
    
      <p className="flex items-center gap-1">
        © 2021, Made with
        <span className="text-red-500">♥</span>
        by
        <span className="font-medium text-gray-500">
          Akriti Srivastava
        </span>
        &
        <span className="font-medium text-gray-500">
          Hestabit Software Trainee.
        </span>
        for a better web
      </p>

    
      <div className="flex items-center gap-6 mt-4 md:mt-0">
        <Link href="#" className="hover:text-teal-500">
          Creative Tim
        </Link>
        <Link href="#" className="hover:text-teal-500">
          Simmmple
        </Link>
        <Link href="#" className="hover:text-teal-500">
          Blog
        </Link>
        <Link href="#" className="hover:text-teal-500">
          License
        </Link>
      </div>
    </footer>
  );
}
