"use client";

export default function AuthRightPanel() {
  return (
    
      <div className="h-220 w-240 relative overflow-hidden flex items-center justify-center
                rounded-l-[40px]
                bg-gradient-to-br from-teal-400 via-teal-500 to-teal-600">


      
      <div className="absolute inset-0 opacity-25">
        <svg
          className="w-full h-full"
          viewBox="0 0 800 800"
          xmlns="http://www.w3.org/2000/svg"
        >
          <defs>
            <linearGradient id="wave" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#ffffff" stopOpacity="0.5" />
              <stop offset="100%" stopColor="#ffffff" stopOpacity="0" />
            </linearGradient>
          </defs>

          <path
            d="M-50,350 C200,250 450,550 900,300"
            fill="none"
            stroke="url(#wave)"
            strokeWidth="100"
          />
          <path
            d="M-50,500 C250,450 500,700 900,550"
            fill="none"
            stroke="url(#wave)"
            strokeWidth="80"
          />
        </svg>
      </div>

      
      <div className="relative z-10 flex items-center gap-6">
        <div className="w-16 h-16 bg-white rounded-full flex items-center justify-center shadow-md">
          <svg
            width="32"
            height="32"
            viewBox="0 0 24 24"
            fill="none"
            stroke="#14b8a6"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
          </svg>
        </div>

        <span className="text-white text-4xl font-bold tracking-wide">
          chakra
        </span>
      </div>
    </div>
  );
}
