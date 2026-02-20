 import "../globals.css";
 import Sidebar from "../../components/ui/Sidebar";
 import Navbar from "../../components/ui/Navbar";
 import Footer from "../../components/ui/Footer";

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
             
               <Footer />
            
           </div>
         </div>
       </body>
     </html>
   );
 }
// import "./globals.css";
// import Sidebar from "../components/ui/Sidebar";
// import Navbar from "../components/ui/Navbar";
// import Footer from "../components/ui/Footer";

// export const metadata = {
//   title: "Purity Dashboard",
//   description: "Next.js + Tailwind Dashboard Layout",
// };

// export default function RootLayout({ children }) {
//   return (
//     <html lang="en">
//       <body className="bg-gray-100">
//         <div className="flex min-h-screen">
          
//           {/* Sidebar */}
//           <Sidebar />

//           {/* Right Section */}
//           <div className="flex flex-col flex-1">
            
//             {/* Navbar */}
//             <Navbar />

//             {/* Page Content */}
//             <main className="p-6 flex-1">
//               {children}
//             </main>

//             {/* Footer (COMMON FOR ALL PAGES) */}
//             <Footer />

//           </div>
//         </div>
//       </body>
//     </html>
//   );
// }
