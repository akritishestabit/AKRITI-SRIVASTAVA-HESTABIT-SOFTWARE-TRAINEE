"use client";

import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const data = [
  { month: "Jan", sales: 120 },
  { month: "Feb", sales: 90 },
  { month: "Mar", sales: 160 },
  { month: "Apr", sales: 140 },
  { month: "May", sales: 200 },
  { month: "Jun", sales: 170 },
  { month: "Jul", sales: 220 },
  { month: "Aug", sales: 190 },
  { month: "Sep", sales: 260 },
  { month: "Oct", sales: 210 },
];

export default function SalesOverviewCard() {
  return (
    <div className="bg-white rounded-xl p-6 shadow-sm h-110">
      
      <h3 className="text-sm font-semibold text-gray-800">
        Sales overview
      </h3>

      <p className="text-xs text-green-500 mt-1">
        (+5%) more in 2021
      </p>

      <div className="h-64 mt-6">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={data}>
            <XAxis dataKey="month" />
            <YAxis />
            <Tooltip />
            <Area
              type="monotone"
              dataKey="sales"
              stroke="#14b8a6"
              fill="#99f6e4"
              strokeWidth={2}
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
