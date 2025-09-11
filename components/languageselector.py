import React from 'react';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Globe } from "lucide-react";

const languages = [
  { code: 'hindi', name: 'हिंदी', flag: '🇮🇳' },
  { code: 'english', name: 'English', flag: '🇬🇧' },
  { code: 'tamil', name: 'தமிழ்', flag: '🇮🇳' },
  { code: 'telugu', name: 'తెలుగు', flag: '🇮🇳' },
  { code: 'bengali', name: 'বাংলা', flag: '🇧🇩' },
  { code: 'marathi', name: 'मराठी', flag: '🇮🇳' },
  { code: 'gujarati', name: 'ગુજરાતી', flag: '🇮🇳' },
  { code: 'punjabi', name: 'ਪੰਜਾਬੀ', flag: '🇮🇳' },
  { code: 'kannada', name: 'ಕನ್ನಡ', flag: '🇮🇳' },
  { code: 'malayalam', name: 'മലയാളം', flag: '🇮🇳' }
];

export default function LanguageSelector({ selectedLanguage, onLanguageChange, className = "" }) {
  return (
    <div className={`flex items-center gap-3 ${className}`}>
      <Globe className="w-5 h-5 text-orange-600" />
      <Select value={selectedLanguage} onValueChange={onLanguageChange}>
        <SelectTrigger className="w-48 border-orange-200 focus:border-orange-400">
          <SelectValue placeholder="भाषा चुनें" />
        </SelectTrigger>
        <SelectContent>
          {languages.map((lang) => (
            <SelectItem key={lang.code} value={lang.code}>
              <div className="flex items-center gap-2">
                <span>{lang.flag}</span>
                <span className="hindi-font">{lang.name}</span>
              </div>
            </SelectItem>
          ))}
        </SelectContent>
      </Select>
    </div>
  );
}