import { useState } from "react";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const checkVibe = async () => {
  setLoading(true);
  setError("");

  try {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        text: text,
      }),
    });

    const data = await response.json();
    console.log(data);
    setResult(data);
  } catch (err) {
    setError("Could not connect to the server.");
  }

  setLoading(false);
};
  return (
  <div>
    <h1>VibeCheck</h1>

    <input
      type="text"
      placeholder="How are you feeling today?"
      value={text}
      onChange={(e) => setText(e.target.value)}
    />

    <br />
    <br />

    <button onClick={checkVibe} disabled={loading}>
      {loading ? "Checking..." : "Check My Vibe"}
    </button>
    {error && (
  <p style={{ color: "red" }}>
    {error}
  </p>
)}

    {result && (
      <div>
        <h2>Emotion: {result.emotion}</h2>
        <p>Confidence: {result.confidence}</p>

        <h2>Recommended Songs</h2>

        {result.tracks.map((track, index) => (
          <div
            key={index}
            style={{
              border: "1px solid gray",
              padding: "10px",
              margin: "10px",
            }}
          >
            <img
              src={track.cover_image || "https://via.placeholder.com/150"}
              alt={track.song}
              width="120"
            />

            <h3>{track.song}</h3>
            <p>{track.artist}</p>

            <a
              href={track.url}
              target="_blank"
              rel="noreferrer"
            >
              Listen on Last.fm
            </a>
          </div>
        ))}
      </div>
    )}
  </div>
);}

export default App;