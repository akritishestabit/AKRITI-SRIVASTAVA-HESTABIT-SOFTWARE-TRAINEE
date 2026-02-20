"use client";

import { useState } from "react";

export default function PlatformSettingsCard() {

  const [settings, setSettings] = useState({
    followEmail: true,
    answerEmail: false,
    mentionEmail: true,
    newLaunch: false,
    monthlyUpdates: false,
    newsletter: true,
  });

  const toggle = (key) => {
    setSettings((prev) => ({
      ...prev,
      [key]: !prev[key],
    }));
  };

  const Switch = ({ active, onClick }) => (
    <button
      onClick={onClick}
      className={`w-10 h-5 rounded-full flex items-center px-1 transition ${
        active ? "bg-teal-400" : "bg-gray-300"
      }`}
    >
      <span
        className={`w-4 h-4 bg-white rounded-full transform transition ${
          active ? "translate-x-5" : ""
        }`}
      />
    </button>
  );

  return (
    <div className="bg-white rounded-2xl shadow-sm p-6">

      <h3 className="font-semibold text-gray-700 mb-6">
        Platform Settings
      </h3>

      <div className="space-y-4 text-sm">

        <div className="flex justify-between items-center">
          <span>Email me when someone follows me</span>
          <Switch
            active={settings.followEmail}
            onClick={() => toggle("followEmail")}
          />
        </div>

        <div className="flex justify-between items-center">
          <span>Email me when someone answers</span>
          <Switch
            active={settings.answerEmail}
            onClick={() => toggle("answerEmail")}
          />
        </div>

        <div className="flex justify-between items-center">
          <span>Email me when someone mentions me</span>
          <Switch
            active={settings.mentionEmail}
            onClick={() => toggle("mentionEmail")}
          />
        </div>

        <div className="flex justify-between items-center">
          <span>New launches and projects</span>
          <Switch
            active={settings.newLaunch}
            onClick={() => toggle("newLaunch")}
          />
        </div>

        <div className="flex justify-between items-center">
          <span>Monthly product updates</span>
          <Switch
            active={settings.monthlyUpdates}
            onClick={() => toggle("monthlyUpdates")}
          />
        </div>

        <div className="flex justify-between items-center">
          <span>Subscribe to newsletter</span>
          <Switch
            active={settings.newsletter}
            onClick={() => toggle("newsletter")}
          />
        </div>

      </div>
    </div>
  );
}
