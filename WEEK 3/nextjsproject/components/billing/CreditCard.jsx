"use client";

export default function CreditCard() {
  return (
    <div
      className="relative h-[200px] rounded-2xl p-6 text-white
                 bg-gradient-to-br from-[#1a1f37] via-[#202940] to-[#111827]
                 overflow-hidden shadow-lg"
    >
      
      <div className="absolute inset-0 opacity-10">
        <svg
          viewBox="0 0 800 800"
          className="w-full h-full"
          xmlns="http://www.w3.org/2000/svg"
        >
          <circle cx="600" cy="200" r="250" stroke="white" strokeWidth="1" fill="none" />
          <circle cx="650" cy="250" r="180" stroke="white" strokeWidth="1" fill="none" />
          <circle cx="700" cy="300" r="120" stroke="white" strokeWidth="1" fill="none" />
        </svg>
      </div>

      
      <div className="relative z-10 flex justify-between items-start">
        <h3 className="text-lg font-semibold">Purity UI</h3>

        
        <div className="flex items-center">
          <div className="w-8 h-8 bg-gray-400 rounded-full opacity-80"></div>
          <div className="w-8 h-8 bg-gray-300 rounded-full -ml-3 opacity-80"></div>
        </div>
      </div>

      
      <div className="relative z-10 mt-8 text-xl tracking-widest font-medium">
        7812 2139 0823 XXXX
      </div>

     
      <div className="relative z-10 flex justify-between mt-6 text-sm opacity-80">
        <div>
          <p className="uppercase text-xs opacity-60">Valid Thru</p>
          <p>05/24</p>
        </div>

        <div>
          <p className="uppercase text-xs opacity-60">CVV</p>
          <p>09X</p>
        </div>
      </div>
    </div>
  );
}
