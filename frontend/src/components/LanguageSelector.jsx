import { languages } from '../languages';

export default function LanguageSelector({ lang, setLang }) {
  return (
    <select
      value={lang}
      onChange={(e) => setLang(e.target.value)}
      className="border-2 border-orange-400 rounded px-3 py-2 text-sm bg-white shadow"
    >
      {languages.map((l) => (
        <option key={l.code} value={l.code}>
          {l.flag} {l.name}
        </option>
      ))}
    </select>
  );
}