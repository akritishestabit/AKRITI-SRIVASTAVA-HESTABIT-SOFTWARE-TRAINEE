// // app/page.js
// import { redirect } from "next/navigation";

// export default function HomePage() {
//   redirect("/dashboard");
// }
export default function Home() {
  return (
    <div className="h-screen flex items-center justify-center">
      <a
        href="/dashboard"
        className="px-6 py-3 bg-teal-500 text-white rounded-lg"
      >
        Go to Dashboard
      </a>
    </div>
  );
}
