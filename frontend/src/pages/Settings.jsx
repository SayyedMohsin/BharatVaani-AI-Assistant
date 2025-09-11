import { useState, useEffect } from 'react';
import { languages } from '../languages';

export default function Settings() {
  const [profile, setProfile] = useState({
    email: 'user@example.com',
    preferred_language: 'hi',
    location: '',
    phone_number: '',
    upi_id: '',
    voice_enabled: true,
  });
  const [saved, setSaved] = useState(false);

  useEffect(() => {
    fetch(`http://localhost:8000/api/profile/${profile.email}`)
      .then((r) => r.json())
      .then((d) => setProfile({ ...profile, ...d }));
  }, []);

  const save = async () => {
    await fetch('http://localhost:8000/api/profile', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(profile),
    });
    setSaved(true);
    setTimeout(() => setSaved(false), 2000);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-white to-pink-50 p-6">
      <div className="max-w-2xl mx-auto space-y-6">
        <h1 className="text-4xl font-bold text-center text-purple-600 hindi-font">सेटिंग्स</h1>

        <div>
          <label className="block font-medium">भाषा चुनें</label>
          <select
            value={profile.preferred_language}
            onChange={(e) => setProfile({ ...profile, preferred_language: e.target.value })}
            className="w-full border-2 border-purple-300 rounded-lg p-2 mt-1"
          >
            {languages.map((l) => (
              <option key={l.code} value={l.code}>
                {l.flag} {l.name}
              </option>
            ))}
          </select>
        </div>

        {['location', 'phone_number', 'upi_id'].map((key) => (
          <div key={key}>
            <label className="block font-medium">{key.replace('_', ' ')}</label>
            <input
              className="w-full border-2 border-purple-300 rounded-lg p-2 mt-1"
              value={profile[key]}
              onChange={(e) => setProfile({ ...profile, [key]: e.target.value })}
            />
          </div>
        ))}

        <label className="flex items-center gap-2">
          <input
            type="checkbox"
            checked={profile.voice_enabled}
            onChange={(e) => setProfile({ ...profile, voice_enabled: e.target.checked })}
          />
          वॉइस कमांड चालू
        </label>

        <button
          onClick={save}
          className="w-full py-3 px-6 bg-purple-600 text-white rounded-lg shadow hover:bg-purple-700"
        >
          {saved ? 'सेव हो गई!' : 'सेव करें'}
        </button>
      </div>
    </div>
  );
}