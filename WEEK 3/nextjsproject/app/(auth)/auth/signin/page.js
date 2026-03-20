import AuthNavbar from "@/components/auth/AuthNavbar";
import SignInForm from "@/components/auth/SignInForm";
import AuthRightPanel from "@/components/auth/AuthRightPanel";
import AuthFooter from "@/components/auth/AuthFooter";

export default function SignInPage() {
  return (
    <div className="relative min-h-screen bg-gray-50 overflow-hidden">
      <AuthNavbar />

      <div className="flex min-h-screen">
        <div className="w-1/2 flex items-center justify-center pt-24">
          <SignInForm />
        </div>

        <div className="w-1/2">
          <AuthRightPanel />
        </div>
      </div>

      <AuthFooter />
    </div>
  );
}
