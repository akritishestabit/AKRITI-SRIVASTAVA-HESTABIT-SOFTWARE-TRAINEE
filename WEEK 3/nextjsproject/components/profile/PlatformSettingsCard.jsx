"use client";

import { useState } from "react";
import ToggleSwitch from "./ToggleSwitch";

export default function PlatformSettingsCard() {
  const [settings, setSettings] = useState({
    emailFollows: true,
    emailAnswers: false,
    emailMentions: true,
    newLaunches: false,
    monthlyUpdates: false,
    newsletter: true,
  });

  const toggle = (key) => {
    setSettings((prev) => ({
      ...prev,
      [key]: !prev[key],
    }));
  };

  return (
    <div className="bg-white rounded-2xl shadow-md p-6">
      
      <h3 className="text-lg font-semibold text-gray-800 mb-6">
        Platform Settings
      </h3>

      
      <div className="mb-6">
        <p className="text-xs font-semibold text-gray-400 uppercase mb-4">
          Account
        </p>

        <div className="space-y-4">
          <SettingRow
            label="Email me when someone follows me"
            enabled={settings.emailFollows}
            onToggle={() => toggle("emailFollows")}
          />
          <SettingRow
            label="Email me when someone answers on my post"
            enabled={settings.emailAnswers}
            onToggle={() => toggle("emailAnswers")}
          />
          <SettingRow
            label="Email me when someone mentions me"
            enabled={settings.emailMentions}
            onToggle={() => toggle("emailMentions")}
          />
        </div>
      </div>

      {/* APPLICATION SECTION */}
      <div>
        <p className="text-xs font-semibold text-gray-400 uppercase mb-4">
          Application
        </p>

        <div className="space-y-4">
          <SettingRow
            label="New launches and projects"
            enabled={settings.newLaunches}
            onToggle={() => toggle("newLaunches")}
          />
          <SettingRow
            label="Monthly product updates"
            enabled={settings.monthlyUpdates}
            onToggle={() => toggle("monthlyUpdates")}
          />
          <SettingRow
            label="Subscribe to newsletter"
            enabled={settings.newsletter}
            onToggle={() => toggle("newsletter")}
          />
        </div>
      </div>
    </div>
  );
}



function SettingRow({ label, enabled, onToggle }) {
  return (
    <div className="flex items-center justify-between">
      <span className="text-sm text-gray-600">
        {label}
      </span>
      <ToggleSwitch enabled={enabled} onChange={onToggle} />
    </div>
  );
}
