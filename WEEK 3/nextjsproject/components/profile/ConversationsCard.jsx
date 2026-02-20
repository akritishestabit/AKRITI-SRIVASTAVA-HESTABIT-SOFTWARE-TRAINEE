"use client";

import Image from "next/image";

const conversations = [
  {
    id: 1,
    name: "Esthera Jackson",
    message: "Hi! I need more information...",
    avatar: "/conversation1.png",
  },
  {
    id: 2,
    name: "Alexa Liras",
    message: "Awesome work, can you help me?",
    avatar: "/conversation2.png",
  },
  {
    id: 3,
    name: "Laurent Perrier",
    message: "About files I can...",
    avatar: "/conversation3.png",
  },
  {
    id: 4,
    name: "Michael Levi",
    message: "Have a great afternoon...",
    avatar: "/conversation4.png",
  },
];

export default function ConversationsCard() {
  return (
    <div className="bg-white rounded-2xl shadow-md p-6">
      
      
      <h3 className="text-lg font-semibold text-gray-800 mb-6">
        Conversations
      </h3>

      
      <div className="space-y-5">
        {conversations.map((item) => (
          <ConversationRow key={item.id} {...item} />
        ))}
      </div>
    </div>
  );
}



function ConversationRow({ name, message, avatar }) {
  return (
    <div className="flex items-center justify-between">
      
      
      <div className="flex items-center gap-3">
        <Image
          src={avatar}
          alt={name}
          width={40}
          height={40}
          className="rounded-xl object-cover"
        />
        <div>
          <p className="text-sm font-medium text-gray-800">
            {name}
          </p>
          <p className="text-xs text-gray-500">
            {message}
          </p>
        </div>
      </div>

      
      <button className="text-xs font-semibold text-teal-500 hover:underline">
        REPLY
      </button>
    </div>
  );
}
