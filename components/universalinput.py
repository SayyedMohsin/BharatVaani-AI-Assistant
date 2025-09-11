import React, { useState, useRef, useEffect } from 'react';
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Send, Mic, MicOff } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

export default function UniversalInput({ onCommandSubmit, isProcessing, language }) {
  const [commandText, setCommandText] = useState('');
  const [isListening, setIsListening] = useState(false);
  const recognitionRef = useRef(null);

  const langMap = {
    'hindi': 'hi-IN',
    'english': 'en-US',
    'tamil': 'ta-IN',
    'telugu': 'te-IN',
    'bengali': 'bn-IN',
    'marathi': 'mr-IN',
    'gujarati': 'gu-IN',
    'punjabi': 'pa-IN',
    'kannada': 'kn-IN',
    'malayalam': 'ml-IN'
  };

  const handleMicClick = () => {
    if (isListening) {
      recognitionRef.current.stop();
      return;
    }

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      alert("माफ करें, आपका ब्राउज़र वॉइस रिकग्निशन का समर्थन नहीं करता है।");
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = langMap[language] || 'hi-IN';
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onstart = () => setIsListening(true);
    recognition.onend = () => setIsListening(false);
    recognition.onerror = (event) => {
      console.error("Speech recognition error", event.error);
      setIsListening(false);
    };

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setCommandText(transcript);
    };

    recognitionRef.current = recognition;
    recognition.start();
  };

  useEffect(() => {
    return () => {
      if (recognitionRef.current) {
        recognitionRef.current.stop();
      }
    };
  }, []);

  const handleSubmit = () => {
    if (commandText.trim()) {
      onCommandSubmit(commandText);
      setCommandText('');
    }
  };

  return (
    <Card className="border-2 border-orange-200 bg-white/80 backdrop-blur-sm shadow-xl">
      <CardContent className="p-6">
        <div className="space-y-4">
          <div className="relative">
            <Textarea
              value={commandText}
              onChange={(e) => setCommandText(e.target.value)}
              placeholder="यहाँ अपना सवाल टाइप करें या माइक का उपयोग करें..."
              className="min-h-24 text-lg hindi-font border-orange-200 focus:border-orange-400 resize-none pr-20"
              disabled={isProcessing}
            />
            <div className="absolute top-3 right-3">
              <Button
                size="icon"
                onClick={handleMicClick}
                disabled={isProcessing}
                className={`rounded-full w-12 h-12 transition-all duration-300 ${isListening ? 'bg-red-500 hover:bg-red-600 animate-pulse' : 'bg-orange-500 hover:bg-orange-600'}`}
              >
                {isListening ? <MicOff className="w-6 h-6" /> : <Mic className="w-6 h-6" />}
              </Button>
            </div>
          </div>
          
          <motion.div
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
          >
            <Button
              onClick={handleSubmit}
              disabled={isProcessing || !commandText.trim()}
              className="w-full py-3 bg-gradient-to-r from-green-500 to-blue-500 hover:from-green-600 hover:to-blue-600 shadow-lg text-lg font-semibold hindi-font"
            >
              {isProcessing ? (
                <>
                  <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                  प्रोसेसिंग...
                </>
              ) : (
                <>
                  <Send className="w-5 h-5 mr-2" />
                  भेजें
                </>
              )}
            </Button>
          </motion.div>
        </div>
      </CardContent>
    </Card>
  );
}