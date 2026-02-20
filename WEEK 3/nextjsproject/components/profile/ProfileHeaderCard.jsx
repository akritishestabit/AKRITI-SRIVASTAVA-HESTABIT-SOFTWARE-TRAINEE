"use client";

import Image from "next/image";
import { FiEdit } from "react-icons/fi";
import { useState } from "react";

export default function ProfileHeaderCard() {
  const [activeTab, setActiveTab] = useState("overview");

  const tabs = [
    { id: "overview", label: "Overview" },
    { id: "teams", label: "Teams" },
    { id: "projects", label: "Projects" },
  ];

  return (
    <div className="relative -mt-16 z-20">
      <div
        className="w-full bg-white/80 backdrop-blur-md 
                   rounded-2xl shadow-md 
                   px-6 py-6 flex items-center justify-between"
      >
        
        <div className="flex items-center gap-5">
          
         
          <div className="relative">
            <Image
              src="/profile_header_Image.png"   
              alt="Profile"
              width={80}
              height={80}
              className="rounded-xl object-cover"
            />

            
            <button
              className="absolute -bottom-2 -right-2 
                         w-8 h-8 rounded-full bg-white 
                         shadow flex items-center justify-center 
                         hover:bg-gray-100 transition"
            >
              <FiEdit className="text-teal-500 text-sm" />
            </button>
          </div>

          
          <div>
            <h2 className="text-lg font-semibold text-gray-800">
              Esthera Jackson
            </h2>
            <p className="text-sm text-gray-500">
              esthera@simmmple.com
            </p>
          </div>
        </div>

        
        <div className="flex items-center gap-3">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`px-5 py-2 rounded-full text-sm font-medium transition
                ${
                  activeTab === tab.id
                    ? "bg-gray-900 text-white"
                    : "bg-gray-100 text-gray-600 hover:bg-gray-200"
                }`}
            >
              {tab.label}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
