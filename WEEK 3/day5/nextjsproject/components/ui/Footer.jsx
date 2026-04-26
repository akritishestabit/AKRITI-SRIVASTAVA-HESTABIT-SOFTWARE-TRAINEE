export default function Footer() {
  return (
    <footer className="mt-8 py-4 text-center text-xs text-gray-500">
      © {new Date().getFullYear()} made with ❤️ by{" "}
      <span className="font-medium text-gray-700">
        Akriti Srivastava
      </span>
    </footer>
  );
}
