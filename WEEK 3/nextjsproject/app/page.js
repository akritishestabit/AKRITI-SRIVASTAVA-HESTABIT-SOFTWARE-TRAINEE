// // app/page.js
// import { redirect } from "next/navigation";

// export default function HomePage() {
//   redirect("/dashboard");
// }
// export default function Home() {
//   return (
//     <div className="h-screen flex items-center justify-center">
//       <a
//         href="/dashboard"
//         className="px-6 py-3 bg-teal-500 text-white rounded-lg"
//       >
//         Go to Dashboard
//       </a>
//     </div>
//   );
// }
"use client";

import Link from "next/link";
import { FiArrowRight } from "react-icons/fi";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 flex items-center justify-center px-6">
      
      <div className="text-center max-w-2xl">

        {/* Heading */}
        <h1 className="text-4xl md:text-5xl font-bold text-gray-800 leading-tight">
          Welcome to <span className="text-teal-500">Purity UI Dashboard</span>
        </h1>

        {/* Subtext */}
        <p className="mt-6 text-gray-600 text-lg">
          A modern and modular dashboard built with Next.js and Tailwind CSS.
          Clean structure. Scalable components. Professional UI.
        </p>

        {/* Buttons */}
        <div className="mt-10 flex flex-col sm:flex-row gap-4 justify-center">

          <Link
            href="/dashboard"
            className="inline-flex items-center justify-center gap-2 px-6 py-3 bg-teal-500 hover:bg-teal-600 text-white font-medium rounded-xl transition shadow-md"
          >
            Go to Dashboard
            <FiArrowRight />
          </Link>

          <Link
            href="/auth/signin"
            className="px-6 py-3 border border-gray-300 text-gray-700 hover:bg-gray-100 font-medium rounded-xl transition"
          >
            Sign In
          </Link>

        </div>

      </div>

    </div>
  );
}

