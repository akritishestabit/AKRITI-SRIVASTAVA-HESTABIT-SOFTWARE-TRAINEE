 import "../globals.css";
 import Sidebar from "../../components/ui/Sidebar";
 import Navbar from "../../components/ui/Navbar";


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
             <Navbar />

             <main className="p-6 flex-1">{children}</main>
             
               {/* <Footer /> */}
               <footer className="px-10 mb-2 text-sm text-gray-500 flex justify-between items-center bg-gray-100">
              <p>
                © 2021, Made with ❤️ Akriti Srivastava by Hestabit Software. 
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

