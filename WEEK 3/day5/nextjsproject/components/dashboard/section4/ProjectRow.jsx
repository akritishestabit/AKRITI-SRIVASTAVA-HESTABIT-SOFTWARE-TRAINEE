export default function ProjectRow({ project }) {
  return (
    <div className="grid grid-cols-4 items-center text-sm">
      
      
      <div className="flex items-center gap-2 font-medium text-gray-800">
        <span>{project.icon}</span>
        <span>{project.name}</span>
      </div>

     
      <div className="flex -space-x-2">
        {Array.from({ length: project.members }).map((_, i) => (
          <div
            key={i}
            className="w-6 h-6 rounded-full bg-gray-200 border border-white"
          />
        ))}
      </div>

      
      <div className="text-black-600">
        {project.budget}
      </div>

      
      <div>
        <p className="text-xs text-gray-600 mb-1">
          {project.completion}%
        </p>
        <div className="h-1 w-full bg-gray-200 rounded">
          <div
            className="h-full bg-teal-400 rounded"
            style={{ width: `${project.completion}%` }}
          />
        </div>
      </div>
    </div>
  );
}
