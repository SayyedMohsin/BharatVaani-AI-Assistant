import React, { useState, useEffect } from "react";
import { UserProfile } from "@/entities/all";
import { User } from "@/entities/User";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Switch } from "@/components/ui/switch";
import { Settings as SettingsIcon, Save, User as UserIcon, Globe } from "lucide-react";
import { motion } from "framer-motion";
import LanguageSelector from "../components/LanguageSelector";

export default function SettingsPage() {
  const [userProfile, setUserProfile] = useState({
    preferred_language: 'hindi',
    location: '',
    phone_number: '',
    upi_id: '',
    voice_enabled: true
  });
  const [user, setUser] = useState(null);
  const [isSaving, setIsSaving] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    loadUserData();
  }, []);

  const loadUserData = async () => {
    try {
      const currentUser = await User.me();
      setUser(currentUser);

      const profiles = await UserProfile.filter({ created_by: currentUser.email });
      if (profiles.length > 0) {
        setUserProfile(profiles[0]);
      }
    } catch (error) {
      console.error('Error loading user data:', error);
    }
    setIsLoading(false);
  };

  const handleSaveProfile = async () => {
    setIsSaving(true);
    try {
      const existingProfiles = await UserProfile.filter({ created_by: user.email });
      
      if (existingProfiles.length > 0) {
        await UserProfile.update(existingProfiles[0].id, userProfile);
      } else {
        await UserProfile.create(userProfile);
      }
      
      alert('सेटिंग्स सफलतापूर्वक सेव हो गईं!');
    } catch (error) {
      console.error('Error saving profile:', error);
      alert('सेटिंग्स सेव करने में समस्या हुई।');
    }
    setIsSaving(false);
  };

  if (isLoading) {
    return (
      <div className="min-h-screen p-8 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-orange-600 mx-auto mb-4"></div>
          <p className="hindi-font text-gray-600">लोड हो रहा है...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen p-4 md:p-8">
      <div className="max-w-4xl mx-auto space-y-8">
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center space-y-4"
        >
          <h1 className="text-3xl md:text-5xl font-bold bg-gradient-to-r from-purple-600 via-blue-600 to-green-600 bg-clip-text text-transparent hindi-font">
            सेटिंग्स
          </h1>
          <p className="text-lg text-gray-700 hindi-font">
            अपनी प्राथमिकताएं और प्रोफाइल सेटअप करें
          </p>
        </motion.div>

        <div className="grid lg:grid-cols-2 gap-8">
          {/* User Profile */}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.2 }}
          >
            <Card className="border-2 border-blue-200 bg-blue-50/30">
              <CardHeader>
                <CardTitle className="flex items-center gap-3 hindi-font">
                  <UserIcon className="w-6 h-6 text-blue-600" />
                  उपयोगकर्ता प्रोफाइल
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                {user && (
                  <div className="p-4 bg-white rounded-lg space-y-2">
                    <p className="hindi-font"><strong>नाम:</strong> {user.full_name}</p>
                    <p className="hindi-font"><strong>ईमेल:</strong> {user.email}</p>
                    <p className="hindi-font"><strong>भूमिका:</strong> {user.role}</p>
                  </div>
                )}
                
                <div className="space-y-2">
                  <Label htmlFor="location" className="hindi-font font-medium">
                    स्थान (शहर/गांव)
                  </Label>
                  <Input
                    id="location"
                    value={userProfile.location}
                    onChange={(e) => setUserProfile({...userProfile, location: e.target.value})}
                    placeholder="अपना स्थान दर्ज करें"
                    className="hindi-font border-blue-200 focus:border-blue-400"
                  />
                </div>

                <div className="space-y-2">
                  <Label htmlFor="phone" className="hindi-font font-medium">
                    फोन नंबर
                  </Label>
                  <Input
                    id="phone"
                    value={userProfile.phone_number}
                    onChange={(e) => setUserProfile({...userProfile, phone_number: e.target.value})}
                    placeholder="+91 9876543210"
                    className="border-blue-200 focus:border-blue-400"
                  />
                </div>

                <div className="space-y-2">
                  <Label htmlFor="upi" className="hindi-font font-medium">
                    UPI ID
                  </Label>
                  <Input
                    id="upi"
                    value={userProfile.upi_id}
                    onChange={(e) => setUserProfile({...userProfile, upi_id: e.target.value})}
                    placeholder="आपकी UPI ID"
                    className="border-blue-200 focus:border-blue-400"
                  />
                </div>
              </CardContent>
            </Card>
          </motion.div>

          {/* App Settings */}
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.4 }}
          >
            <Card className="border-2 border-green-200 bg-green-50/30">
              <CardHeader>
                <CardTitle className="flex items-center gap-3 hindi-font">
                  <SettingsIcon className="w-6 h-6 text-green-600" />
                  ऐप सेटिंग्स
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <div className="space-y-3">
                  <Label className="hindi-font font-medium flex items-center gap-2">
                    <Globe className="w-4 h-4" />
                    प्राथमिक भाषा
                  </Label>
                  <LanguageSelector
                    selectedLanguage={userProfile.preferred_language}
                    onLanguageChange={(lang) => setUserProfile({...userProfile, preferred_language: lang})}
                  />
                </div>

                <div className="flex items-center justify-between p-4 bg-white rounded-lg">
                  <div>
                    <p className="font-medium hindi-font">वॉइस कमांड्स</p>
                    <p className="text-sm text-gray-600 hindi-font">
                      आवाज़ से कमांड देने की सुविधा
                    </p>
                  </div>
                  <Switch
                    checked={userProfile.voice_enabled}
                    onCheckedChange={(checked) => setUserProfile({...userProfile, voice_enabled: checked})}
                  />
                </div>

                <div className="p-4 bg-orange-50 border-l-4 border-orange-400 rounded">
                  <h4 className="font-semibold hindi-font text-orange-800 mb-2">सुविधाएं:</h4>
                  <ul className="text-sm text-orange-700 hindi-font space-y-1">
                    <li>• 10+ भारतीय भाषाओं का समर्थन</li>
                    <li>• वॉइस-टू-टेक्स्ट और टेक्स्ट-टू-वॉइस</li>
                    <li>• ऑफलाइन बेसिक कमांड्स</li>
                    <li>• सरकारी योजनाओं की जानकारी</li>
                  </ul>
                </div>
              </CardContent>
            </Card>
          </motion.div>
        </div>

        {/* Developer Info */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.6 }}
        >
          <Card className="border-2 border-purple-200 bg-purple-50/30">
            <CardHeader>
              <CardTitle className="hindi-font">डेवलपर की जानकारी</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <h4 className="font-semibold hindi-font mb-3">संपर्क विवरण:</h4>
                  <div className="space-y-2 text-sm">
                    <p><strong>नाम:</strong> Sayyed Mohsin Ali</p>
                    <p><strong>ईमेल:</strong> smohsin32@yahoo.in</p>
                    <p><strong>फोन:</strong> +919765335549</p>
                  </div>
                </div>
                <div>
                  <h4 className="font-semibold hindi-font mb-3">तकनीकी स्टैक:</h4>
                  <div className="text-sm space-y-1">
                    <p>• OpenAI Whisper (आवाज़ की पहचान)</p>
                    <p>• GPT-4o (भाषा मॉडल)</p>
                    <p>• Google TTS (आवाज़ संश्लेषण)</p>
                    <p>• Python FastAPI + Firebase</p>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </motion.div>

        {/* Save Button */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.8 }}
          className="text-center"
        >
          <Button
            onClick={handleSaveProfile}
            disabled={isSaving}
            className="px-8 py-3 bg-gradient-to-r from-orange-600 to-red-600 hover:from-orange-700 hover:to-red-700 text-white font-semibold rounded-xl shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-200"
          >
            <Save className="w-5 h-5 mr-2" />
            <span className="hindi-font">
              {isSaving ? 'सेव हो रहा है...' : 'सेटिंग्स सेव करें'}
            </span>
          </Button>
        </motion.div>
      </div>
    </div>
  );
}