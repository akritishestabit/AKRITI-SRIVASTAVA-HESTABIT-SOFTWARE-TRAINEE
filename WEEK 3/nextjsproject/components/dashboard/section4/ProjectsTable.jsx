import { projects } from "./data";
import ProjectRow from "./ProjectRow";

export default function ProjectsTable() {
  return (
    <div>
      
      <div className="grid grid-cols-4 text-xs text-gray-400 font-semibold pb-3 border-b">
        <span>COMPANIES</span>
        <span>MEMBERS</span>
        <span>BUDGET</span>
        <span>COMPLETION</span>
      </div>

      
      <div className="mt-4 space-y-4">
        {projects.map((project, i) => (
          <ProjectRow key={i} project={project} />
        ))}
      </div>
    </div>
  );
}
