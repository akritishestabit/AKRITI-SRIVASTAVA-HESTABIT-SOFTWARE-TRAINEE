

import Link from "next/link";
import { usePathname } from "next/navigation";

export default function SidebarItem({ icon: Icon, label, href }) {
  const pathname = usePathname();
  const isActive = pathname === href;

  return (
    <Link href={href}>
      <div
        className={`flex items-center gap-3 px-4 py-3 rounded-xl cursor-pointer transition
          ${
            isActive
              ? "bg-white text-gray-900 shadow-sm font-semibold"
              : "text-gray-500 hover:bg-white"
          }
        `}
      >
        <Icon className="text-teal-500 text-lg" />
        <span className="text-sm">{label}</span>
      </div>
    </Link>
  );
}
