export default function SidebarItem({ icon: Icon, label, active }) {
  return (
    <div
      className={`flex items-center gap-3 px-4 py-3 rounded-lg cursor-pointer transition
        ${
          active
            ? "bg-white text-gray-900 font-semibold shadow-xl"
            : "text-gray-600 hover:bg-white hover:text-gray-900 hover:shadow-sm"
        }
      `}
    >
      <Icon className="text-lg text-teal-500" />
      <span className="text-sm">{label}</span>
    </div>
  );
}
