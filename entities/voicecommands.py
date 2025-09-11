{
  "name": "VoiceCommand",
  "type": "object",
  "properties": {
    "command_text": {
      "type": "string",
      "description": "The voice command text"
    },
    "language": {
      "type": "string",
      "enum": [
        "hindi",
        "english",
        "tamil",
        "telugu",
        "bengali",
        "marathi",
        "gujarati",
        "punjabi",
        "kannada",
        "malayalam"
      ],
      "default": "hindi",
      "description": "Language of the command"
    },
    "category": {
      "type": "string",
      "enum": [
        "upi",
        "government_schemes",
        "local_services",
        "weather",
        "general",
        "health"
      ],
      "description": "Category of the command"
    },
    "response_text": {
      "type": "string",
      "description": "AI response to the command"
    },
    "audio_url": {
      "type": "string",
      "description": "URL of the recorded audio"
    },
    "status": {
      "type": "string",
      "enum": [
        "processing",
        "completed",
        "failed"
      ],
      "default": "processing",
      "description": "Status of command processing"
    }
  },
  "required": [
    "command_text",
    "language"
  ]
}