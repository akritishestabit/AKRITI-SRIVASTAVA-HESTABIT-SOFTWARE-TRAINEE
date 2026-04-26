import {
  FiCheckCircle,
  FiArrowUpCircle,
  FiAlertCircle,
  FiXCircle,
} from "react-icons/fi";

const iconMap = {
  success: {
    icon: <FiCheckCircle />,
    color: "text-green-500",
  },
  info: {
    icon: <FiArrowUpCircle />,
    color: "text-teal-500",
  },
  warning: {
    icon: <FiAlertCircle />,
    color: "text-orange-400",
  },
  error: {
    icon: <FiXCircle />,
    color: "text-red-500",
  },
};

export default function OrderItem({ order }) {
  const { icon, color } = iconMap[order.type];

  return (
    <div className="flex items-start gap-3">
      
      {/* ICON */}
      <span className={`text-lg ${color}`}>
        {icon}
      </span>

      {/* TEXT */}
      <div>
        <p className="text-sm font-medium text-gray-800">
          {order.title}
        </p>
        <p className="text-xs text-gray-400 mt-1">
          {order.date}
        </p>
      </div>
    </div>
  );
}
