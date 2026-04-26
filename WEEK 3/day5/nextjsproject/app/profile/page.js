import ProfileHero from "@/components/profile/ProfileHero";
import ProfileHeaderCard from "@/components/profile/ProfileHeaderCard";
import PlatformSettingsCard from "@/components/profile/PlatformSettingsCard";
import ProfileInformationCard from "@/components/profile/ProfileInformationCard";
import ConversationsCard from "@/components/profile/ConversationsCard";
import ProjectsSection from "@/components/profile/ProjectsSection";

export default function ProfilePage() {
  return (
    <div className="p-4">
      <ProfileHero />
      <div className="px-6">
        <ProfileHeaderCard />
        
      </div> 
      <div className="py-4 grid grid-cols-3 gap-6">
          <PlatformSettingsCard />
          <ProfileInformationCard/>
          <ConversationsCard />
        </div>
       <div className="" >

        <ProjectsSection />
       </div>
       
    </div>
    
  );
}
