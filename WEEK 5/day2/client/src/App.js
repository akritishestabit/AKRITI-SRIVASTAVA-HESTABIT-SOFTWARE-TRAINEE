import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("Loading...");
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:5000");
        const data = await response.text();
        setMessage(data);
      } catch (err) {
        setError("Failed to connect to backend");
        console.log(err);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>React Client</h1>
      {error ? <p>{error}</p> : <p>{message}</p>}
    </div>
  );
}

export default App;
