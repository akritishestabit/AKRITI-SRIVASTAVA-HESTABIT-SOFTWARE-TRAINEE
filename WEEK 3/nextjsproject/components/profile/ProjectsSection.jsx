"use client";

import ProjectCard from "./ProjectCard";

export default function ProjectsSection() {
  const projects = [
    {
      id: 1,
      image: "/project1.png",
      title: "Modern",
      description:
        "As Uber works through a huge amount of internal management turmoil.",
    },
    {
      id: 2,
      image: "/project2.png",
      title: "Scandinavian",
      description:
        "Music is something that every person has his or her own specific opinion about.",
    },
    {
      id: 3,
      image: "/project3.png",
      title: "Minimalist",
      description:
        "Different people have different taste, and various types of music.",
    },
  ];

  return (
    <div className="mt-6">
      
      
      <div className="mb-6">
        <h3 className="text-lg font-semibold text-gray-800">
          Projects
        </h3>
        <p className="text-sm text-gray-500">
          Architects design houses
        </p>
      </div>

      
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
        
        {projects.map((project) => (
          <ProjectCard key={project.id} {...project} />
        ))}

        
        <div className="bg-white rounded-2xl shadow-md flex items-center justify-center border-2 border-dashed border-gray-200 hover:border-teal-400 transition cursor-pointer">
          <div className="text-center p-6">
            <div className="w-10 h-10 mx-auto mb-3 rounded-full bg-gray-100 flex items-center justify-center text-gray-500 text-lg">
              +
            </div>
            <p className="text-sm font-medium text-gray-600">
              Create New Project
            </p>
          </div>
        </div>

      </div>
    </div>
  );
}
