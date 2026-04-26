import StatsGrid from "../../components/dashboard/stats/StatsGrid";
import BuiltByDevelopers from "../../components/dashboard/promo/BuiltByDevelopers";
import WorkWithRockets from "../../components/dashboard/promo/WorkWithRockets";
import ActiveUsersCard from "../../components/dashboard/section3/ActiveUsersCard";
import SalesOverviewCard from "../../components/dashboard/section3/SalesOverviewCard";
import ProjectsCard from "../../components/dashboard/section4/ProjectsCard";
import OrdersOverview from "../../components/dashboard/section5/OrdersOverview";

export default function DashboardPage() {
  return (
    <div className="space-y-6">
      <StatsGrid />

      <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
        <div className="xl:col-span-2">
          <BuiltByDevelopers />
        </div>
        <div className="xl:col-span-1">
          <WorkWithRockets />
        </div>
      </div>

      
      <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
        <div className="xl:col-span-1">
          <ActiveUsersCard />
        </div>
        <div className="xl:col-span-2">
          <SalesOverviewCard />
        </div>
      </div>

      <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
        
        
        <div className="xl:col-span-2">
          <ProjectsCard />
        </div>

        <div className="bg-white rounded-xl shadow-sm" >
          <OrdersOverview />
        </div>
      </div>
    </div>
  );
}
