

import CreditCard from "./CreditCard";
import SalaryCard from "./SalaryCard";
import PaypalCard from "./PaypalCard";
import InvoicesCard from "./InvoicesCard";
import PaymentMethodSection from "./PaymentMethodSection";

export default function TopCardsSection() {
  return (
    <div className="grid grid-cols-12 gap-6">

      
      <div className="col-span-12 lg:col-span-5">
        <CreditCard />
      </div>

    
      <div className="col-span-12 lg:col-span-3 grid grid-cols-2 gap-6">
        <SalaryCard />
        <PaypalCard />
      </div>

      
      <div className="col-span-12 lg:col-span-4 row-span-2">
        <InvoicesCard />
      </div>

      
      <div className="col-span-12 lg:col-span-8">
        <PaymentMethodSection />
      </div>

    </div>
  );
}
