"use client";

import BillingInfoCard from "./BillingInfoCard";

export default function BillingInformationSection() {
  return (
    <div className="bg-white rounded-2xl p-6 shadow-md">

      
      <h2 className="text-lg font-semibold text-gray-800 mb-6">
        Billing Information
      </h2>

      
      <div className="space-y-6">

        <BillingInfoCard
          name="Oliver Liam"
          company="Viking Burrito"
          email="oliver@burrito.com"
          vat="FRB1235476"
        />

        <BillingInfoCard
          name="Oliver Liam"
          company="Viking Burrito"
          email="oliver@burrito.com"
          vat="FRB1235476"
        />

        <BillingInfoCard
          name="Oliver Liam"
          company="Viking Burrito"
          email="oliver@burrito.com"
          vat="FRB1235476"
        />

      </div>
    </div>
  );
}
