"use client";

export default function BuiltByDevelopers() {
  return (
    <div className="bg-white rounded-xl p-6 shadow-sm flex justify-between items-stretch h-70">
      
      
      <div className="flex flex-col justify-between max-w-sm">
        
        
        <div>
          <p className="text-xs text-gray-400 font-semibold uppercase">
            Built by developers
          </p>

          <h3 className="mt-2 text-lg font-semibold text-gray-900">
            Purity UI Dashboard
          </h3>

          <p className="mt-2 text-sm text-gray-500 leading-relaxed">
            From colors, cards, typography to complex elements, you will
            find the full documentation.
          </p>
        </div>

        
        <button className="text-sm font-medium text-gray-900 flex items-center gap-1 hover:underline">
          Read more
          <span className="text-lg">→</span>
        </button>
      </div>

    
      <div className="w-80 rounded-xl bg-teal-400 flex items-center justify-center">
        <span className="text-white text-xl font-semibold">
          chakra
        </span>
      </div>
    </div>
  );
}
