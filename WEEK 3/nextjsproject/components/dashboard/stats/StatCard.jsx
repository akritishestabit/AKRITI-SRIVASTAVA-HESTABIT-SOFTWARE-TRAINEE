"use client";

export default function StatCard({
  title,
  value,
  percentage,
  isPositive = true,
  icon,
}) {
  return (
    <div className="bg-white rounded-xl px-5 py-4 flex items-center justify-between shadow-sm">
      
      {/* LEFT CONTENT */}
      <div>
        <p className="text-xs text-gray-400 font-medium">{title}</p>

        <div className="flex items-center gap-2 mt-1">
          <h3 className="text-lg font-semibold text-gray-900">
            {value}
          </h3>

          <span
            className={`text-xs font-medium ${
              isPositive ? "text-green-500" : "text-red-500"
            }`}
          >
            {percentage}
          </span>
        </div>
      </div>

      {/* RIGHT ICON */}
      <div className="w-11 h-11 rounded-lg bg-teal-400 flex items-center justify-center text-white">
        {icon}
      </div>
    </div>
  );
}
