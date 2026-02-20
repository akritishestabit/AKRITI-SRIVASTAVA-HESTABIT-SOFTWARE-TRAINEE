// import AuthNavbar from "@/components/auth/AuthNavbar";
// import SignInForm from "@/components/auth/SignInForm";
// import AuthRightPanel from "@/components/auth/AuthRightPanel";
// import AuthFooter from "@/components/auth/AuthFooter";

// export default function SignInPage() {
//   return (
//     <>
//       <AuthNavbar />

//       <div className="flex min-h-[calc(100vh-120px)]">
//         {/* LEFT */}
//         <div className="w-1/2 flex items-center justify-center">
//           <SignInForm />
//         </div>

//         {/* RIGHT */}
//         <div className="w-1/2">
//           <AuthRightPanel />
//         </div>
//       </div>

//       <AuthFooter />
//     </>
//   );
// }

import AuthNavbar from "@/components/auth/AuthNavbar";
import SignInForm from "@/components/auth/SignInForm";
import AuthRightPanel from "@/components/auth/AuthRightPanel";
import AuthFooter from "@/components/auth/AuthFooter";

export default function SignInPage() {
  return (
    <div className="relative min-h-screen bg-gray-50 overflow-hidden">
      
      {/* FLOATING NAVBAR */}
      <AuthNavbar />

      {/* MAIN CONTENT */}
      <div className="flex min-h-screen">
        
        {/* LEFT SIDE */}
        <div className="w-1/2 flex items-center justify-center pt-24">
          <SignInForm />
        </div>

        {/* RIGHT SIDE */}
        <div className="w-1/2">
          <AuthRightPanel />
        </div>

      </div>

      <AuthFooter />
    </div>
  );
}
