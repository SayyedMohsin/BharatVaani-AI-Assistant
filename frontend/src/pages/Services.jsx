import { useState } from 'react';
import LanguageSelector from '../components/LanguageSelector';

export default function Services() {
  const [query, setQuery] = useState('');
  const [answer, setAnswer] = useState('');
  const [lang, setLang] = useState('hi');

  const ask = async (q) => {
    const prompt = `भारतीय संदर्भ में ${q} के बारे में ${lang} में छोटा जवाब दो`;
    const res = await fetch('http://localhost:8000/api/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: prompt, language: lang }),
    });
    const data = await res.json();
    setAnswer(data.answer);
  };

  const categories = ['UPI', 'सरकारी योजनाएं', 'शिक्षा', 'मौसम', 'स्वास्थ्य'];

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50 p-6">
      <div className="max-w-4xl mx-auto space-y-6">
        <h1 className="text-4xl font-bold text-center text-blue-600 hindi-font">सभी सेवाएं</h1>
        <LanguageSelector lang={lang} setLang={setLang} />

        <div className="grid md:grid-cols-3 gap-4">
          {categories.map((c) => (
            <button
              key={c}
              onClick={() => ask(c)}
              className="p-4 bg-white border-2 border-blue-300 rounded-lg shadow hover:bg-blue-50"
            >
              {c}
            </button>
          ))}
        </div>

        <textarea
          rows={3}
          className="w-full border-2 border-blue-300 rounded-lg p-3"
          placeholder="और सवाल लिखें..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button
          onClick={() => ask(query)}
          className="w-full py-3 px-6 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700"
        >
          खोजें
        </button>

        {answer && (
          <div className="p-4 bg-blue-100 border-l-4 border-blue-500 rounded shadow-md">
            <p className="whitespace-pre-wrap hindi-font">{answer}</p>
          </div>
        )}
      </div>
    </div>
  );
}