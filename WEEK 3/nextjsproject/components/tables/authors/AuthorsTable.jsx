
"use client";

import AuthorRow from "./AuthorRow";
import { authorsData } from "./data";

export default function AuthorsTable() {
  return (
    <div className="bg-white rounded-xl shadow-sm overflow-hidden">
      
      
      <div className="px-6 py-5">
        <h2 className="text-lg font-semibold text-gray-900">
          Authors Table
        </h2>
      </div>

      
      <div className="overflow-x-auto">
        <table className="w-full border-collapse">
          <thead>
            <tr className="text-left text-xs font-semibold text-gray-400 uppercase border-t border-gray-100">
              <th className="py-3 px-6">Author</th>
              <th className="py-3 px-6">Function</th>
              <th className="py-3 px-6">Status</th>
              <th className="py-3 px-6">Employed</th>
              <th className="py-3 px-6"></th>
            </tr>
          </thead>

          <tbody>
            {authorsData.map((author) => (
              <AuthorRow key={author.id} author={author} />
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
