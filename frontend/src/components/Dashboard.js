import React, { useState, useEffect } from "react";
import axios from "axios";

const setTwitterUsername = async (username) => {
  try {
    const response = await axios.post('/api/set_twitter', { username });
    alert(response.data.message);
  } catch (error) {
    console.error('Error setting Twitter username:', error);
    alert('Failed to set Twitter username.');
  }
};


const Dashboard = () => {
  const [tokens, setTokens] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch token data from the backend API
    const fetchTokens = async () => {
      try {
        const response = await axios.get("/api/tokens");
        setTokens(response.data);
      } catch (error) {
        console.error("Error fetching tokens:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchTokens();
  }, []);

  if (loading) {
    return <div className="text-center text-xl">Loading tokens...</div>;
  }

  return (
      <div className="p-6">
        <h1 className="text-2xl font-bold mb-4">Token Dashboard</h1>
        {tokens.length === 0 ? (
            <div className="text-center text-lg">No tokens found.</div>
        ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {tokens.map((token) => (
                  <div
                      key={token.contract}
                      className="p-4 bg-white border rounded shadow"
                  >
                    <div>
                      <h2 className="font-semibold text-lg">{token.contract}</h2>
                      <p>Liquidity: ${token.liquidity}</p>
                      <p>Market Cap: {token.marketCap}</p>
                      <a
                          href={token.tweetLink}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-blue-500 underline"
                      >
                        View Tweet
                      </a>
                    </div>
                  </div>
              ))}
            </div>
        )}
        <form
            onSubmit={(e) => {
              e.preventDefault();
              const formData = new FormData(e.target);
              setTwitterUsername(formData.get('username'));
            }}
            className="mb-4"
        >
          <input
              type="text"
              name="username"
              placeholder="Enter Twitter username"
              className="border p-2 rounded mr-2"
              required
          />
          <button type="submit" className="bg-green-600 text-white px-4 py-2 rounded">
            Set Username
          </button>
        </form>
        <button
            onClick={() => window.location.reload()}
            className="mt-6 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
        >
          Refresh
        </button>
      </div>
  );
};

export default Dashboard;
