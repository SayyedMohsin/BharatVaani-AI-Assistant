
import React, { useState, useEffect } from "react";
import { VoiceCommand, UserProfile } from "@/entities/all";
import { User } from "@/entities/User";
import { InvokeLLM } from "@/integrations/Core";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Sparkles, MessageCircle, Type, Trash2 } from "lucide-react";
import { motion } from "framer-motion";

import UniversalInput from "../components/UniversalInput";
import LanguageSelector from "../components/LanguageSelector";
import ResponseDisplay from "../components/ResponseDisplay";

export default function HomePage() {
  const [selectedLanguage, setSelectedLanguage] = useState('hindi');
  const [isProcessing, setIsProcessing] = useState(false);
  const [currentResponse, setCurrentResponse] = useState('');
  const [recentCommands, setRecentCommands] = useState([]);
  const [userProfile, setUserProfile] = useState(null);

  useEffect(() => {
    loadUserProfile();
    loadRecentCommands();
  }, []);

  const loadUserProfile = async () => {
    try {
      const user = await User.me();
      const profiles = await UserProfile.filter({ created_by: user.email });
      if (profiles.length > 0) {
        setUserProfile(profiles[0]);
        setSelectedLanguage(profiles[0].preferred_language || 'hindi');
      }
    } catch (error) {
      console.log('User not logged in or no profile found');
    }
  };

  const loadRecentCommands = async () => {
    try {
      const commands = await VoiceCommand.list('-created_date', 5);
      setRecentCommands(commands);
    } catch (error) {
      console.error('Error loading commands:', error);
    }
  };

  const handleDeleteCommand = async (commandId) => {
    try {
      await VoiceCommand.delete(commandId);
      loadRecentCommands(); // Refresh list after deleting
    } catch (error) {
      console.error("Failed to delete command:", error);
      alert("कमांड हटाने में विफल रहा।");
    }
  };

  const handleCommandSubmit = async (commandText) => {
    setIsProcessing(true);
    setCurrentResponse('');

    try {
      // Process text command with AI
      const prompt = `
      यह एक भारतीय भाषाओं का AI असिस्टेंट है। उपयोगकर्ता का सवाल है: "${commandText}"
      Language: ${selectedLanguage}
      
      कृपया इस सवाल का जवाब दें।
      
      यदि सवाल है:
      - UPI/पेमेंट के बारे में: UPI की विस्तृत जानकारी दें, कैसे इस्तेमाल करें, सुरक्षा टिप्स दें
      - सरकारी योजनाओं के बारे में: योजना की पूरी जानकारी, आवेदन प्रक्रिया, पात्रता मापदंड दें
      - मौसम के बारे में: सामान्य मौसम की जानकारी और सुझाव दें
      - स्थानीय सेवाओं के बारे में: कैसे ढूंढें और संपर्क करें इसकी जानकारी दें
      - स्वास्थ्य के बारे में: सामान्य स्वास्थ्य सुझाव दें (डॉक्टर से सलाह लेने की सलाह भी दें)
      - सामान्य सवाल: उपयुक्त और विस्तृत जवाब दें
      
      जवाब ${selectedLanguage} भाषा में दें और भारतीय संदर्भ में रखें।
      जवाब व्यावहारिक और उपयोगी हो।
      `;

      const aiResponse = await InvokeLLM({
        prompt: prompt,
        add_context_from_internet: true
      });

      // Save command to database
      await VoiceCommand.create({
        command_text: commandText,
        language: selectedLanguage,
        category: "general",
        response_text: aiResponse,
        status: "completed"
      });

      setCurrentResponse(aiResponse);
      loadRecentCommands();

    } catch (error) {
      console.error('Error processing command:', error);
      setCurrentResponse('माफ करें, आपके सवाल को प्रोसेस करने में समस्या हुई है। कृपया दोबारा कोशिश करें।');
    }

    setIsProcessing(false);
  };

  const quickCommands = [
    {
      text: "मेरा UPI बैलेंस कैसे चेक करूं?",
      icon: "💳",
      category: "upi"
    },
    {
      text: "आज का मौसम कैसा है?",
      icon: "🌤️",
      category: "weather"
    },
    {
      text: "नजदीकी अस्पताल कैसे ढूंढूं?",
      icon: "🏥",
      category: "local_services"
    },
    {
      text: "राशन कार्ड के लिए आवेदन कैसे करें?",
      icon: "🆔",
      category: "government_schemes"
    }
  ];

  const handleQuickCommand = async (command) => {
    await handleCommandSubmit(command.text);
  };

  return (
    <div className="min-h-screen p-4 md:p-8">
      <div className="max-w-6xl mx-auto space-y-8">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center space-y-4"
        >
          <h1 className="text-4xl md:text-6xl font-bold bg-gradient-to-r from-orange-600 via-red-500 to-green-600 bg-clip-text text-transparent hindi-font">
            नमस्ते! BharatVaani में आपका स्वागत है
          </h1>
          <p className="text-xl text-gray-700 hindi-font max-w-3xl mx-auto">
            भारतीय भाषाओं में सवाल पूछें और अपनी दैनिक समस्याओं का समाधान पाएं
          </p>
          
          <LanguageSelector 
            selectedLanguage={selectedLanguage}
            onLanguageChange={setSelectedLanguage}
            className="justify-center"
          />
        </motion.div>

        <div className="grid lg:grid-cols-2 gap-8">
          {/* Universal Input */}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.2 }}
          >
            <UniversalInput
              onCommandSubmit={handleCommandSubmit}
              isProcessing={isProcessing}
              language={selectedLanguage}
            />
          </motion.div>

          {/* Quick Commands */}
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.4 }}
            className="space-y-4"
          >
            <h3 className="text-xl font-bold text-gray-900 hindi-font">
              त्वरित कमांड्स
            </h3>
            <div className="grid gap-3">
              {quickCommands.map((command, index) => (
                <Button
                  key={index}
                  onClick={() => handleQuickCommand(command)}
                  disabled={isProcessing}
                  variant="outline"
                  className="justify-start h-auto p-4 border-2 border-orange-200 hover:border-orange-300 hover:bg-orange-50 transition-all duration-200"
                >
                  <span className="text-2xl mr-3">{command.icon}</span>
                  <span className="hindi-font font-medium">{command.text}</span>
                </Button>
              ))}
            </div>
          </motion.div>
        </div>

        {/* Response Display */}
        {currentResponse && (
          <ResponseDisplay 
            response={currentResponse}
            language={selectedLanguage}
          />
        )}

        {/* Recent Commands */}
        {recentCommands.length > 0 && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.6 }}
          >
            <Card className="border-2 border-blue-200 bg-white/80 backdrop-blur-sm">
              <CardHeader>
                <CardTitle className="flex items-center gap-3 hindi-font">
                  <MessageCircle className="w-6 h-6 text-blue-600" />
                  हाल की कमांड्स
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-3">
                  {recentCommands.map((command) => (
                    <div key={command.id} className="flex items-center justify-between p-3 bg-blue-50 rounded-lg">
                      <div className="hindi-font flex-1">
                        <p className="font-medium text-gray-900">{command.command_text}</p>
                        <p className="text-sm text-gray-600 capitalize">{command.language} • {command.category}</p>
                      </div>
                      <Button
                        variant="ghost"
                        size="icon"
                        onClick={() => handleDeleteCommand(command.id)}
                        className="text-red-500 hover:bg-red-100"
                      >
                        <Trash2 className="w-5 h-5" />
                      </Button>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </motion.div>
        )}

        {/* Features */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.8 }}
          className="grid md:grid-cols-3 gap-6"
        >
          <Card className="text-center border-2 border-orange-200 hover:border-orange-300 transition-colors">
            <CardContent className="p-6">
              <Type className="w-12 h-12 text-orange-600 mx-auto mb-4" />
              <h3 className="font-bold text-lg hindi-font mb-2">वॉइस और टेक्स्ट</h3>
              <p className="text-gray-600 hindi-font">बोलें या टाइप करें, आपकी मर्जी</p>
            </CardContent>
          </Card>

          <Card className="text-center border-2 border-green-200 hover:border-green-300 transition-colors">
            <CardContent className="p-6">
              <Sparkles className="w-12 h-12 text-green-600 mx-auto mb-4" />
              <h3 className="font-bold text-lg hindi-font mb-2">AI समाधान</h3>
              <p className="text-gray-600 hindi-font">दैनिक समस्याओं का तुरंत समाधान</p>
            </CardContent>
          </Card>

          <Card className="text-center border-2 border-blue-200 hover:border-blue-300 transition-colors">
            <CardContent className="p-6">
              <MessageCircle className="w-12 h-12 text-blue-600 mx-auto mb-4" />
              <h3 className="font-bold text-lg hindi-font mb-2">10+ भाषाएं</h3>
              <p className="text-gray-600 hindi-font">भारत की सभी मुख्य भाषाओं का समर्थन</p>
            </CardContent>
          </Card>
        </motion.div>
      </div>
    </div>
  );
}
