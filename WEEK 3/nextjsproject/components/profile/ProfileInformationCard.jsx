"use client";

import { FaFacebook, FaTwitter, FaInstagram } from "react-icons/fa";

export default function ProfileInformationCard() {
  return (
    <div className="bg-white rounded-2xl shadow-md p-6">
      
      
      <h3 className="text-lg font-semibold text-gray-800 mb-3">
        Profile Information
      </h3>

     
      <p className="text-sm text-gray-500 leading-relaxed mb-5">
        Hi, I’m Alec Thompson, Decisions: If you can’t decide, the answer is no.
        If two equally difficult paths, choose the one more painful in the short
        term (pain avoidance is creating an illusion of equality).
      </p>

      <div className="border-t border-gray-200 my-4" />

      
      <div className="space-y-3 text-sm text-gray-600">
        
        <InfoRow label="Full Name" value="Alec M. Thompson" />
        <InfoRow label="Mobile" value="(44) 123 1234 123" />
        <InfoRow label="Email" value="alecthompson@mail.com" />
        <InfoRow label="Location" value="United States" />

        
        <div className="flex items-center gap-3 pt-2">
          <span className="font-medium text-gray-700">
            Social:
          </span>
          <div className="flex gap-3 text-teal-500">
            <FaFacebook className="cursor-pointer hover:text-teal-600 transition" />
            <FaTwitter className="cursor-pointer hover:text-teal-600 transition" />
            <FaInstagram className="cursor-pointer hover:text-teal-600 transition" />
          </div>
        </div>

      </div>
    </div>
  );
}




function InfoRow({ label, value }) {
  return (
    <div className="flex gap-2">
      <span className="font-medium text-gray-700">
        {label}:
      </span>
      <span className="text-gray-500">
        {value}
      </span>
    </div>
  );
}
