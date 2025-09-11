
import React, { useState, useRef } from 'react';
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Mic, MicOff, Square, Play, Pause } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

export default function VoiceRecorder({ onRecordingComplete, isProcessing }) {
  const [isRecording, setIsRecording] = useState(false);
  const [audioUrl, setAudioUrl] = useState(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const mediaRecorder = useRef(null);
  const audioRef = useRef(null);
  const chunks = useRef([]);

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      // Changed to a more compatible mimeType
      const options = { mimeType: 'audio/webm' };
      mediaRecorder.current = new MediaRecorder(stream, options);
      chunks.current = [];

      mediaRecorder.current.ondataavailable = (event) => {
        chunks.current.push(event.data);
      };

      mediaRecorder.current.onstop = () => {
        // Changed blob type and file extension to webm
        const blob = new Blob(chunks.current, { type: 'audio/webm' });
        const url = URL.createObjectURL(blob);
        setAudioUrl(url);
        const file = new File([blob], 'voice-command.webm', { type: 'audio/webm' });
        onRecordingComplete(file);
      };

      mediaRecorder.current.start();
      setIsRecording(true);
    } catch (error) {
      console.error('Error accessing microphone:', error);
    }
  };

  const stopRecording = () => {
    if (mediaRecorder.current && mediaRecorder.current.state === 'recording') {
      mediaRecorder.current.stop();
      mediaRecorder.current.stream.getTracks().forEach(track => track.stop());
    }
    setIsRecording(false);
  };

  const togglePlayback = () => {
    if (audioRef.current) {
      if (isPlaying) {
        audioRef.current.pause();
      } else {
        audioRef.current.play();
      }
      setIsPlaying(!isPlaying);
    }
  };

  return (
    <Card className="border-2 border-orange-200 bg-white/80 backdrop-blur-sm shadow-xl">
      <CardContent className="p-8">
        <div className="text-center space-y-6">
          <div className="hindi-font">
            <h3 className="text-2xl font-bold text-gray-900 mb-2">
              आवाज़ में बोलें
            </h3>
            <p className="text-gray-600">
              अपना सवाल या कमांड रिकॉर्ड करें
            </p>
          </div>

          <div className="flex justify-center">
            <AnimatePresence mode="wait">
              {!isRecording ? (
                <motion.div
                  key="start"
                  initial={{ scale: 0.8, opacity: 0 }}
                  animate={{ scale: 1, opacity: 1 }}
                  exit={{ scale: 0.8, opacity: 0 }}
                  transition={{ type: "spring", duration: 0.5 }}
                >
                  <Button
                    onClick={startRecording}
                    disabled={isProcessing}
                    className="w-20 h-20 rounded-full bg-gradient-to-r from-orange-500 to-red-500 hover:from-orange-600 hover:to-red-600 shadow-2xl hover:shadow-3xl transform hover:scale-105 transition-all duration-300"
                  >
                    <Mic className="w-8 h-8 text-white" />
                  </Button>
                </motion.div>
              ) : (
                <motion.div
                  key="recording"
                  initial={{ scale: 0.8, opacity: 0 }}
                  animate={{ scale: 1, opacity: 1 }}
                  exit={{ scale: 0.8, opacity: 0 }}
                  transition={{ type: "spring", duration: 0.5 }}
                  className="flex gap-4 items-center"
                >
                  <div className="flex items-center gap-3 bg-red-50 px-4 py-2 rounded-full">
                    <div className="w-3 h-3 bg-red-500 rounded-full animate-pulse"></div>
                    <span className="text-red-700 font-medium hindi-font">रिकॉर्डिंग चल रही है</span>
                  </div>
                  <Button
                    onClick={stopRecording}
                    className="w-16 h-16 rounded-full bg-red-600 hover:bg-red-700 shadow-xl"
                  >
                    <Square className="w-6 h-6 text-white fill-current" />
                  </Button>
                </motion.div>
              )}
            </AnimatePresence>
          </div>

          {audioUrl && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="flex justify-center items-center gap-4 bg-green-50 p-4 rounded-xl"
            >
              <audio
                ref={audioRef}
                src={audioUrl}
                onEnded={() => setIsPlaying(false)}
                className="hidden"
              />
              <Button
                onClick={togglePlayback}
                variant="outline"
                className="rounded-full w-12 h-12 border-green-300 hover:bg-green-100"
              >
                {isPlaying ? (
                  <Pause className="w-5 h-5 text-green-700" />
                ) : (
                  <Play className="w-5 h-5 text-green-700" />
                )}
              </Button>
              <span className="text-green-800 font-medium hindi-font">
                रिकॉर्डिंग तैयार है
              </span>
            </motion.div>
          )}

          {isProcessing && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="flex items-center justify-center gap-3 text-blue-700"
            >
              <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-blue-700"></div>
              <span className="font-medium hindi-font">प्रोसेसिंग हो रही है...</span>
            </motion.div>
          )}
        </div>
      </CardContent>
    </Card>
  );
}
