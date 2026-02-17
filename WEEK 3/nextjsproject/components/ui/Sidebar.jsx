"use client";

import Image from "next/image";
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
  return (
    <aside className="w-64 min-h-screen bg-white flex flex-col">
      <div className="px-6 py-6 flex items-center gap-2">
        <Image src="/logo.svg" alt="Purity UI Logo" width={28} height={28} />
        <span className="text-sm font-bold tracking-wide text-gray-800">
          PURITY UI DASHBOARD
        </span>
      </div>

      <nav className="px-3 space-y-1">
        <SidebarItem icon={FiHome} label="Dashboard" active />
        <SidebarItem icon={FiTable} label="Tables" />
        <SidebarItem icon={FiCreditCard} label="Billing" />
        <SidebarItem icon={FiRepeat} label="RTL" />

        <div className="mt-6 mb-2 px-3 text-xs font-semibold text-gray-800 uppercase">
          Account Pages
        </div>

        <SidebarItem icon={FiUser} label="Profile" />
        <SidebarItem icon={FiLogIn} label="Sign In" />
        <SidebarItem icon={FiUserPlus} label="Sign Up" />
      </nav>

      <div className="mt-16">
        <SidebarHelp />
      </div>
    </aside>
  );
}
