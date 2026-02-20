import "../globals.css";
import Sidebar from "../../components/ui/Sidebar";

export const metadata = {
  title: "Purity Dashboard",
  description: "Next.js + Tailwind Dashboard Layout",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="bg-gray-100">
        <div className="flex min-h-screen">

          
          <Sidebar />

          
          <div className="flex flex-col flex-1">

           
            <main className="flex-1 p-6">
              {children}
            </main>

            
            <footer className="px-10 py-4 text-sm text-gray-500 flex justify-between items-center bg-gray-100">
              <p>
                © 2021, Made with ❤️ by Akriti Srivastava for Hestabit Software.
              </p>

              <div className="flex gap-6">
                <span className="cursor-pointer hover:text-gray-700 transition">
                  Akriti
                </span>
                <span className="cursor-pointer hover:text-gray-700 transition">
                  Simmmple
                </span>
                <span className="cursor-pointer hover:text-gray-700 transition">
                  Blog
                </span>
                <span className="cursor-pointer hover:text-gray-700 transition">
                  License
                </span>
              </div>
            </footer>

          </div>

        </div>
      </body>
    </html>
  );
}
