"use client";

export default function ToggleSwitch({ enabled, onChange }) {
  return (
    <button
      onClick={onChange}
      className={`w-10 h-5 rounded-full flex items-center px-1 transition
        ${enabled ? "bg-teal-400" : "bg-gray-300"}`}
    >
      <span
        className={`w-4 h-4 bg-white rounded-full shadow transform transition
          ${enabled ? "translate-x-5" : ""}`}
      />
    </button>
  );
}
