import React, { useState, useRef } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Volume2, VolumeX, Copy, Check } from "lucide-react";
import { motion } from "framer-motion";

export default function ResponseDisplay({ response, language }) {
  const [isPlaying, setIsPlaying] = useState(false);
  const [isCopied, setIsCopied] = useState(false);
  const speechRef = useRef(null);

  const speakResponse = () => {
    if ('speechSynthesis' in window) {
      if (isPlaying) {
        speechSynthesis.cancel();
        setIsPlaying(false);
        return;
      }

      const utterance = new SpeechSynthesisUtterance(response);
      
      // Set language for speech synthesis
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
      
      utterance.lang = langMap[language] || 'hi-IN';
      utterance.rate = 0.9;
      utterance.pitch = 1;
      
      utterance.onstart = () => setIsPlaying(true);
      utterance.onend = () => setIsPlaying(false);
      utterance.onerror = () => setIsPlaying(false);
      
      speechSynthesis.speak(utterance);
    }
  };

  const copyToClipboard = () => {
    navigator.clipboard.writeText(response);
    setIsCopied(true);
    setTimeout(() => setIsCopied(false), 2000);
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <Card className="border-2 border-green-200 bg-white/90 backdrop-blur-sm shadow-xl">
        <CardHeader className="pb-3">
          <CardTitle className="flex items-center justify-between hindi-font">
            <span className="text-green-800">AI का जवाब</span>
            <div className="flex gap-2">
              <Button
                onClick={speakResponse}
                variant="outline"
                size="sm"
                className="border-green-300 hover:bg-green-50"
              >
                {isPlaying ? (
                  <VolumeX className="w-4 h-4 text-green-700" />
                ) : (
                  <Volume2 className="w-4 h-4 text-green-700" />
                )}
              </Button>
              <Button
                onClick={copyToClipboard}
                variant="outline"
                size="sm"
                className="border-green-300 hover:bg-green-50"
              >
                {isCopied ? (
                  <Check className="w-4 h-4 text-green-700" />
                ) : (
                  <Copy className="w-4 h-4 text-green-700" />
                )}
              </Button>
            </div>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="prose max-w-none hindi-font">
            <p className="text-gray-800 text-lg leading-relaxed whitespace-pre-wrap">
              {response}
            </p>
          </div>
        </CardContent>
      </Card>
    </motion.div>
  );
}