import { useState } from 'react';
import LanguageSelector from '../components/LanguageSelector';

export default function Home() {
  const [text, setText] = useState('');
  const [answer, setAnswer] = useState('');
  const [lang, setLang] = useState('hi');
  const [loading, setLoading] = useState(false);

  const ask = async () => {
    if (!text.trim()) return;
    setLoading(true);
    try {
      const res = await fetch('http://localhost:8000/api/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, language: lang }),
      });
      const data = await res.json();
      setAnswer(data.answer);
    } catch {
      setAnswer('कुछ गलत हो गया।');
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-orange-50 via-white to-green-50 p-6 flex flex-col items-center">
      <div className="max-w-2xl w-full space-y-6">
        <h1 className="text-4xl font-bold text-center text-orange-600 hindi-font">
          नमस्ते! BharatVaani AI
        </h1>

        <LanguageSelector lang={lang} setLang={setLang} />

        <textarea
          rows={4}
          className="w-full border-2 border-orange-300 rounded-lg p-3 hindi-font"
          placeholder="अपना सवाल यहाँ लिखें..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        <button
          onClick={ask}
          disabled={loading}
          className="w-full py-3 px-6 bg-orange-600 text-white rounded-lg shadow hover:bg-orange-700 disabled:opacity-60"
        >
          {loading ? 'प्रोसेसिंग...' : 'पूछें'}
        </button>

        {answer && (
          <div className="p-4 bg-green-100 border-l-4 border-green-500 rounded shadow-md">
            <p className="text-gray-800 hindi-font">{answer}</p>
          </div>
        )}
      </div>
    </div>
  );
}