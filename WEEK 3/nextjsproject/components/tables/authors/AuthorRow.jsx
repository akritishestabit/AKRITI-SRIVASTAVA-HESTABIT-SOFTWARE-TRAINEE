// components/tables/authors/AuthorRow.jsx
import Image from "next/image";

export default function AuthorRow({ author }) {
  const isOnline = author.status === "Online";

  return (
    <tr className="border-t border-gray-100">
      
      {/* AUTHOR */}
      <td className="py-4 px-6">
        <div className="flex items-center gap-3">
          <Image
            src={author.avatar}
            alt={author.name}
            width={36}
            height={36}
            className="rounded-full"
          />
          <div>
            <p className="text-sm font-semibold text-gray-900">
              {author.name}
            </p>
            <p className="text-xs text-gray-500">
              {author.email}
            </p>
          </div>
        </div>
      </td>

      {/* FUNCTION */}
      <td className="py-4 px-6">
        <p className="text-sm font-semibold text-gray-900">
          {author.role}
        </p>
        <p className="text-xs text-gray-500">
          {author.department}
        </p>
      </td>

      {/* STATUS */}
      <td className="py-4 px-6">
        <span
          className={`px-3 py-1 text-xs font-semibold rounded-full
            ${
              isOnline
                ? "bg-green-100 text-green-600"
                : "bg-gray-100 text-gray-500"
            }
          `}
        >
          {author.status}
        </span>
      </td>

      {/* EMPLOYED */}
      <td className="py-4 px-6 text-sm font-semibold text-gray-700">
        {author.employed}
      </td>

      {/* ACTION */}
      <td className="py-4 px-6 text-sm text-gray-500 cursor-pointer hover:text-teal-500">
        Edit
      </td>
    </tr>
  );
}
