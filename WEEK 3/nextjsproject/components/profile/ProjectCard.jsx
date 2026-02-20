"use client";

import Image from "next/image";

export default function ProjectCard({ image, title, description }) {
  return (
    <div className="bg-white rounded-2xl shadow-md overflow-hidden">
      
      
      <div className="relative h-40 w-full">
        <Image
          src={image}
          alt={title}
          fill
          className="object-cover"
        />
      </div>

      
      <div className="p-5">
        <p className="text-xs text-gray-400 uppercase mb-1">
          Project
        </p>

        <h4 className="text-sm font-semibold text-gray-800 mb-2">
          {title}
        </h4>

        <p className="text-xs text-gray-500 mb-4 leading-relaxed">
          {description}
        </p>

        <button className="text-xs font-semibold text-teal-500 hover:underline">
          VIEW ALL
        </button>
      </div>
    </div>
  );
}
