"use client";

import ActiveUsersStats from "./ActiveUsersStats";

export default function ActiveUsersCard() {
  return (
    <div className="bg-white rounded-xl shadow-sm overflow-hidden p-4 h-110" >
      
      
<div className="rounded-xl bg-gradient-to-br from-slate-800 to-slate-900 p-10 relative">
  
  
  <div className="absolute left-6 top-8 bottom-10 flex flex-col justify-between text-xs text-white/100">
    <span>500</span>
    <span>400</span>
    <span>300</span>
    <span>200</span>
    <span>100</span>
    <span>0</span>
  </div>

  <div className="flex items-end justify-between h-40 ml-10">
    {[280, 220, 160, 260, 210, 300, 240, 180].map((value, i) => (
      <div
        key={i}
        className="w-2 rounded bg-white/90"
        style={{ height: `${value / 2}px` }}
      />
    ))}
  </div>
</div>


      
      <div className="px-6 pt-4">
        <h3 className="text-sm font-semibold text-gray-800">
          Active Users
        </h3>
        <p className="text-xs text-green-500 mt-1">
          (+23) than last week
        </p>
      </div>

      
      <div className="px-6 py-8">
        <ActiveUsersStats />
      </div>
    </div>
  );
}
