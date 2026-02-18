import { FiMoreVertical } from "react-icons/fi";

export default function ProjectsHeader() {
  return (
    <div className="flex items-center justify-between mb-6">
      <div>
        <h3 className="text-sm font-semibold text-gray-800">
          Projects
        </h3>
        <p className="text-xs text-green-500">
          30 done this month
        </p>
      </div>

      <FiMoreVertical className="text-gray-400 cursor-pointer" />
    </div>
  );
}
