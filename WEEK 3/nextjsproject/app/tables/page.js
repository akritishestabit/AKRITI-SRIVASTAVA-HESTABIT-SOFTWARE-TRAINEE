//app/tables/page.js
import AuthorsTable from "../../components/tables/authors/AuthorsTable";
import ProjectsCard from "../../components/dashboard/section4/ProjectsCard"; 

export default function TablesPage() {
  return (
    <div className="space-y-12">
      <AuthorsTable />

    
      <div className="xl:col-span-2">
                <ProjectsCard />
              </div>
    </div>
  );
}
