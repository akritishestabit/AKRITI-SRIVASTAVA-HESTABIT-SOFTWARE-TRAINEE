import ProjectsHeader from "./ProjectsHeader";
import ProjectsTable from "./ProjectsTable";

export default function ProjectsCard() {
  return (
    <div className="bg-white rounded-xl p-6 shadow-sm">
      <ProjectsHeader />
      <ProjectsTable />
    </div>
  );
}
