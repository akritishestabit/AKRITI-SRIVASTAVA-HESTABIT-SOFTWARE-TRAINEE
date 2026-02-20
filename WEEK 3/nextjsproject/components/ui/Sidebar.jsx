"use client";

import Image from "next/image";
import { usePathname } from "next/navigation";
import {
  FiHome,
  FiTable,
  FiCreditCard,
  FiRepeat,
  FiUser,
  FiLogIn,
  FiUserPlus,
} from "react-icons/fi";

import SidebarItem from "./SidebarItem";
import SidebarHelp from "./SidebarHelp";

export default function Sidebar() {
  const pathname = usePathname(); 

  return (
    <aside className="w-64 min-h-screen bg-white flex flex-col">
      
      {/* LOGO */}
      <div className="px-6 py-6 flex items-center gap-2">
        <Image src="/logo.svg" alt="Purity UI Logo" width={28} height={28} />
        <span className="text-sm font-bold tracking-wide text-gray-800">
          PURITY UI DASHBOARD
        </span>
      </div>

      {/* NAV */}
      <nav className="px-3 space-y-1">
        <SidebarItem
          icon={FiHome}
          label="Dashboard"
          href="/dashboard"
          active={pathname === "/dashboard"}
        />

        <SidebarItem
          icon={FiTable}
          label="Tables"
          href="/tables"
          active={pathname === "/tables"}
        />

        <SidebarItem
          icon={FiCreditCard}
          label="Billing"
          href="/billing"
          active={pathname === "/billing"}
        />

        <SidebarItem
          icon={FiRepeat}
          label="RTL"
          href="/rtl"
          active={pathname === "/rtl"}
        />

        <div className="mt-6 mb-2 px-3 text-xs font-semibold text-gray-800 uppercase">
          Account Pages
        </div>

        <SidebarItem
          icon={FiUser}
          label="Profile"
          href="/profile"
          active={pathname === "/profile"}
        />

        <SidebarItem
          icon={FiLogIn}
          label="Sign In"
          href="/auth/signin"
          active={pathname === "/signin"}
        />

        <SidebarItem
          icon={FiUserPlus}
          label="Sign Up"
          href="/auth/signup"
          active={pathname === "/signup"}
        />
      </nav>

      <div className="mt-16">
        <SidebarHelp />
      </div>
    </aside>
  );
}
