import TopCardsSection from "@/components/billing/TopCardsSection";
import BillingInformationSection from "@/components/billing/BillingInformationSection";
import TransactionsSection from "@/components/billing/TransactionsSection";

export default function BillingPage() {
  return (
    
        <div className="p-6 space-y-6">
      <TopCardsSection />
      <div className="mt-6 grid grid-cols-12 gap-6">

  <div className="col-span-12 lg:col-span-8">
    <BillingInformationSection />
  </div>

  <div className="col-span-12 lg:col-span-4">
    
    <TransactionsSection />
  </div>

</div>
    </div>
      
    
    
  );
}
