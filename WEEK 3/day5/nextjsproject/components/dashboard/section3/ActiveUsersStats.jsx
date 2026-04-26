import {
  FiUsers,
  FiMousePointer,
  FiShoppingCart,
  FiBox,
} from "react-icons/fi";

const stats = [
  { label: "Users", value: "32,984", progress: 75, icon: <FiUsers /> },
  { label: "Clicks", value: "2.42m", progress: 60, icon: <FiMousePointer /> },
  { label: "Sales", value: "$2,400", progress: 80, icon: <FiShoppingCart /> },
  { label: "Items", value: "320", progress: 45, icon: <FiBox /> },
];

export default function ActiveUsersStats() {
  return (
    <div className="grid grid-cols-4 gap-6 text-sm">
      {stats.map((item, i) => (
        <div key={i}>
          
          
          <div className="flex items-center gap-1 text-teal-500 text-xs">
            {item.icon}
            <span>{item.label}</span>
          </div>

          
          <p className="mt-1 font-semibold text-gray-900">
            {item.value}
          </p>

          
          <div className="mt-2 h-1 w-full bg-gray-200 rounded">
            <div
              className="h-full bg-teal-400 rounded"
              style={{ width: `${item.progress}%` }}
            />
          </div>
        </div>
      ))}
    </div>
  );
}
