"use client";

import {
  FiDollarSign,
  FiUsers,
  FiUserPlus,
  FiShoppingCart,
} from "react-icons/fi";

import StatCard from "./StatCard";

export default function StatsGrid() {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-6">
      
      <StatCard
        title="Today's Money"
        value="$53,000"
        percentage="+55%"
        isPositive
        icon={<FiDollarSign size={18} />}
      />

      <StatCard
        title="Today's Users"
        value="2,300"
        percentage="+5%"
        isPositive
        icon={<FiUsers size={18} />}
      />

      <StatCard
        title="New Clients"
        value="+3,052"
        percentage="-14%"
        isPositive={false}
        icon={<FiUserPlus size={18} />}
      />

      <StatCard
        title="Total Sales"
        value="$173,000"
        percentage="+8%"
        isPositive
        icon={<FiShoppingCart size={18} />}
      />
    </div>
  );
}
