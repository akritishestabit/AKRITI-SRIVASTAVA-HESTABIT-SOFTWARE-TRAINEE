"use client";

import Image from "next/image";

export default function WorkWithRockets() {
  return (
    <div className="relative rounded-xl overflow-hidden shadow-sm  w-full h-70">
      
      
      <Image
        src="/images/back.png"
        alt="Work with the Rockets"
        fill
        priority
        quality={100}
        sizes="(max-width: 1280px) 100vw, 50vw"
        className="object-cover object-center"
      />

    
      <div className="absolute inset-0 bg-black/50 flex flex-col justify-between p-5">
        
        
        <div>
          <h3 className="text-white text-lg font-semibold">
            Work with the Rockets
          </h3>

          <p className="mt-2 text-sm text-gray-200 leading-relaxed max-w-md">
            Wealth creation is an evolutionarily recent positive-sum game.
            It is all about who takes the opportunity first.
          </p>
        </div>

    
        <button className="text-sm font-medium text-white flex items-center gap-1 hover:underline">
          Read more
          <span className="text-lg">→</span>
        </button>
      </div>
    </div>
  );
}
