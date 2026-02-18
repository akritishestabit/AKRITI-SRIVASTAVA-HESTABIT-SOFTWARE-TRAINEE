// export default function SidebarItem({ icon: Icon, label, active }) {
//   return (
//     <div
//       className={`flex items-center gap-3 px-4 py-3 rounded-lg cursor-pointer transition
//         ${
//           active
//             ? "bg-white text-gray-900 font-semibold shadow-xl"
//             : "text-gray-600 hover:bg-white hover:text-gray-900 hover:shadow-sm"
//         }
//       `}
//     >
//       <Icon className="text-lg text-teal-500" />
//       <span className="text-sm">{label}</span>
//     </div>
//   );
// }


// import Link from "next/link";

// export default function SidebarItem({ icon: Icon, label, href, active }) {
//   return (
//     <Link href={href}>
//       <div
//         className={`flex items-center gap-3 px-4 py-2 rounded-lg text-sm cursor-pointer transition-all
//           ${
//             active
//               ? "bg-white text-gray-900 shadow-md"
//               : "text-gray-500 hover:bg-white hover:shadow-sm"
//           }
//         `}
//       >
//         <Icon
//           className={`text-lg ${
//             active ? "text-teal-500" : "text-teal-400"
//           }`}
//         />
//         <span className={`${active ? "font-semibold" : "font-medium"}`}>
//           {label}
//         </span>
//       </div>
//     </Link>
//   );
// }

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
